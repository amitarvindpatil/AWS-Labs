### AWS Organisation 
AWS Organizations is a free, global service for centrally managing and governing multiple AWS accounts. It’s commonly used by enterprises to enforce security, control costs, and standardize governance across teams and projects.

Usage:

        1. multiple Teams or Department
        2. Seprate Environments (DEV,PROD,TEST) 
        3. Compliance and security requirements
        4. Need for centralized billing and access control

Key Concept:

        1. Organisation:- A container to all your AWS accounts
        2. Management A/C :- The root account that creates and controls the organization
        3. Member A/C :- AWS accounts within the organization
        4. Organizational Units (OUs) :- Logical groupings of accounts, Used to apply policies at scale

Structure:

        Root
        ├── Security
        │    ├── Log-Archive
        │    └── Security-Tools
        ├── Production
        │    ├── App1-Prod
        │    └── App2-Prod
        └── Non-Production
            ├── Dev
            └── Test
Feature:
        
        1.  Service Control Policies(SCP): Guardrails, not permissions
        2.  Consolidated Billing:- Single bill for all accounts
        3.  Account Management & Automation:- Create accounts programmatically
        4.  Centralized Security & Compliance:- Enforce security standards

Common Best Practices
        
        1.  Use multiple accounts, not multiple VPCs only
        2.  Keep management account isolated
        3.  Use SCPs as guardrails, not daily access control
        4. Separate accounts for: Security, Logging, Enable CloudTrail and Config at organization level

Lab: Create AWS Orgnizations, OU'S and Accounts

        1. Goto AWS management account and goto AWS Orgnizations Services
        2. Create AWS Orgnizations
        3. Create new OU 
        4. Select root and goto action and create New OU (Development,Test,Prod) etc.
        5. Add AWS Account (dev)
        6. login to Dev account copy account-id
        7. back to management account and Add new AWS account 
        8. 2 option we have (Create an AWS account and Invite an existing account)
        9. put the account-id and details and send invite
        10. goto dev account goto aws organization service
        12 goto invitation and accept it
        13. Now for production we will create new account.
        14 goto Add aws new account and select Create AWS account
        15. fill the details Name of account(production) email and Tags etc and create.
        17. move AWS dev and prod account int OU's 
