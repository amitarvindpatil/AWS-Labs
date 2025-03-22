# Elastic Network Interface (ENI) - Hands On
###### 1. Launch 2 EC2 instances as per that It create 2 ENI per instance in-use state
###### 2. Goto Instance Network Interface in EC2 service and create an network interface
###### 3. Config the inputs such as Subnet-Id and IPv4 address and select SG
###### 4. After  Creation, Its in available state then Click On Action and attach to Instance

# Placement Group HandsOn
###### 1. In EC2 Service and goto placement group section
###### 2. Create placement group with below config
###### 3. Name - `placement-group-example` and strategy `(Cluster,Spread and Partition)`
###### 4. Create and instance go to placement group in advance config section here we able to see the placement group as we created