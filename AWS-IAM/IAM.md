
#### IAM - Identity Access Management
IAM is globle Service use to manage access to all AWS Serviecs and Resouces
IAM lets you
- Authenticate Identity (Who you are)
- Authorize Action (what you allow to do)
- Securely manage access to cloud resources using least-privileges principles. 

#### Core Componets
1. Identity
 - Root user :- Created user when AWS account is Created , has full Access AWS account. 

 - IAM user :- Individual User (e.g. admin,developer)

 - IAM Roles :- Assumed by user, Serviecs or external identities, Use Temp credentials (best practice)

2. Policies
Policies are JSON documents that defines:
- Action (e.g. s3:GetObject)
- Resouces (e.g. Bucket ARN)
- Effect (e.g. Allow or Deny)
- Conditions (IP,MFA,time,tags)

Example:
        
        {
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Action": ["s3:GetObject"],
            "Resource": "arn:aws:s3:::my-bucket/*"
        }]
        }
