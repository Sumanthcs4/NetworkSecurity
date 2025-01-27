### Network Security project for Phishing data

# **Phishing Detection Using Machine Learning**

This project aims to detect phishing websites based on various features using machine learning. The dataset contains characteristics of websites, which can be used to classify them as phishing or legitimate. By training a machine learning model on this dataset, we can predict whether a website is malicious.

The project incorporates several modern tools and practices, such as data pipelines, version control with DVC, model tracking with MLflow, and deployment using AWS and Flask.

---

## **Table of Contents**
- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## **Overview**

Phishing websites are designed to trick users into entering sensitive information like usernames, passwords, and credit card numbers. This project uses a phishing dataset with 31 features such as URL length, presence of IP addresses, domain age, and more. The goal is to use machine learning techniques to classify websites as either phishing or legitimate.

The project uses:
- **MongoDB** for data storage and pipelines.
- **MLflow** for tracking experiments and model performance.
- **DVC** for version control.
- **GitHub workflows** for CI/CD.
- **AWS EC2** for deploying the Flask API.
- **AWS S3** for storage.

---

## **Features**

- **Feature 1**: Predict if a website is phishing based on URL characteristics.
- **Feature 2**: Classify websites using machine learning algorithms.
- **Feature 3**: Data preprocessing and feature selection for improved model performance.
- **Feature 4**: Model evaluation using accuracy, precision, recall, and F1-score.
- **Feature 5**: End-to-end pipeline using MongoDB, DVC, and GitHub workflows for CI/CD.
- **Feature 6**: Deployment of model predictions using Flask API hosted on AWS EC2.

---

## **Technologies Used**

- **Programming Languages**: Python
- **Libraries**: Pandas, NumPy, scikit-learn, Matplotlib, Flask
- **Tools**: DVC, MLflow, GitHub Actions, Docker
- **Cloud Services**: AWS S3 (storage), AWS EC2 (deployment)
- **Database**: MongoDB
- **Deployment**: Flask API

---

## **Installation**

To get the project up and running locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/phishing-detection.git
