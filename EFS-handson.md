## EFS Lab
###### 1. Create 2 EC2 instances in public subnet for login server
###### 2. Security Group for EC2 : SSH
###### 3. Create SG `efs-demo-test` for EFS with add in-bound rule NFS and all both instances SG 
###### 4. Goto EFS Service and Create EFS and select customize option (good practice)
###### 5. config the General file settings (as per the requirement)
###### 6. config the Network Access select vpc and replace existing SG with `efs-demo-test` and create it
###### 7. Login both Servers

###### 8. Run below commands on both Server
###### `-sudo su`
###### `-yum install -y amazon-efs-utils`
###### `-mkdir efs` mount directory
###### - Copy mount commands from EFS Attach section
###### `-echo "hello World" > efs/index.html` Run this command on any one server
###### `-ls efs` run on second mounted server
