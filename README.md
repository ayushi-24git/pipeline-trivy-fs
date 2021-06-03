
<h1>
Pipeline-trivy

</h1>
This repository demonstrates Trivy, a vulnerability management tool for images and containers. The elaborate working can be understood [here](https://rastogee-ayushi.medium.com/trivy-keep-your-artifacts-vulnerability-free-6dce292134e5).  

The repo contains a single task, scan-fs, which scans the given folder on your local through Trivy tool. Since Trivy can only scan repositories with lock files, if your filesystem contains any kind of lock files, you can straightway **cd** inside the folder and do `trivy fs .`. Otherwise, you can first generate a lock file and then  scan the repo. Here, I have tried to generate Pipfile.lock file for my Python project on local and then scanned it for vulnerabilities. For support of other languages, you can take a look [here](https://aquasecurity.github.io/trivy/v0.18.3/vuln-detection/library/).

If you have **minikube** on your laptop, do a `minikube start` and run the following commands:

<h2>Installing the tasks</h2>  


  `kubectl apply -f https://raw.githubusercontent.com/ayushi-24git/pipeline-trivy/main/tasks/vulnerable-image.yaml`  
  
  `kubectl apply -f https://raw.githubusercontent.com/ayushi-24git/pipeline-trivy/main/tasks/scan-image.yaml`  
  


<h2>Applying pipeline yamls</h2>  


  `kubectl apply -f https://raw.githubusercontent.com/ayushi-24git/pipeline-trivy/main/pipeline.yaml`  
  
  `kubectl apply -f https://raw.githubusercontent.com/ayushi-24git/pipeline-trivy/main/pipelinerun.yaml`  
  
After applying the above, you can start the Tekton pipeline by running `tkn pipeline start scan-pipeline-fs`. After this, the pipeline starts and you will be prompted to enter the directory of the folder you want to scan. Check for the logs and you can see the table of all vulnerabilities detected by Trivy.
  
