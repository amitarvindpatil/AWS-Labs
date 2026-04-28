### Validator,Request Body and Query String

Step 1. Create Lambda a create a new Python function and use this code: Name:- Lambda-validator-demo

    import json

    def lambda_handler(event, context):
        name = event.get("name")
        
        if not name:
        params = event.get('queryStringParameters',{})
        name = params.get('name','world')

        response_data = {
            "statusCode": 200,
        "body": f"Request Payloads = {event}!"
        }

Step 2. Create a REST API in API Gateway

    1. Goto to the API Gateway and Create API
    2. Choose REST API then Click on Build
    3. Name: Request-validator-api - Create API

Step 3: Create a Resource and Method

    1. Click on Action and Create Resource
    2. Name : Request-validator-api
    3. with Resources Selected, Click on Action Create POST method
    4. Configure the method:
        - Integration Type: Lambda Function
        - Use Lambda Proxy Integration: Checked
        - Lambda Function: Select the one you created earlier - Lambda-validator-demo

Step 4.: Create a Model

    1. Click on Models on left side panel
    2. Create a Model Name:DemoRequestValidator,Content-type:application/json

    model-schema

    {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "title": "RequestModel",
    "type": "object",
    "required": ["name", "email", "mobile-number"],
    "properties": {
        "name": { "type": "string", "minLength": 1 },
        "email": { "type": "string", "format": "email" },
        "mobile-number": { "type": "integer", "minimum": 1000000000, "maximum": 9999999999 }
    },
    "additionalProperties": false
    }

    3. Create and goto resouces-method request-Request-Validator:validate body,query String parameter and headers,Request Body ->
    content-type -application/json Model:- DemoRequestValidator

Step 4: Deploy Your API

    1. Click Action Deploy API
    2. Choose ["New Stage"]- Name: Dev
    3. After Deployment, you will see Invoke URL

    "https://{api-id}.execute-api.{region}.amazonaws.com/dev/Request-validator-api"
    To test it, go to Postman: select raw option - json

    {
    "name":"amit-test",
    "email":"amitpatil@gmail.com",
    "mobile-number":"9834232323"
    }
