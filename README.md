# Network Security using Phishing Data



[![CI/CD](https://github.com/Sumanthcs4/NetworkSecurity/actions/workflows/main.yml/badge.svg)](https://github.com/Sumanthcs4/NetworkSecurity/actions/workflows/main.yml)


## Project Overview

This project focuses on analyzing and improving network security using machine learning techniques. It includes a complete pipeline that covers data ingestion from a MongoDB database, data validation, data transformation, model training, evaluation, and deployment using Docker and AWS. The project leverages DAGsHub for MLOps, providing experiment tracking, model versioning, and data versioning.

The machine learning model used in this project is a **Random Forest Classifier**, which has demonstrated high performance in classifying network traffic as benign or malicious based on various network features.

## Project Architecture

```mermaid
graph TD
    subgraph "Data Ingestion"
        A[MongoDB Database] --> B(Data Ingestion Component)
        B --> C{Train/Test Split}
    end
    
    subgraph "Data Validation"
        C --> D(Data Validation Component)
        D --> E{Validation Checks}
        E -- Pass --> F[Data Validation Artifact]
        E -- Fail --> G[Validation Error]
    end
    
    subgraph "Data Transformation"
        F --> H(Data Transformation Component)
        H --> I[KNN Imputer]
        I --> J[Transformed Data Artifact]
    end
    
    subgraph "Model Training"
        J --> K(Model Trainer Component)
        K --> L[Random Forest Model]
        K --> M[Model Trainer Artifact]
    end
    
    subgraph "Model Evaluation"
        M --> N(Model Evaluation Component)
        N --> O{Performance Metrics}
    end
    
    subgraph "Deployment"
        O -- Pass Threshold --> P(Model Pusher Component)
        P --> Q[AWS S3]
        Q --> R[Docker Image in ECR]
        R --> S[FastAPI on EC2]
        O -- Fail Threshold --> T[Do Not Deploy]
    end
    
    classDef primary fill:#4285f4,stroke:#333,stroke-width:2px,color:white
    classDef secondary fill:#34a853,stroke:#333,stroke-width:2px,color:white
    classDef warning fill:#fbbc05,stroke:#333,stroke-width:2px,color:black
    classDef error fill:#ea4335,stroke:#333,stroke-width:2px,color:white
    classDef success fill:#00c851,stroke:#333,stroke-width:2px,color:white
    
    class A,B,D,H,K,N,P primary
    class F,J,M,Q,R success
    class C,E,O warning
    class G,T error
    class I,L,S secondary
```

## Deployment Pipeline

```mermaid
graph TD
    A[Push to Main Branch] --> B[GitHub Actions Trigger]
    B --> C[CI: Linting & Unit Tests]
    C --> D[Build Docker Image]
    D --> E[Configure AWS]
    E --> F[Push to ECR]
    F --> G[Deploy to EC2]
    G --> H[Start Container]
    H --> I[Cleanup]

    classDef primary fill:#4285f4,stroke:#333,stroke-width:2px,color:white
    classDef secondary fill:#34a853,stroke:#333,stroke-width:2px,color:white
    classDef process fill:#fbbc05,stroke:#333,stroke-width:2px,color:black

    class A,E primary
    class B,C,D,F process
    class G,H,I secondary
```

## Technologies Used

- **Programming Language:** Python 3.10
- **Machine Learning:** scikit-learn (RandomForestClassifier, KNNImputer), pandas, numpy
- **Data Storage:** MongoDB Atlas (for raw data), AWS S3 (for artifacts and model)
- **MLOps:** DAGsHub, MLflow
- **Deployment:** Docker, AWS EC2, GitHub Actions
- **Web Framework:** FastAPI, Uvicorn
- **Data Validation:** Evidently
- **Other Tools:** awscli

## Features

- **Data Ingestion:** Automated data ingestion from MongoDB with train-test split
- **Data Validation:** Comprehensive validation including schema, column, and drift detection
- **Data Transformation:** KNNImputer for missing values and target variable mapping
- **Model Training:** Random Forest Classifier with automated evaluation
- **Experiment Tracking:** MLflow integration via DAGsHub
- **Model Deployment:** Dockerized application on AWS EC2
- **CI/CD:** Automated pipeline using GitHub Actions
- **Artifact Storage:** AWS S3 bucket integration
- **Web API:** FastAPI-based REST API for predictions

## Dataset

The dataset contains various network security features stored in MongoDB. Key features include:
- IP address characteristics
- URL properties
- Domain information
- SSL/HTTPS metrics
- Traffic patterns
- Security indicators

## Setup Instructions

1. **Clone the Repository:**
```bash
git clone https://github.com/Sumanthcs4/NetworkSecurity.git
cd NetworkSecurity
```

2. **Set up Virtual Environment:**
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. **Install Dependencies:**
```bash
pip install -r requirements.txt
```

4. **Configure Environment Variables:**
Create a `.env` file with:
```
MONGO_DB_URL=your_mongodb_url
AWS_ACCESS_KEY_ID=your_aws_key
AWS_SECRET_ACCESS_KEY=your_aws_secret
AWS_REGION=your_region
TRAINING_BUCKET_NAME=your_bucket
ECR_REPOSITORY_NAME=your_repo
AWS_ECR_LOGIN_URI=your_uri
```

5. **Run the Project:**
```bash
# Run Pipeline
python src/pipeline/training_pipeline.py

# Run API
uvicorn app:app --reload --port 8080
```

## Docker Usage

```bash
# Build
docker build -t networksecurity:latest .

# Run
docker run -p 8080:8080 \
  --name networksecurity \
  -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
  -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY \
  -e AWS_REGION=$AWS_REGION \
  -e TRAINING_BUCKET_NAME=$TRAINING_BUCKET_NAME \
  -e MONGO_DB_URL=$MONGO_DB_URL \
  networksecurity:latest
```

## Project Structure

```
NetworkSecurity/
├── .github/                  # GitHub Actions workflows
├── app.py                   # FastAPI application
├── Artifacts/               # Generated artifacts
├── data_schema/             # Schema definition
├── notebook/                # Jupyter notebooks
├── requirements.txt         # Dependencies
├── src/                     # Source code
│   ├── components/          # Pipeline components
│   ├── config/             # Configurations
│   ├── constant/           # Constants
│   ├── entity/             # Entity definitions
│   ├── exception/          # Custom exceptions
│   ├── logging/            # Logging setup
│   ├── pipeline/           # Pipeline definition
│   └── utils/              # Utilities
├── template.index          # HTML template
├── Dockerfile              # Docker configuration
└── setup.py                # Package setup
```

## Contributing

Please read `CONTRIBUTING.md` for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
