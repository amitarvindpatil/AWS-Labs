
### What is APIGateway?

AWS API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale.

Think of it as a smart receptionist for your backend services. 

It handles all the tasks involved in accepting and processing
 up to hundreds of thousands of concurrent API calls.

### Why use it?

- Scalability: Automatically scales to handle incoming traffic.
- Security: Offers throttling, authorization, and access control.
- Efficiency: Supports multiple API versions for iterative development.
- Monitoring: Integrated with Amazon CloudWatch.

### How does it works?

 API gateway act as reverse proxy, accepting API calls from client and routing them to appropriate backends ServiceLambda,
EC2,HTTPEndpoints or AWS Resouces

### Understand API Methods ?

| Methods   |   Purpose
| GET    | Retrives data (Read-Only)
| POST  |  Storeing Data to Create Resources
| PUT   |  Updates or Create Resouces
| Delete  | Remove Data or resouces
|Patch |  Applies Partial Updates
