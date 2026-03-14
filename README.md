# Customer Churn Prediction 📊

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-22C55E?style=for-the-badge)

<br/>

**An end-to-end machine learning system that predicts whether a bank customer will churn —  
built with Neural Networks and deployed as an interactive Streamlit web application.**

</div>

---

## 📌 Project Overview

Customer churn costs banks millions annually. Identifying at-risk customers **before** they leave allows businesses to take targeted retention actions — saving revenue and improving customer relationships 🎯

This project answers the question:

> **"Given a customer's demographic and banking profile, how likely are they to leave?"**

---

## 🚀 Live Demo

<div align="center">

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live%20App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://customer-churn-prediction-pg2spsbjlksybbuyappw8hf.streamlit.app/)
[![Notebook](https://img.shields.io/badge/Notebook-View%20Analysis-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](notebooks/churn_analysis.ipynb)
[![Dataset](https://img.shields.io/badge/Dataset-Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/datasets/rjmanoj/credit-card-customer-churn-prediction)

</div>

---

## 🖼️ App Preview

<p align="center">
  <img src="app_preview1.png" width="45%" alt="Customer likely to stay"/>
  &nbsp;&nbsp;
  <img src="app_preview2.png" width="45%" alt="Customer likely to churn"/>
</p>
<p align="center">
  <em>Left: Customer predicted to stay &nbsp;|&nbsp; Right: Customer predicted to churn</em>
</p>

<p align="center">
  <img src="app_preview3.png" width="45%" alt="App view 3"/>
  &nbsp;&nbsp;
  <img src="app_preview4.png" width="45%" alt="App view 4"/>
</p>

---

## 📂 Project Structure

```
Customer-Churn-Prediction/
│
├── app/                          # Streamlit web application
│   └── app.py
│
├── data/
│   └── raw/                      # Raw dataset
│
├── models/
│   ├── churn_prediction_model.h5 # Trained Neural Network
│   └── scaler.pkl                # Fitted StandardScaler
│
├── notebooks/
│   └── churn_analysis.ipynb      # EDA + Model training notebook
│
├── src/                          # Modular source code
├── requirements.txt
└── README.md
```

---

## 🛠️ Tech Stack

<div align="center">

| Category | Tools |
|---|---|
| **Language** | Python 3.11 |
| **Deep Learning** | TensorFlow, Keras |
| **ML & Data** | Scikit-learn, Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn |
| **Deployment** | Streamlit |

</div>

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

<div align="center">

| Model | Accuracy |
|---|---|
| Logistic Regression | 82% |
| Random Forest | 85% |
| SVM | 86% |
| ✅ **Neural Network** | **86%** |

</div>

> **Neural Network (TensorFlow/Keras)** was selected as the final model for deployment due to its performance and scalability.

---

## 🧠 ML Pipeline

```
Raw Data  →  Cleaning  →  EDA  →  Feature Scaling  →  Model Training  →  Evaluation  →  Deployment
```

---

### Features Used for Prediction

<div align="center">

| Feature | Description |
|---|---|
| `CreditScore` | Customer's credit score |
| `Age` | Customer's age |
| `Balance` | Account balance |
| `Tenure` | Years as a customer |
| `NumOfProducts` | Number of bank products held |
| `IsActiveMember` | Whether the customer is active |

</div>

---

## ▶️ Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/mysticalayushi/Customer-Churn-Prediction.git
cd Customer-Churn-Prediction

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the Streamlit app
streamlit run app/app.py
```

Or explore the analysis notebook:
```bash
jupyter notebook notebooks/churn_analysis.ipynb
```

---

## 🔮 Future Improvements

- [ ] Hyperparameter tuning with Optuna
- [ ] Feature importance visualization (SHAP values)
- [ ] Add SMOTE for handling class imbalance
- [ ] REST API with FastAPI for model serving

---

## 👩‍💻 Author

<div align="center">

**Ayushi Rai**  
[![GitHub](https://img.shields.io/badge/GitHub-mysticalayushi-181717?style=flat&logo=github)](https://github.com/mysticalayushi)

</div>

---

<div align="center">
<sub>If you found this project helpful, consider giving it a ⭐ on GitHub!</sub>
</div>
