# Customer Churn Prediction 📊
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red)
![ML](https://img.shields.io/badge/Machine%20Learning-Project-green)
![TensorFlow](https://img.shields.io/badge/DeepLearning-TensorFlow-orange?logo=tensorflow)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

Machine Learning project to predict **credit card customer churn** using customer demographic and banking data. 💳

---

## 📌 Project Overview

Customer churn is a major challenge for banks and various service providers. 🏦  
This project builds a machine learning model that predicts whether a customer is likely to leave the bank.

The model analyzes customer attributes such as:

- Age 👤  
- Geography 🌍  
- Credit Score 📊  
- Account Balance 💰  
- Tenure ⏳  
- Number of Products 🧾  
- Active Membership ✅  

The goal is to help businesses **identify high-risk customers and take retention actions**. 🎯

---

## 🚀 Live Demo

Try the deployed app here:

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live%20App-red?logo=streamlit)](https://customer-churn-prediction-pg2spsbjlksybbuyappw8hf.streamlit.app/)
## 📂 Project Structure

```
Customer-Churn-Prediction
│
├── app/                     # Streamlit web app 🌐
│
├── data/                    # Dataset 📊
│   └── raw/
│
├── models/                  # Saved trained models 🤖
│   ├── churn_prediction_model.h5
│   └── scaler.pkl
│
├── notebooks/               # Jupyter notebooks for analysis 📓
│   └── churn_analysis.ipynb
│
├── src/                     # Source code 💻
│
├── requirements.txt         # Project dependencies 📦
├── .gitignore
└── README.md
```

---

## 🛠️ Technologies Used

- Python 🐍  
- Pandas 🐼  
- NumPy 🔢  
- Scikit-learn 🤖  
- TensorFlow / Keras 🧠  
- Matplotlib 📈  
- Seaborn 🌊  
- Streamlit 🚀  

---

## ⚙️ Model Training Process

1. Data cleaning and preprocessing 🧹  
2. Exploratory Data Analysis (EDA) 🔎  
3. Data scaling using **StandardScaler** ⚖️  
4. Model training using a **Neural Network** 🧠  
5. Model evaluation 📊  
6. Model saving for deployment 💾  

---

## 📈 Model Performance

- **Accuracy:** ~85% (may vary depending on training)  
- **Task:** Binary classification (Churn vs Not Churn)

---

## 📊 Model Comparison

| Model | Accuracy |
|------|------|
| Logistic Regression | 82% |
| Random Forest | 85% |
| SVM | 86% |
| Neural Network | 86% |

Neural Network was selected as the training model. 🧠

---
## 📊 Dataset

This project uses the **Credit Card Customer Churn Dataset** which contains customer demographic and banking information used to predict churn behavior.

[![Kaggle Dataset](https://img.shields.io/badge/Dataset-Kaggle-blue?logo=kaggle)](https://www.kaggle.com/datasets/rjmanoj/credit-card-customer-churn-prediction)

---

## 📋 Dataset Preview

| CreditScore | Geography | Age | Balance | Tenure | NumOfProducts | IsActiveMember | Churn |
|-------------|-----------|-----|---------|--------|---------------|---------------|-------|
| 619 | France | 42 | 0.00 | 2 | 1 | 1 | 1 |
| 608 | Spain | 41 | 83807.86 | 1 | 1 | 1 | 0 |
| 502 | France | 42 | 159660.80 | 8 | 3 | 0 | 1 |

---

## 🧠 Machine Learning Pipeline

```
Data Collection
      ↓
Data Cleaning
      ↓
Exploratory Data Analysis
      ↓
Feature Scaling
      ↓
Model Training
      ↓
Model Evaluation
      ↓
Streamlit Deployment
```

---

## ▶️ How to Run the Project

### 1️⃣ Install dependencies 📦

```bash
pip install -r requirements.txt
```

### 2️⃣ Run the notebook 📓

Open and run:

```
notebooks/churn_analysis.ipynb
```

### 3️⃣ Run the Streamlit app 🚀

```bash
streamlit run app/app.py
```

---

## 🔮 Future Improvements

- Hyperparameter tuning ⚙️  
- Feature selection 🎯

---

## 👩‍💻 Author

**Ayushi Rai**
