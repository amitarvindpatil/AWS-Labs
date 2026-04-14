#### Lab: Configure Password Policy
    1. Goto IAM Service --> Account Settings
    2. Select Edit Password Policy
    3. select Custom Option
    4. fillup and set the input for password configuration like password minimum length and strength and Other Requirements
    5. Note: uncheck Password expiration requires administration reset
    6. Save Changes


#### Lab: Configure User Groups and Add User in it

    1. IAM Service - Select User Groups
    2. Set the Name - "Developer" to Groups 
    3. Attach users in the group (Optional)
    4. Provide Permission to group
    5. Create user group

    User Create:
    1. Select User and set Name - "Amit"
    2. Add Permission Options - Add user to group (good practice), Copy Permission (bad practice), Attach policy Directly (Bad Practice)
    3. Select user group (Developer)
    4. Review and Create User

    Note: if we select Provide user access to the AWS Management Console - optional
    then here we need configure Password to access Console

#### Lab: Create Policy and attach to user for access s3 bucket

    1. Create S3 bucket 
    2. create user as "Sarang" do not attach permission
    3. Create policy to allow permission 
    4. Click on Action and attach to user "Sarang" (iam-policy-for-sarang.json)

#### IAM Permission Boundries

    1. Create a user "shraddha"
    2. Attach direct administration access permission
    3. Create a policy as "scopepermissions.json" attach policy (present in files)
    4. goto user configuration - Permission boundrary and attach ScopePermission policy
    5. login with shraddha and try to launch instance
    6. try to create new user "userx" from Shraddha with same procdure we did for shraddha like attach boundrary 

    It's not allow to create even have admin permission
    even we login to userx and launch ec2 instance still getting denied permission

#### IAM policy Simulator

    goto iam - right hand panel (Tools)- IAM policy Simulator
    - create an user and assign some permission and try to check with Simulator
    here we can see the user has which permission 

#### IAM Role - Switch Role usecase (Trust RelationShip)

    1. goto dev acccount - IAM
    2. Create group "externalContractor" - attach permission s3fullAccess 
    3. create user "maggie" add into externalContractor group
    
    4. goto prod account - s3 bucket("rr-cutomer-feedback")
    5. iam - create policy Name:- "Rr-iam-policy-maggie"  copy policy(cross-account-iam-role-for-s3-bucket.json) - update policy s3 bucket arn (
    6. Create a role - select "AWS Account" - An AWS Account (set Dev AccountID)
    7. Select Policy "Rr-iam-policy-maggie" 
    8. provide RoleName - AIUpdateRole
    
    9. goto dev acccount - maggie user configuration - Permission - Add Inline Policy
    10.  Add (assumerole-for-maggie.json) - replace placeholder
    11. login as maggie - in dev 
    12. try to switch role in production account and goto s3 bucket access the bucket

#### Resouce Based policy (Bucket-policy) - Refer trust relationship senario

    1. goto prod acccount - s3 - rr-cutomer-feedback bucket - bucket policy
    2. replace maggie user arn into principal - refer policy from resouces-basedpolicy.json
    3. sign with dev - maggie
    4. copy the bucket url of rr-cutomer-feedback from prod and search on web  
