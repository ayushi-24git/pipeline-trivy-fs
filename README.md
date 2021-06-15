<h1>
Pipeline-trivy-fs

</h1>
This repository demonstrates Trivy, a vulnerability management tool for images and containers. It uses Tekton pipeline under the hood.  



This repository contains a single task, **scan-fs**, which scans the given folder on your local through Trivy tool. Since Trivy can only scan repositories with lock files, if your filesystem contains any kind of lock files, you can straightway **cd** inside the folder and do `trivy fs .`. Otherwise, you can first generate a lock file and then  scan the repo. Here, I have tried to generate Pipfile.lock file for my Python project on local and then scanned it for vulnerabilities. For support of other languages, you can take a look [here](https://aquasecurity.github.io/trivy/v0.18.3/vuln-detection/library/). Further working of Trivy can be understood [here](https://rastogee-ayushi.medium.com/trivy-keep-your-artifacts-vulnerability-free-6dce292134e5). 

## Setting up cluster
Set up a cluster using minikube by doing a minikube start.

## Setting up Tekton
Install tekton with the following command after setting up the cluster

kubectl apply --filename https://storage.googleapis.com/tekton-releases/pipeline/latest/release.yaml

This will install all the necessary Tekton components to get started.

## Applying the Tasks and Pipeline yamls
Apply all the mentioned tasks in the repositorry above. Example format:

kubectl apply -f https://raw.githubusercontent.com/ayushi-24git/pipeline-trivy-tekton/main/tasks/scan-fs.yaml

Apply the pipeline yamls as:

kubectl apply -f https://raw.githubusercontent.com/ayushi-24git/pipeline-trivy-tekton/scan-pipeline-fs.yaml

kubectl apply -f https://raw.githubusercontent.com/ayushi-24git/pipeline-trivy-tekton/scan-pipelinerun-fs.yaml

Now, start the pipeline by: `tkn pipeline start scan-pipeline-fs`. Now, you will be prompted to enter the absolute path of the folder you want to scan. Check for the logs and you can see the table of all vulnerabilities detected by Trivy.


Check logs
Now, the pipeline has successfully started. You can check the logs using the following command:

`tkn pipelinerun logs <name-of-the-pipelinerun>`
You can see the table of all vulnerabilities (if any) detected by Trivy.

  



  

  

  
