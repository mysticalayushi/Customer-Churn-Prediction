
# Customer Churn Prediction

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red)
![ML](https://img.shields.io/badge/Machine%20Learning-Project-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
Machine Learning project to predict **credit card customer churn** using customer demographic and banking data.

---

## Project Overview

Customer churn is a major challenge for banks and financial institutions.  
This project builds a machine learning model that predicts whether a customer is likely to leave the bank.

The model analyzes customer attributes such as:

- Age  
- Geography  
- Credit Score  
- Account Balance  
- Tenure  
- Number of Products  
- Active Membership  

The goal is to help businesses **identify high-risk customers and take retention actions**.

---

## Project Structure

```
Customer-Churn-Prediction
│
├── app/                     # Streamlit web app
│
├── data/                    # Dataset
│   └── raw/
│
├── models/                  # Saved trained models
│   ├── churn_prediction_model.h5
│   └── scaler.pkl
│
├── notebooks/               # Jupyter notebooks for analysis
│   └── churn_analysis.ipynb
│
├── src/                     # Source code
│
├── requirements.txt         # Project dependencies
├── .gitignore
└── README.md
```

---

## Technologies Used

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- TensorFlow / Keras  
- Matplotlib  
- Seaborn  
- Streamlit  

---

## Model Training Process

1. Data cleaning and preprocessing  
2. Exploratory Data Analysis (EDA)  
3. Feature engineering  
4. Data scaling using **StandardScaler**  
5. Model training using a **Neural Network**  
6. Model evaluation  
7. Model saving for deployment  

---

## Model Performance

- **Accuracy:** ~85% (may vary depending on training)  
- **Task:** Binary classification (Churn vs Not Churn)

---
## Model Comparison

| Model | Accuracy |
|------|------|
| Logistic Regression | 82% |
| Random Forest | 85% |
| SVM | 86% |
| Neural Network | 86% |

Random Forest performed the best in this experiment.

## How to Run the Project

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the notebook

Open and run:

```
notebooks/churn_analysis.ipynb
```

### 3. Run the Streamlit app

```bash
streamlit run app/app.py
```

---

## Dataset

Dataset used: **Credit Card Customer Churn dataset**

Features include demographic and account activity information.

---

## Future Improvements

- Hyperparameter tuning  
- Feature selection 

---

## Author

**AYUSHI RAI**


