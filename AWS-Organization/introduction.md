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
