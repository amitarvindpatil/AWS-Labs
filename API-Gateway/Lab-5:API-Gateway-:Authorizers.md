#### API Gateway : Authorizers
user --> API Gateway --> Authorize --> authenticate(yes) --> API

Authorization:
- Setup Auth Lambda
- Pass Auth Token
- Lambda validates
- User is allow to access api

Step 1. Create Lambda a create a new Python function and use this code for Setup Auth Lambda: Name:- Lambda-api-authorizer

    import json

    def generate_policy(principal_id, effect, resource):
        return {
            "principalId": principal_id,
            "policyDocument": {
                "Version": "2012-10-17",
                "Statement": [{
                    "Action": "execute-api:Invoke",
                    "Effect": effect,
                    "Resource": resource
                }]
            }
        }

    def lambda_handler(event, context):
        token = event['authorizationToken']
        method_arn = event['methodArn']

        if token == "Bearer mysecrettoken":
            return generate_policy("user", "Allow", method_arn)
        else:
            return generate_policy("user", 
            "Deny", method_arn)

Step 2. 

    1. Select the API - Lambda-validator-demo
    2. goto authorizers (left panel) - Create
    3. Authorizer name: authrizerforlamdba-validator-demo, Authorizer type: Lambda - select the arn Lambda-api-authorizer
    Lambda event payload - Token, Token source: authorization Token - Create

Step 3. validate authorizer Test Authorizer - copy it from lambda code

Step 4: Attach authorizer with API
    
    1. goto to resouces of api - POST - method request -edit
    Authorization - choose authrizerforlamdba
    
    2. Redeploy Lambda-validator-demo api
    3. hit the url again into postman without authorizer token - it give an error -unauthorized
    4. click on header key:authorizationToken value :- pass the Token
