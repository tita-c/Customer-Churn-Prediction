# Customer Churn Prediction using Machine Learning

## Project Overview

Customer churn is a major challenge for subscription-based businesses because losing existing customers directly impacts revenue. The goal of this project is to build a machine learning model that can predict whether a customer is likely to leave a telecom service provider.

This project analyzes customer information such as demographics, service usage, contract details, and billing history to identify customers who have a higher probability of churning.

The project covers the complete machine learning workflow, including data preprocessing, exploratory data analysis, model development, evaluation, feature importance analysis, and deployment using Streamlit.

---

## Problem Statement

Businesses often have difficulty identifying customers who are at risk of leaving. By using machine learning, we can analyze customer behavior patterns and predict potential churn cases before they happen.

The objectives of this project are:

- Predict whether a customer is likely to churn.
- Identify important factors that influence customer churn.
- Provide insights that can help businesses design customer retention strategies.

---

## Technologies Used

### Programming Language
- Python

### Machine Learning
- Scikit-learn
- XGBoost

### Data Processing and Analysis
- Pandas
- NumPy

### Data Visualization
- Matplotlib
- Seaborn

### Deployment
- Streamlit

### Model Serialization
- Pickle

---

## Project Structure

```
Customer-Churn-Prediction

│
├── app.py
│   Streamlit application for customer churn prediction
│
├── data
│   └── customer_churn.csv
│
├── notebooks
│   └── churn_prediction.ipynb
│
├── churn_model.pkl
│   Trained machine learning model
│
├── scaler.pkl
│   Feature scaling object
│
├── feature_names.pkl
│   Saved feature information
│
├── requirements.txt
│
└── README.md
```

---

## Dataset

The project uses the IBM Telco Customer Churn dataset.

The dataset contains customer details including:

- Customer demographics
- Tenure
- Internet services
- Contract information
- Payment methods
- Monthly charges
- Total charges
- Churn status

The target variable is customer churn, where:

- 0 represents customers who stayed
- 1 represents customers who left

---

## Machine Learning Workflow

The project follows a complete machine learning pipeline:

1. Data loading and understanding
2. Data cleaning and preprocessing
3. Exploratory Data Analysis
4. Feature encoding
5. Train-test data splitting
6. Feature scaling
7. Model training
8. Model evaluation
9. Hyperparameter tuning
10. Model deployment

---

## Data Preprocessing

The following preprocessing steps were performed:

- Removed unnecessary features
- Converted categorical variables using one-hot encoding
- Converted churn labels into binary format
- Applied feature scaling
- Split the dataset into training and testing sets

---

## Models Implemented

Multiple machine learning algorithms were trained and evaluated.

### Logistic Regression

Used as a baseline classification model to establish initial performance.

Performance:

- Accuracy: 80%
- Churn F1-score: 0.61


### Random Forest Classifier

Used to capture non-linear relationships between customer features and churn behavior.


### Balanced Random Forest

Implemented class balancing techniques to improve detection of churn customers.


### Tuned Random Forest

Hyperparameter optimization was performed using GridSearchCV with cross-validation.

This model was selected as the final model because it provided better churn detection performance.

---

## Model Performance Comparison

| Model | Accuracy | Churn Recall | Churn F1-score |
|---|---|---|---|
| Logistic Regression | 80% | 57% | 0.61 |
| Random Forest | 79% | 51% | 0.56 |
| Balanced Random Forest | 77% | 66% | 0.61 |
| Tuned Random Forest | 75% | 79% | 0.63 |

Although the tuned model has slightly lower overall accuracy, it identifies a higher percentage of customers who are likely to churn, which is more valuable for customer retention purposes.

---

## Feature Importance Analysis

The final model identified the following features as the most influential factors affecting churn:

1. Tenure
2. Total Charges
3. Two-year Contract
4. Monthly Charges
5. Fiber Optic Internet Service
6. Electronic Check Payment Method
7. One-year Contract
8. Online Security
9. Technical Support

---

## Business Insights

The model results provide the following insights:

- Customers with shorter tenure have a higher probability of leaving.
- Long-term contracts reduce customer churn.
- Higher monthly charges can increase churn risk.
- Customers using additional services such as online security and technical support are more likely to remain customers.
- Payment methods and service plans can influence customer retention.

These insights can help businesses create targeted retention strategies.

---

## Deployment

A Streamlit web application was developed to allow users to enter customer information and receive churn predictions.

The application provides:

- Customer churn prediction
- Churn probability score
- Risk assessment based on model output

---

## How to Run the Project

Clone the repository:

```bash
git clone https://github.com/yourusername/Customer-Churn-Prediction.git
```

Navigate to the project folder:

```bash
cd Customer-Churn-Prediction
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Future Improvements

Possible improvements for this project:

- Implement SMOTE for better handling of class imbalance
- Add SHAP-based model explainability
- Deploy the application on cloud platforms
- Build an API using Flask or FastAPI
- Add automated customer retention recommendations
- Develop a real-time analytics dashboard

---

## Author

Tita
Student