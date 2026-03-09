### Service Control Policy

Service Control Policies (SCPs) are a key governance feature of AWS Organizations that help you centrally control and restrict what actions AWS accounts can perform within an organization.

An SCP is a JSON-based policy that:
Is applied at the organization, OU, or account level
Limits AWS service actions that can be used
Affects all IAM users, roles, and root users in member accounts

SCPs help organizations to:

    Enforce security standards
    Maintain compliance
    Prevent accidental or malicious actions
    Control service and region usage
    Reduce blast radius across accounts

SCP affects on IAM user,Roles and  Root user of member accounts
Deny List SCPs (Most Common Example):

    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Action": [
            "ec2:*",
            "s3:*"
          ],
          "Resource": "*"
        }
      ]
    }

common use cases:
      
    Security Enforcement
        - Prevent disabling CloudTrail
        - Block deletion of Config rules
        - Enforce encryption settings
    Region Restrictions
        - Allow resources only in approved regions (e.g., ap-south-1)
    Cost Control
        - Deny expensive services
        - Restrict instance types
    Compliance
        - Enforce least privilege at org level
        - Prevent usage of non-approved services

Best Practices for SCPs

    ✅ Start with deny-based SCPs
    ✅ Test SCPs in non-production OUs first
    ✅ Keep SCPs simple and well-documented
    ✅ Avoid over-restricting (can block AWS services unexpectedly)
    ✅ Always maintain break-glass access in IAM

Simple Real-World Example

    Company scenario:
      Root SCP:
        Deny all regions except India
      Production OU SCP:
        Deny deleting logs
        Deny stopping security services
      Dev OU SCP:
        Allow more flexibility

Lab - Create Orgnizations SCP
=================================================
    1. In AWS organization of management account click on policies section
    2. goto SCP and enable it
    3. Create a policy 
    Name: PreventOrgLeave

    Policy statement
            {
            	"Version": "2012-10-17"
            	"Statement" : [
            		{
            			"Effect" : "Deny",
            			"Action" : [
            				"organization:LeaveOrganization"
            			],
            			Resources: "*"
            		
            		}
            	]
            
            }
    4. Click a target and attach OU
    5. goto dev accout and goto AWS Orgnizations
    6. click on leave the organization and try it

