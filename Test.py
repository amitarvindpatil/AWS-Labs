import json
import logging
from os import getenv
from typing import TypedDict, List, Optional, Any
from datetime import datetime

import boto3
from logger import log
from botocore.exceptions import ClientError

BUCKET_REPORTS_NAME = getenv("REPORTS_BUCKET")
client = boto3.client("s3")

MAX_RESULTS = 100


# =========================
# Event Input
# =========================
class Event(TypedDict, total=False):
    FromDate: str   # YYYY-MM-DD
    ToDate: str     # YYYY-MM-DD
    Limit: int
    NextToken: str


class ReportDetails(TypedDict):
    ReportId: str
    ETag: str
    Size: int
    LastModified: str
    Key: str


# =========================
# Helper: Parse datetime from key
# =========================
def parse_key_datetime(key: str) -> Optional[datetime]:
    """
    Converts key like:
    2026-04-20T13:48:33:345123
    into datetime
    """
    try:
        # Fix non-standard microseconds format
        # Replace last ":" with "."
        if key.count(":") >= 3:
            parts = key.rsplit(":", 1)
            key_fixed = parts[0] + "." + parts[1]
        else:
            key_fixed = key

        return datetime.fromisoformat(key_fixed)
    except Exception:
        return None


# =========================
# S3 list with pagination
# =========================
def list_objects(prefix: str, continuation_token: Optional[str]):
    kwargs = {
        "Bucket": BUCKET_REPORTS_NAME,
        "Prefix": prefix,
    }

    if continuation_token:
        kwargs["ContinuationToken"] = continuation_token

    log.info("S3 list kwargs: %s", kwargs)

    response = client.list_objects_v2(**kwargs)
    return response


# =========================
# Process objects
# =========================
def process_objects(
    contents: List[Any],
    from_date: datetime,
    to_date: datetime,
) -> List[ReportDetails]:

    items: List[ReportDetails] = []

    for o in contents:
        key = o["Key"]

        key_dt = parse_key_datetime(key)
        if not key_dt:
            continue

        # ✅ Date filtering
        if key_dt < from_date or key_dt > to_date:
            continue

        item: ReportDetails = {
            "ReportId": key,  # no separate ID
            "ETag": o["ETag"],
            "Size": o["Size"],
            "LastModified": str(o["LastModified"]),
            "Key": key,
        }

        items.append(item)

    return items


# =========================
# Main business logic
# =========================
def get_reports(
    limit: int,
    from_date_str: str,
    to_date_str: str,
    next_token: Optional[str],
):
    from_date = datetime.fromisoformat(from_date_str)
    to_date = datetime.fromisoformat(to_date_str)

    # 🔥 Prefix optimization (use only start date)
    prefix = from_date_str  # e.g. "2026-04-20"

    response = list_objects(prefix, next_token)

    contents = response.get("Contents", [])
    log.info("S3 returned %d objects", len(contents))

    items = process_objects(contents, from_date, to_date)

    # ✅ Sort latest first
    items.sort(
        key=lambda x: parse_key_datetime(x["Key"]),
        reverse=True
    )

    return {
        "Reports": items[:limit],
        "NextToken": response.get("NextContinuationToken"),
    }


# =========================
# Lambda entry
# =========================
def main(event: Event, context):
    log.info("event: %s", event)

    from_date = event.get("FromDate")
    to_date = event.get("ToDate")

    if not from_date or not to_date:
        raise ValueError("FromDate and ToDate are required")

    limit = int(event.get("Limit") or MAX_RESULTS)
    next_token = event.get("NextToken")

    # ✅ Validation
    if from_date > to_date:
        raise ValueError("FromDate must be <= ToDate")

    result = get_reports(
        limit=limit,
        from_date_str=from_date,
        to_date_str=to_date,
        next_token=next_token,
    )

    log.info("Returned %d reports", len(result["Reports"]))

    return result
