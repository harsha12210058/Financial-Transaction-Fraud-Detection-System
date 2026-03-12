# Financial-Transaction-Fraud-Detection-System
Machine Learning | Fraud Detection | Streamlit Deployment

A machine learning system designed to detect fraudulent financial transactions using transactional and behavioral features.
The project includes data analysis, feature engineering, model training, evaluation, and deployment using Streamlit for real-time fraud prediction.

Live Demo

Streamlit Web Application

https://financial-transaction-fraud-detection-system.streamlit.app/

Users can input transaction details and instantly check whether the transaction is fraudulent.
Problem Statement

Financial fraud is one of the biggest challenges in digital banking and online payment systems. Fraudulent transactions cause billions of dollars in losses annually.

This project aims to build a machine learning model capable of identifying suspicious transactions based on transaction behavior and financial patterns.

The system analyzes factors such as:

Transaction type

Transaction amount

Sender balance

Receiver balance

Transaction timing

Dataset

The dataset contains financial transaction records with the following attributes:

Feature	Description
type	Transaction type
amount	Transaction amount
oldbalanceOrg	Sender balance before transaction
newbalanceOrig	Sender balance after transaction
oldbalanceDest	Receiver balance before transaction
newbalanceDest	Receiver balance after transaction
isFraud	Fraud label

The dataset is highly imbalanced, where fraudulent transactions represent a very small percentage of total transactions.

Exploratory Data Analysis (EDA)

EDA was performed to understand transaction behavior and fraud patterns.

Fraud Transactions by Type

Upload screenshot here:

images/fraud_by_type.png

(Use your notebook graph showing fraud transactions by type)

Feature Engineering

Several additional features were created to improve fraud detection performance.

Engineered features include:

origin_balance_error

destination_balance_error

amount_balance_ratio

account_emptied

receiver_balance_jump

large_transaction

risk_score

These features capture abnormal transaction patterns commonly seen in fraudulent activity.

Handling Imbalanced Data

Fraud datasets are typically highly imbalanced.

To address this problem:

SMOTE (Synthetic Minority Oversampling Technique) was applied to balance the dataset.

This improves the model's ability to detect fraud cases.

Machine Learning Models

Three models were trained and compared:

Logistic Regression

Random Forest

XGBoost

Evaluation metrics used:

Precision

Recall

F1 Score

ROC-AUC Score

Model Performance

After comparing all models:

Random Forest achieved the best performance and was selected as the final model.

Example evaluation metrics:

Model	ROC-AUC
Logistic Regression	~0.99
Random Forest	~0.999
XGBoost	~0.999

Upload screenshot here:

images/model_comparison.png

(Your model comparison table screenshot)

Confusion Matrix

Upload screenshot here:

images/confusion_matrix.png

This visualization shows how well the model distinguishes between:

Legitimate transactions

Fraudulent transactions

Precision-Recall Curve

Upload screenshot here:

images/precision_recall_curve.png

This curve is particularly important for imbalanced datasets like fraud detection.

Feature Importance

Feature importance analysis helps understand which variables contribute most to fraud detection.

Upload screenshot here:

images/feature_importance.png

Top contributing features include:

origin_balance_error

amount_balance_ratio

amount_exceeds_balance

newbalanceOrig

Model Explainability (SHAP)

SHAP values were used to explain the contribution of each feature toward fraud prediction.

Upload screenshot here:

images/shap_summary.png

This helps make the model more interpretable and transparent.

Web Application

The trained model was deployed using Streamlit to allow real-time fraud detection.

Users enter transaction details and receive immediate predictions.

Upload screenshot here:

images/streamlit_app.png

Example output:

Legitimate Transaction

Fraudulent Transaction Detected

Technology Stack

Python
Pandas
NumPy
Scikit-learn
XGBoost
Streamlit
Matplotlib
Seaborn
SHAP
Future Improvements

Possible improvements include:

Deep learning models for fraud detection

Real-time transaction streaming

Advanced anomaly detection techniques

Model monitoring and drift detection

API deployment for integration with banking systems

Author

Harsha Vardhan

Machine Learning | Data Science | Fraud Detection
