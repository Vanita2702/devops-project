Overview
	
A simple Flask-based Python web application that displays the message “Hello DevOps! Version: v1” when accessed through a web browser.



Tech Stack

*  Python – Programming language 
*  Flask – Lightweight web framework for building the web application 
*  Pip – Package manager for installing dependencies


Setup Steps

1) Creating and cloning project to github.

Code path: https://github.com/Vanita2702/devops-project/blob/main/app/app.py 

2) Installing dependencies and testing

pip install -r requirements.txt








3) Adding a test condition file to validate.

Code path: https://github.com/Vanita2702/devops-project/blob/main/tests/test_app.py 

pip install pytest                   #pytest is a python testing framework.
python -m pytest  tests/








Dockerfile Steps

1) Creating docker file
       

2) Build the docker image and run
   
    Docker build -t <dockerhub-username>/<repo-name>:<tag> .

  


3) 
