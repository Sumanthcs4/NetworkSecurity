
# Network Security Analysis with Machine Learning

[![CI/CD](https://github.com/Sumanthcs4/NetworkSecurity/actions/workflows/workflow.yml/badge.svg)](https://github.com/Sumanthcs4/NetworkSecurity/actions/workflows/workflow.yml)

## Project Overview

This project focuses on analyzing and improving network security using machine learning techniques. It includes a complete pipeline that covers data ingestion from a MongoDB database, data validation, data transformation, model training, evaluation, and deployment using Docker and AWS. The project leverages DAGsHub for MLOps, providing experiment tracking, model versioning, and data versioning.

The machine learning model used in this project is a **Random Forest Classifier**, which has demonstrated high performance in classifying network traffic as benign or malicious based on various network features.

## Project Architecture

The following diagram illustrates the overall architecture of the project:

```mermaid
graph TD
    subgraph "Data Ingestion"
        A[MongoDB Database] --> B(Data Ingestion Component);
        B --> C{Train/Test Split};
    end
    subgraph "Data Validation"
        C --> D(Data Validation Component);
        D --> E{Validation Checks};
        E -- Pass --> F[Data Validation Artifact];
        E -- Fail --> G[Validation Error];
    end
    subgraph "Data Transformation"
        F --> H(Data Transformation Component);
        H --> I[KNN Imputer];
        I --> J[Transformed Data Artifact];
    end
    subgraph "Model Training"
        J --> K(Model Trainer Component);
        K --> L[Random Forest Model];
        K --> M[Model Trainer Artifact];
    end
    subgraph "Model Evaluation"
        M --> N(Model Evaluation Component);
        N --> O{Performance Metrics};
    end
    subgraph "Deployment"
        O -- Pass Threshold --> P(Model Pusher Component);
        P --> Q[AWS S3];
        Q --> R[Docker Image in ECR];
        R --> S[FastAPI on EC2];
        O -- Fail Threshold --> T[Do Not Deploy];
    end

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#ccf,stroke:#333,stroke-width:2px
    style C fill:#ffccff,stroke:#333,stroke-width:2px
    style D fill:#ccf,stroke:#333,stroke-width:2px
    style E fill:#ffccff,stroke:#333,stroke-width:2px
    style F fill:#ccffcc,stroke:#333,stroke-width:2px
    style G fill:#f00,stroke:#333,stroke-width:2px
    style H fill:#ccf,stroke:#333,stroke-width:2px
    style I fill:#ccf,stroke:#333,stroke-width:2px
    style J fill:#ccffcc,stroke:#333,stroke-width:2px
    style K fill:#ccf,stroke:#333,stroke-width:2px
    style L fill:#f9f,stroke:#333,stroke-width:2px
    style M fill:#ccffcc,stroke:#333,stroke-width:2px
    style N fill:#ccf,stroke:#333,stroke-width:2px
    style O fill:#ffccff,stroke:#333,stroke-width:2px
    style P fill:#ccf,stroke:#333,stroke-width:2px
    style Q fill:#ccffcc,stroke:#333,stroke-width:2px
    style R fill:#ccffcc,stroke:#333,stroke-width:2px
    style S fill:#f9f,stroke:#333,stroke-width:2px
    style T fill:#ccc,stroke:#333,stroke-width:2px
```

## Detailed Stage Diagrams:

### Data Validation:
```mermaid
graph TD
    A[Data Ingestion Artifact] --> B(Data Validation Config);
    B --> C{Initiate Data Validation};
    C --> D[Read Data: train.csv, test.csv];
    D --> E{Schema Check};
    D --> F{Validate Number of Columns};
    D --> G{Is Numerical Columns Exist};
    D --> H{Data Drift Check}
    E -- Status: False --> M[Validation Error];
    F -- Status: False --> M;
    G -- Status: False --> M;
    H -- Status: False --> M;
    E -- Status: True --> I{Detect Dataset Drift};
    F -- Status: True --> I;
    G -- Status: True --> I;
    H -- Status: True --> I;
    I --> J[Data Validation Artifact];
    style M fill:#f00,stroke:#333,stroke-width:2px
```

### Data Transformation:
```mermaid
graph TD
    A[Data Validation Artifact] --> B(Data Transformation Config);
    B --> C{Initiate Data Transformation};
    C --> D[Read Data: train.csv, test.csv];
    D --> E[Training Dataframe: Drop Target Column];
    E --> F[Testing Dataframe: Drop Target Column];
    F --> G{Target Variable Mapping: -1 to 0};
    G --> H[Get Data Transformer Object: KNNImputer];
    H --> I[Fit preprocessor object on training data];
    I --> J[Transform training and testing data];
    J --> K[Create train and test array];
    K --> L[Save train.npy and test.npy];
    L --> M[Save preprocessor object: preprocessing.pkl];
    M --> N[Data Transformation Artifact];
```

### Model Training:
```mermaid
graph TD
    A[Data Transformation Artifact] --> B(Model Trainer Config);
    B --> C{Initiate Model Trainer};
    C --> D[Load train.npy and test.npy];
    D --> E[Split into X_train, y_train, X_test, y_test];
    E --> F{Train Model};
    F --> G[Evaluate Models using evaluate_models function];
    G --> H{Find best model and best score};
    H --> I[Predict on training data];
    I --> J[Calculate training metrics];
    J --> K[Predict on testing data];
    K --> L[Calculate testing metrics];
    L --> M[Log metrics and model to MLflow];
    M --> N[Save NetworkModel object];
    N --> O[Save best model to final_model/model.pkl];
    O --> P[Model Trainer Artifact];
```

### Deployment:
```mermaid
graph TD
    A[Push to Main Branch] --> B{GitHub Actions Trigger};
    B --> C[CI: Linting, Unit Tests];
    C --> D{CD: Build & Push Docker Image};
    D --> E[Configure AWS Credentials];
    E --> F[Login to ECR];
    F --> G[Build, Tag, Push Image to ECR];
    G --> H{CD: Deploy to EC2 (Self-Hosted Runner)};
    H --> I[Configure AWS Credentials];
    I --> J[Login to ECR];
    J --> K[Pull Latest Image];
    K --> L[Stop & Remove Existing Container];
    L --> M[Run New Container: map port 8080, set env vars];
    M --> N[Clean Old Images & Containers];
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
- **Data Ingestion:** Automated data ingestion from a MongoDB database with train-test split.
- **Data Validation:** Comprehensive data validation checks, including schema validation, column number validation, numerical column existence check, datatype check, and data drift detection using the evidently library.
- **Data Transformation:** Data preprocessing using a KNNImputer to handle missing values and target variable mapping.
- **Model Training:** Training and evaluation of a Random Forest Classifier.
- **Experiment Tracking:** Integration with MLflow (via DAGsHub) to track experiments, log metrics (F1-score, precision, recall), and log the trained model.
- **Model Deployment:** Dockerized application deployed on AWS EC2 using a self-hosted GitHub Actions runner.
- **CI/CD:** Automated CI/CD pipeline using GitHub Actions for linting, testing, building, pushing the Docker image to Amazon ECR, and deploying to EC2.
- **Artifact Storage:** Stores artifacts (datasets, preprocessor, trained model) in an AWS S3 bucket.
- **Web API:** REST API built with FastAPI to serve predictions.

## Dataset
The dataset used in this project is stored in a MongoDB database. The schema of the data is defined in `data_schema/schema.yaml`. The dataset contains the following features (all numeric):

```yaml
columns:
  - having_IPhaving_IP_Address: numeric
  - URLURL_Length: numeric
  - Shortining_Service: numeric
  - having_At_Symbol: numeric
  - double_slash_redirecting: numeric
  - Prefix_Suffix: numeric
  - having_Sub_Domain: numeric
  - SSLfinal_State: numeric
  - Domain_registeration_length: numeric
  - Favicon: numeric
  - port: numeric
  - HTTPS_token: numeric
  - Request_URL: numeric
  - URL_of_Anchor: numeric
  - Links_in_tags: numeric
  - SFH: numeric
  - Submitting_to_email: numeric
  - Abnormal_URL: numeric
  - Redirect: numeric
  - on_mouseover: numeric
  - RightClick: numeric
  - popUpWidnow: numeric
  - Iframe: numeric
  - age_of_domain: numeric
  - DNSRecord: numeric
  - web_traffic: numeric
  - Page_Rank: numeric
  - Google_Index: numeric
  - Links_pointing_to_page: numeric
  - Statistical_report: numeric
  - Result: numeric

target_column: Result
```

## AWS Deployment

The project is deployed on AWS EC2 using a self-hosted GitHub Actions runner. The CI/CD pipeline automates the following steps:

1.  **Continuous Integration:**
    *   Performs linting on the codebase (currently a placeholder in the workflow).
    *   Executes unit tests (currently a placeholder in the workflow).

2.  **Continuous Delivery:**
    *   Builds a Docker image containing the application and its dependencies.
    *   Pushes the newly built Docker image to Amazon Elastic Container Registry (ECR).

3.  **Continuous Deployment:**
    *   Connects to the EC2 instance (where the self-hosted GitHub Actions runner is configured).
    *   Pulls the latest Docker image from the ECR repository.
    *   Stops and removes any previously running Docker container named `networksecurity`.
    *   Starts a new Docker container based on the pulled image, with the following configurations:
        *   Names the container `networksecurity`.
        *   Maps port 8080 on the EC2 instance to port 8080 inside the container, making the FastAPI application accessible.
        *   Sets environment variables within the container to provide the application with necessary configurations like AWS credentials and the MongoDB connection string. These are sourced securely from GitHub Actions secrets.
        *   Utilizes the host's inter-process communication (IPC) namespace (`--ipc="host"`).
    *   Cleans up any old, unused Docker images and containers from the EC2 instance to free up space.

**Deployment Diagram:**

```mermaid
graph TD
    A[Push to Main Branch] --> B{GitHub Actions Trigger};
    B --> C[CI: Linting, Unit Tests];
    C --> D{CD: Build & Push Docker Image};
    D --> E[Configure AWS Credentials];
    E --> F[Login to ECR];
    F --> G[Build, Tag, Push Image to ECR];
    G --> H{CD: Deploy to EC2 (Self-Hosted Runner)};
    H --> I[Configure AWS Credentials];
    I --> J[Login to ECR];
    J --> K[Pull Latest Image];
    K --> L[Stop & Remove Existing Container];
    L --> M[Run New Container: map port 8080, set env vars];
    M --> N[Clean Old Images & Containers];
```

