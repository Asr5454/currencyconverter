**Assignment1:**
**Resolving Steps**                                                             

**Note:**

**All the respective files are available in the repository https://github.com/Asr5454/currencyconverter/tree/main**

**Also Terraform has not used as it requires the cloud platform to create an cluster. I have knowledge into TF and Please go through the files attached for main.tf , variable.tf and outputs.tf**

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

<img width="831" alt="usinghelm" src="https://github.com/user-attachments/assets/a1ac979a-077d-49ae-9bc6-a1c97a8c59be" />



----------------------------------------------------------------------

**6.** ✅ Exposed App via Port Forwarding
Verified pod status:
kubectl get pods
Forwarded service port:
kubectl port-forward svc/currency-converter 8000:80

<img width="731" alt="portforwarding" src="https://github.com/user-attachments/assets/6bfd6f52-8ae0-4674-8dd4-b8f3669a2639" />

**Verifying**
**Opened app in browser:** http://localhost:8000 ----I implemented as it will be in used only when port forwarding command executes. Once exit the port forwarding command the application will be not accessible.


**Tree Diagram**
├── currencyconverter
│   ├── Dockerfile
│   ├── helm
│   │   └── currency-converter
│   │       ├── Chart.yaml
│   │       ├── templates
│   │       │   ├── deployment.yaml
│   │       │   └── service.yaml
│   │       └── values.yaml
│   ├── main.py
│   ├── requirements.txt
│   ├── templates
│   │   └── index.html
│   └── terraform
│       ├── main.tf
│       ├── outputs.tf
│       └── variable.tf

