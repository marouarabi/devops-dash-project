# DevOps System Monitoring Dashboard

## Project Overview

This project is a **DevOps-based system monitoring dashboard** developed as part of a **Cloud & DevOps course**.

The application provides **real-time monitoring of system resources**, including:

- CPU usage
- Memory usage
- Disk usage
- System information

The dashboard is built with **Python Dash** and will later be deployed using a complete **DevOps pipeline**.

---

# Technologies Used

- Python
- Dash
- Plotly
- Docker
- Terraform
- Ansible
- Kubernetes
- Jenkins
- AWS

---

# Project Structure


devops-dash-project/

│
├── app/
│ ├── app.py
│ ├── metrics.py
│ ├── requirements.txt
│ └── assets/
│ └── style.css
│
├── docker/
├── terraform/
├── ansible/
├── k8s/
├── jenkins/
│
├── rapport-devops/
│
├── README.md
└── .gitignore


---

# Run the Application Locally

## 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/devops-dash-project.git
cd devops-dash-project
2. Create a virtual environment
cd app
py -3.11 -m venv venv
3. Activate the environment
Windows
venv\Scripts\activate
4. Install dependencies
pip install -r requirements.txt
5. Run the dashboard
python app.py
6. Open the dashboard in your browser
http://localhost:8050
Dashboard Features

Real-time CPU monitoring

Memory usage tracking

Disk usage monitoring

System information display

Historical metrics visualization

Automatic refresh every few seconds

DevOps Pipeline (Next Steps)

The project will implement the following DevOps stages:

Application development with Python Dash

Containerization with Docker

Infrastructure provisioning using Terraform

Configuration management with Ansible

Deployment using Kubernetes

CI/CD pipeline with Jenkins

Cloud deployment on AWS

Authors

DevOps Project – Cloud & DevOps Course

Team Members:

RABI Maroua

ELKHATIB Sara

OUCHIDA Iliass