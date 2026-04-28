

#### API Gateway: Resource Policy

Step 1. Get the IP address of laptop

Step 2: Create resource policy

    1. goto the API Gateway - resource policy -(left panel) - Create
    2. Select a template : IP range deny list 
    3. paste IP address into array of aws:SourceIP , update the Resouces : as api url e.g. /dev/Lambda-validator-demo
    Note: deny alway takes first response
    4. Redeploy Lambda-validator-demo api
    5. hit the url again into postman
