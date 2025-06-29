**Assignment1:**

1. 💻 Microservice Development
Write a microservice in Python or Go.
The service must:
Accept three inputs:
From currency (dropdown)
To currency (dropdown)
Amount (input box)
Query a live exchange rate API (e.g., exchangerate.host or openexchangerates.org) to perform real-time conversion.
Return the converted amount to the user.
Deliverables:
REST API (e.g., /convert?from=USD&to=EUR&amount=100)
Minimal web UI with dropdowns and textbox (can be Flask, FastAPI, or minimal frontend in Go).

2. 📦 Docker
Create a Dockerfile to containerize your application.
The Dockerfile should:
Use minimal base image (e.g., python:slim or golang:alpine)
Copy source, install dependencies, and expose necessary ports.
Use a non-root user (bonus).
Deliverables:
Working Dockerfile
Application should run with docker build and docker run.

3. 🔁 CI/CD Pipeline
Choose Jenkins, GitHub Actions, Bitbucket Pipelines, or any other supported CI/CD tool.
Pipeline should:
Build Docker image.
Push image to a container registry (Docker Hub, GitHub Packages, or similar).
Lint/test Helm charts (bonus).
Deliverables:
CI/CD config file (e.g., .github/workflows/pipeline.yml)
Brief README.md on how to trigger and observe the pipeline.

4. 🎛️ Helm Chart
Create a Helm chart to deploy your service.
Helm chart must include:
Deployment
Service
Configurable values (e.g., image tag, port)
README explaining the chart usage
Deliverables:
Folder: helm/currency-converter/ with chart structure.

5. ☁️ Infrastructure with Terraform
Use Terraform to provision the infrastructure.
Choose AWS, GCP, or Azure (depending on experience).
The script must:
Create a managed Kubernetes cluster (e.g., EKS/GKE/AKS).
Configure necessary IAM roles and permissions.
Deploy Helm chart after provisioning.
Deliverables:
terraform/ directory containing main.tf, variables.tf, and outputs.tf.
Clear separation between infrastructure and application deployment logic.


==============================================================================================================================================================
                                                                Resolving Steps
==============================================================================================================================================================                                                                

## 🔧 Steps Followed in This Project

### 1. ✅ Developed Currency Converter Microservice
- Built a microservice using **FastAPI** with:
  - `/` route rendering a UI with currency dropdowns
  - `/convert` route fetching live exchange rates via API
- Used [ExchangeRate-API](https://www.exchangerate-api.com/) with API Token for better way to follow security.


### 2. ✅ Designed Minimal Web UI
- Created `templates/index.html` using **Jinja2**
- Inputs: `from_currency`, `to_currency`, and `amount`
- Displayed converted result on the same page

  <img width="570" alt="curconapp" src="https://github.com/user-attachments/assets/efcfcac8-66ce-40d2-a39f-99439ef58d49" />


### 3. ✅ Dockerized the Application
- Created a `Dockerfile` with `python:3.10-slim` as base image
- Installed dependencies from `requirements.txt`
- Used `uvicorn` to run the FastAPI app inside the container
- Built and tested locally with:
  ```bash
  docker build -t currency-final .
  docker run -p 8000:8000 currency-final

  <img width="1243" alt="docker container currency" src="https://github.com/user-attachments/assets/063c4284-b4c9-4347-93ce-2a507a537ea4" />

  
**4.** ✅ Pushed Docker Image to Docker Hub
Tagged the local image:
docker tag currency-final asr5454/currencyconverter:latest
Pushed to Docker Hub:
docker push asr5454/currencyconverter:latest

<img width="1302" alt="Dockerhub" src="https://github.com/user-attachments/assets/740dcbac-e0f9-41cd-a6c7-7f6e1fd2f5fd" />


**5.** ✅ Created Helm Chart for Kubernetes Deployment
Created folder: helm/currency-converter/
Added:
Chart.yaml
values.yaml with image name + port
Templates: deployment.yaml, service.yaml
Deployed to cluster using:
helm install currency-converter ./helm/currency-converter

-----------------------------------------------------------
asrprasad@ASRs-MacBook-Pro currencyconverter % helm install currency-converter ./helm/currency-converter

NAME: currency-converter
LAST DEPLOYED: Sun Jun 29 15:51:04 2025
NAMESPACE: default
STATUS: deployed
REVISION: 1
TEST SUITE: None
asrprasad@ASRs-MacBook-Pro currencyconverter % kubectl get pods
NAME                                  READY   STATUS              RESTARTS   AGE
currency-converter-6dbf8cb59f-bc467   0/1     ContainerCreating   0          4s
asrprasad@ASRs-MacBook-Pro currencyconverter % kubectl get pods
NAME                                  READY   STATUS              RESTARTS   AGE
currency-converter-6dbf8cb59f-bc467   0/1     ContainerCreating   0          14s
asrprasad@ASRs-MacBook-Pro currencyconverter % kubectl get pods
NAME                                  READY   STATUS    RESTARTS   AGE
currency-converter-6dbf8cb59f-bc467   1/1     Running   0          50s
asrprasad@ASRs-MacBook-Pro currencyconverter % kubectl logs currency-converter-6dbf8cb59f-bc467
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
-------------------------------------------------------------



**6.** ✅ Exposed App via Port Forwarding
Verified pod status:
kubectl get pods
Forwarded service port:
kubectl port-forward svc/currency-converter 8000:80

Opened app in browser: http://localhost:8000 ----I implemented as it will be in used only when port forwarding command executes. Once exit the port forwarding command the application will be not accessible.
