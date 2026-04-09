
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

#### Core Componets
1. Enable MFA on root user
2. Use Roles instead of IAM user 
3. Avoid wildcarts (*) in policies
4. Use IAM Access Analyzer
5. Rotate Access keys or eliminate them
6. Use Service Control policies (SCP) at Org level

### IAM vs Related AWS Services


| Service | Purpose |
|------|------|
| IAM | Permissions & authorization |
| AWS Organizations | Multi‑account governance (SCPs) |
| AWS STS | Temporary credentials |
| Amazon Cognito | App user authentication |
| AWS IAM Identity Center (SSO) | Workforce identity |

### When You’ll Touch IAM Most (DevOps View)

- Writing **bucket/KMS policies**
- Creating **cross‑account roles**
- Locking down access using **Conditions**
- Enforcing compliance (SOX, audit)
- Integrating EC2/Lambda/S3 securely
