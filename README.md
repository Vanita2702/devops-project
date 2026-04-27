Overview
	
A simple Flask-based Python web application that displays the message “Hello DevOps! Version: v1” when accessed through a web browser.



Tech Stack

?  Python – Programming language 
?  Flask – Lightweight web framework for building the web application 
?  Pip – Package manager for installing dependencies


Steps

1) Creating and cloning project to github.

Code path: https://github.com/Vanita2702/devops-project/blob/main/app/app.py 

2) Installing dependencies and testing

pip install -r requirements.txt








3) Adding a test condition file to validate.

Code path: https://github.com/Vanita2702/devops-project/blob/main/tests/test_app.py 

pip install pytest                   #pytest is a python testing framework.
python -m pytest  tests/






Making a change to see that if the test case is invalid or wrong the pipeline should fail.








Dockerfile Steps

1) Creating docker file
       

2) Build the docker image and run
   
    Docker build -t <dockerhub-username>/<repo-name>:<tag> .

  


3) Pushing docker image from Github Action 

Yaml path:- https://github.com/Vanita2702/devops-project/blob/main/.github/workflows/ci.yaml 

Steps to add docker username and password
o Go to project repository  > Settings
o On Left side drill down to Secret and Variables  > Actions
o Click on new repositoritory secret and add username and password of dockerhub.







4) Login into dockerhub to see the image.
        
	












Kubernetes Steps – Kubernetes pulls the image from dockerhub


1) Create a deployment and service yaml file. Push to github repo.

https://github.com/Vanita2702/devops-project/tree/main/k8s 






2) Apply k8s folder which consist of deployment and service.




	












ARGOCD – Argocd deploys 

1) Install Argocd


2) Access UI by generating the password








3) Add new application 
 














4) Make a simple change and verify if the changes are synced.



Checkpoints to verify the changes: -
1) Make a change in app.py
2) Commit and sync changes
3) Check github actions
4) Check dockerhub image is updated
5) See if all pods are running and restart the deployment.
6) Argocd-sync-refresh-browse


















K8s monitoring dashboard
1) Install and create a service account dashboard.


2) Create cluster role binding
            

3) Generate a token i.e. password 
 

4) Expose it and login in using the token generated above.












Output:



