### Lab - AWS Orgnizations and Cross Account Access
    ===========================================================
    1. login to prod root user email
    2. goto iam - roles - OrgnizationAccountAccessRole
    3. click on trust relationship
    4. goto management account create user "Alice" with permissions (Administrator)
    5. login management account with Alice 
    6. goto Switch Role and login production account 
    7. able to access Orgnizations Cross accounts
    8. goto dev account and IAM Roles
    9 not Able to see OrgnizationAccountAccessRole
    10. Create a role Trust entity type - AWS Account
    11. Another account - Management account-id
    12 . permissions - administrator access
    13. Switch Role with Development accout
