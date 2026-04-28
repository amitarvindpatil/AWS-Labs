### API Gateway: CloudWatch logging

API Gateway -- IAM Role --CloudWatch Log

Step 1. Create a IAM Role

    1. IAM -> Roles -> Trusted Entity: AWS Service,Use Case: API Gateway
    2. PemissionPolicy - AmazonapiGatewayPushToCloudwatchlogs, Name:APIGatewayCloudWatchIAMRole
    3. Copy ARN
    4. Goto APIGateway - setting (left panel) - logging - and paste the ARN

Step 2 : How to logging the API Gateway

    1. Choose Request-validator-api - click on Stages (left panel)
    2. goto logging and tracing - edit - CloudWatch logs : Errors and info logs
    Enable :Data tracing,Detailed matrics

Step 3 : How to find cloudwatch log groups
    1. copy api -ID (unique)
    2. cloudwatch - log groups - search ID 
