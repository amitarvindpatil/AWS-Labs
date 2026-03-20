import json
import logging
from os import getenv
from typing import TypedDict, List, Optional, Any
from datetime import datetime, timedelta

import boto3
from logger import log
from botocore.exceptions import ClientError

BUCKET_REPORTS_NAME = getenv("REPORTS_BUCKET")
client = boto3.client("s3")

MAX_RESULTS = 100


class Event(TypedDict, total=False):
    Limit: str
    FromDate: str   # YYYY-MM-DD
    ToDate: str     # YYYY-MM-DD
    NextToken: str  # used within a single prefix


class ReportDetails(TypedDict):
    ReportId: str
    ETag: str
    Projects: List[str]
    Key: str
    Size: int
    LastModified: str


# 🔥 Generate date prefixes
def generate_date_prefixes(from_date: str, to_date: str) -> List[str]:
    start = datetime.fromisoformat(from_date)
    end = datetime.fromisoformat(to_date)

    prefixes = []
    current = start

    while current <= end:
        prefix = f"reports/{current.strftime('%Y/%m/%d')}/"
        prefixes.append(prefix)
        current += timedelta(days=1)

    return prefixes


# 🔥 S3 list with pagination
def list_objects(prefix: str, continuation_token: Optional[str] = None):
    kwargs = {
        "Bucket": BUCKET_REPORTS_NAME,
        "Prefix": prefix,
    }

    if continuation_token:
        kwargs["ContinuationToken"] = continuation_token

    log.info("list_objects kwargs: %s", str(kwargs))

    response = client.list_objects_v2(**kwargs)
    return response


def _get_object_projects_metadata(key: str) -> List[str]:
    try:
        head = client.head_object(Bucket=BUCKET_REPORTS_NAME, Key=key)
    except ClientError:
        return []

    metadata = head.get("Metadata") or {}
    raw = metadata.get("projects")

    if not raw:
        return []

    try:
        parsed = json.loads(raw)
        if isinstance(parsed, list):
            return parsed
        return [str(parsed)]
    except Exception:
        if "," in raw:
            return [seg.strip() for seg in raw.split(",") if seg.strip()]
        return [raw.strip()]


# 🔥 Process objects
def process_objects(contents: List[Any]) -> List[ReportDetails]:
    items: List[ReportDetails] = []

    for o in contents:
        key = o["Key"]
        parts = key.split("/")

        # reports/YYYY/MM/DD/<report_id>/report.zip
        if len(parts) == 6 and parts[-1] == "report.zip":
            report_id = parts[4]

            projects = _get_object_projects_metadata(key)

            item: ReportDetails = {
                "ReportId": report_id,
                "ETag": o["ETag"],
                "Size": o["Size"],
                "LastModified": str(o["LastModified"]),
                "Projects": projects,
                "Key": key,
            }

            items.append(item)

    return items


# 🔥 Main logic (multi-prefix + pagination)
def get_reports(limit: int, from_date: str, to_date: str, next_token: Optional[str]):
    prefixes = generate_date_prefixes(from_date, to_date)

    all_items: List[ReportDetails] = []
    next_token_out = None

    for prefix in prefixes:
        response = list_objects(prefix, next_token)

        contents = response.get("Contents", [])
        items = process_objects(contents)

        all_items.extend(items)

        # Handle pagination per prefix
        if response.get("IsTruncated"):
            next_token_out = response.get("NextContinuationToken")
            break  # stop and return next token

    # Sort globally
    all_items.sort(key=lambda x: x["LastModified"], reverse=True)

    return {
        "Reports": all_items[:limit],
        "NextToken": next_token_out,
    }


# 🔥 Lambda entry
def main(event: Event, context):
    log.info("event: %s", str(event))

    limit = int(event.get("Limit") or str(MAX_RESULTS))
    from_date = event.get("FromDate")
    to_date = event.get("ToDate")
    next_token = event.get("NextToken")

    if not from_date or not to_date:
        raise ValueError("FromDate and ToDate are required")

    result = get_reports(limit, from_date, to_date, next_token)

    return result
