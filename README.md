# Network Security Project

A **Machine Learning** project for network security analysis, leveraging **Docker**, **AWS (S3 & EC2)**, and **DAGsHub** for MLOps. This project includes automated workflows, data ingestion, model training, and deployment pipelines.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
  - [Clone the Repository](#1-clone-the-repository)
  - [Setup Environment](#2-setup-environment)
  - [Run the Project](#3-run-the-project)
- [Docker Integration](#docker-integration)
- [AWS Deployment](#aws-deployment)
  - [S3 Integration](#s3-integration)
  - [EC2 Deployment](#ec2-deployment)
- [Logging and Tracking](#logging-and-tracking)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

---

## Project Overview
This project analyzes and improves network security using machine learning techniques. It includes data ingestion, validation, transformation, model training, and evaluation. The results are tracked and logged using **MLflow** on **DAGsHub**.

## Technologies Used
- **Programming Language:** Python 3.8+
- **Machine Learning:** scikit-learn, pandas, numpy
- **MLOps Tools:** DAGsHub, MLflow
- **Deployment:** Docker, AWS (S3 & EC2)
- **Orchestration:** GitHub Actions
- **Logging:** Python Logging
- **Database:** MongoDB Atlas

## Features
- **Data Ingestion:** Automated data ingestion pipeline with train-test split.
- **Data Validation:** Ensures data integrity (e.g., column count and schema).
- **Data Transformation:** Implements preprocessing steps using `KNNImputer`.
- **Model Training:** Trains classification models and evaluates metrics.
- **Artifact Storage:** Stores artifacts (e.g., models and datasets) in S3.
- **Tracking:** Logs metrics and artifacts to MLflow via DAGsHub.
- **Deployment:** Dockerized application deployed on AWS EC2.

## Project Structure
```
networksecurity/
├── networksecurity/      # Source code for the project
├── artifacts/            # Generated artifacts (models, data splits, etc.)
├── docker/               # Docker configuration files
├── configs/              # Configuration files for the pipeline
├── app.py                # To run the app
├── .github/              # GitHub Actions for CI/CD
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies
```

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Sumanthcs4/NetworkSecurity.git
cd NetworkSecurity
```

### 2. Setup Environment
- Install dependencies using `requirements.txt`:
  ```bash
  pip install -r requirements.txt
  ```
- Configure environment variables in a `.env` file:
  ```env
  MONGO_DB_URL="mongodb+srv://<username>:<password>@cluster0.sszo2.mongodb.net/?retryWrites=true&w=majority"
  AWS_ACCESS_KEY_ID="<your-access-key>"
  AWS_SECRET_ACCESS_KEY="<your-secret-key>"
  S3_BUCKET_NAME="<your-s3-bucket>"
  ```

### 3. Run the Project
To start the project, execute the following command:
```bash
python app.py
```

---

## Docker Integration
This project is containerized using Docker.

### Steps to Run with Docker:
1. Build the Docker image:
   ```bash
   docker build -t networksecurity:latest .
   ```
2. Run the Docker container:
   ```bash
   docker run -p 5000:5000 --env-file .env networksecurity:latest
   ```

---

## AWS Deployment

### S3 Integration
- Artifacts (e.g., trained models, data splits) are automatically uploaded to an S3 bucket.
- Configuration for S3 is managed via environment variables.

### EC2 Deployment
- The project is deployed on an AWS EC2 instance with Docker.
- Steps to deploy:
  1. SSH into your EC2 instance:
     ```bash
     ssh -i "your-key.pem" ec2-user@your-ec2-instance
     ```
  2. Clone the repository and navigate to the directory.
  3. Build and run the Docker container as shown above.

---

## Logging and Tracking
- **MLflow:** Tracks metrics, parameters, and artifacts.
- **DAGsHub:** Integrates MLflow tracking and repository management.

Logs Example:
```
[ 2025-01-27 11:06:02,293 ] INFO - HTTP Request: GET https://dagshub.com/api/v1/user "HTTP/1.1 200 OK"
[ 2025-01-27 11:06:19,907 ] INFO - Data Ingestion completed and artifact saved.
[ 2025-01-27 11:11:25,517 ] INFO - Model trainer artifact: ModelTrainerArtifact(...)
```

---

## Future Enhancements
- Implement additional machine learning algorithms.
- Add a web-based user interface.
- Automate hyperparameter tuning.
- Enhance logging and error handling.

---

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

