### Create Django-Deployement-on-EC2
```
1. Launch EC2 Instance with port 22 SG and Custom Port set with 8000 and source as anywhere
2. Login to Server
3. sudo apt-get update
4. git clone https://github.com/yeshwanthlm/django-on-ec2.git
5. sudo apt install python3-pip -y / sudo apt install python3-full
6. pip install django / sudo apt install python3-django
7. python3 manage.py makemigrations
8. python3 manage.py migrate
9. python3 manage.py createsuperuser
10. python3 manage.py runserver 0.0.0.0:8000
11. Copy ip address with run on browser e.g. http://54.122.23.44:8000
```
