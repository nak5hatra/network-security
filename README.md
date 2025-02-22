## Network Security Project for Phising Data

This project focuses on identifying and analyzing phishing attacks. The goal is to develop a system that can detect phishing attempts based on various parameters, such as URL analysis, website content, and other key indicators of fraudulent activity. By utilizing machine learning algorithms and advanced data analysis, the project aims to improve the detection rate and minimize false positives, providing better protection against phishing scams.

## Features
- FastApi for a simple and intuitive user interface.
- Deployed using AWS Elastic Container Registry and Continuous Deployment (CD) pipeline with GitHub.

## Technologies Used
- **Machine Learning:** Python, Scikit-learn
- **Backend:** Flask
- **Containerization:** Docker
- **Deployment:** AWS Elastic Container Registry (ECR)
- **Continuous Deployment:** GitHub Actions
- **Version Control:** GitHub

## Project Setup

### Prerequisites
Ensure you have the following installed on your local machine:
- Python 3.10
- Docker
- AWS CLI (configured with appropriate credentials)
- Git
- Fastapi

### Clone the Repository
```bash
git clone https://github.com/nak5hatra/network-security.git
```
### Install Dependencies
Create a virtual environment and install required dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run the  App Locally
To start the Flask application locally, run:
``` bash
python app.py
```
Access url in Browser: http://localhost:8000/docs
