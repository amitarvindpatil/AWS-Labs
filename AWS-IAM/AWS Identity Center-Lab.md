#### AWS Identity Center

    1. Login to management acccount - alice user - Senior Administrator 
    2. AWS organiztion - check the structure of prod and dev account
    3. goto identity center - Enable - Groups
    4. create a group "Senior Solution Architect"
    5. Create user "arther" - add him into "senario Solution Architect" group
    6. Goto AWS Account - select Prod and Dev Account and add group  "Senior Solution Architect"
    7. Create Permission Sets - Select Predefine Set () - custom permission set (good practice)
    8. select AdministratorAccess - specify permission details Name (RRSolutionArchitectPolicy)- set session duration (1 hrs)
    9. select created permission finish the process
    10. Accept invitation through email
    11. login and test it
