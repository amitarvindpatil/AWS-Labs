### Create First API with Lambda

Step 1. Create Lambda a create a new Python function and use this code: Name:- Lambda-proxy-demo

    import json

    def lambda_handler(event, context):
        name = "World"
        if event.get('queryStringParameters'):
            name = event.get('queryStringParameters').get('name', name)

        response_data = {
            "message": f"Hello, {name}! Your request was successful.",
            "status": "success"
        }

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(response_data)
        }

Step 2. Create a REST API in API Gateway

    1. Goto to the API Gateway and Create API
    2. Choose REST API then Click on Build
    3. Select New API, Name :- FirstAPI and Click Create API

Step 3: Create a Resource and Method

    1. Click on Action and Create Resource
    2. Name : proxy-demo
    3. with Resources Selected, Click on Action Create GET method
    4. Configure the method:
        - Integration Type: Lambda Function
        - Use Lambda Proxy Integration: Checked
        - Lambda Function: Select the one you created earlier - Lambda-proxy-demo
    5. Click Save and accept the permissions prompt.

Step 4: Deploy Your API

    1. Click Action Deploy API
    2. Choose ["New Stage"]- Name: Dev
    3. After Deployment, you will see Invoke URL

    "https://{api-id}.execute-api.{region}.amazonaws.com/dev"
    To test it, go to:
    "https://{api-id}.execute-api.{region}.amazonaws.com/dev/proxy-demo?name=Rahul"
