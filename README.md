# Customer Churn Prediction 📊

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Accuracy](https://img.shields.io/badge/Accuracy-~80%25-22C55E?style=for-the-badge)
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
## 📚 Table of Contents

<ul>
  <li><a href="#-project-overview">📌 Project Overview</a></li>
  <li><a href="#-live-demo">🚀 Live Demo</a></li>
  <li><a href="#-project-structure">📂 Project Structure</a></li>
  <li><a href="#️-tech-stack">🛠️ Tech Stack</a></li>
  <li><a href="#-dataset-description">📊 Dataset Description</a></li>
  <li><a href="#-key-insights-from-eda">📈 Key Insights from EDA</a></li>
  <li><a href="#️-data-preprocessing">⚙️ Data Preprocessing</a></li>
  <li><a href="#-model-training--performance">🤖 Model Training & Performance</a></li>
  <li><a href="#-neural-network-architecture">🧠 Neural Network Architecture</a></li>
  <li><a href="#-inference-pipeline">🔮 Inference Pipeline</a></li>
  <li><a href="#-application-features">🚀 Application Features</a></li>
  <li><a href="#️-run-locally">▶️ Run Locally</a></li>
  <li><a href="#-business-recommendations">💡 Business Recommendations</a></li>
  <li><a href="#-future-improvements">🔭 Future Improvements</a></li>
  <li><a href="#-author">👩‍💻 Author</a></li>
</ul>
  ----
  
## 🚀 Live Demo

<div align="center">

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live%20App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://customer-churn-prediction-pg2spsbjlksybbuyappw8hf.streamlit.app/)
[![Notebook](https://img.shields.io/badge/Notebook-View%20Analysis-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](notebooks/churn_analysis.ipynb)
[![Dataset](https://img.shields.io/badge/Dataset-Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/datasets/rjmanoj/credit-card-customer-churn-prediction)

> ⚠️ **App may be sleeping** — Streamlit free tier may hibernate. Click **Live App** and wait ~30s.

</div>

---

## 📂 Project Structure

```
Customer-Churn-Prediction/
│
├── app/
│   └── app.py                        # Streamlit web application
│
├── data/
│   ├── raw/
│   │   └── Churn_Modelling.csv       # Original dataset
│   └── processed/
│       └── Churn_processed.csv       # Cleaned and encoded dataset
│
├── models/
│   ├── churn_prediction_model.h5     # Trained Neural Network
│   ├── scaler.pkl                    # Fitted StandardScaler
│   └── training_columns.pkl          # Column list for consistent inference
│
├── notebooks/
│   └── churn_analysis.ipynb          # Full analysis notebook
│
├── src/
│   ├── preprocessing.py              # Data loading and preprocessing functions
│   ├── train_model.py                # Model building and training functions
│   └── evaluate.py                   # Model evaluation functions
│
├── requirements.txt
└── README.md
```

---

## 🛠️ Tech Stack

<div align="center">

| 🏷️ Category | 🔧 Tools |
|---|---|
| 🐍 **Language** | Python 3.11 |
| 🧠 **Deep Learning** | TensorFlow, Keras |
| 📊 **ML & Data** | Scikit-learn, Pandas, NumPy |
| 📈 **Visualization** | Matplotlib, Seaborn |
| 🚀 **Deployment** | Streamlit |
| 💾 **Model Serialisation** | Joblib |

</div>

---

## 📊 Dataset Description

The dataset used is the **Credit Card Customer Churn dataset from Kaggle**.

- **Total Records:** 10,000 customers
- **Features:** 14 columns (`RowNumber`, `CustomerId`, `Surname` dropped before modelling)
- **Target Variable:** `Exited` (1 = Churned, 0 = Stayed)
- **Class Distribution:** 79.6% Stayed / 20.4% Churned — handled via class weights

<div align="center">

| 🔑 Feature | 📝 Description |
|---|---|
| `CreditScore` | 💳 Customer credit score |
| `Geography` | 🌍 Customer location (France, Germany, Spain) — one-hot encoded |
| `Gender` | 👤 Male / Female — one-hot encoded |
| `Age` | 🎂 Customer age |
| `Tenure` | 📅 Years with bank |
| `Balance` | 💰 Account balance |
| `NumOfProducts` | 📦 Number of bank products |
| `HasCrCard` | 💳 Has credit card (1 = Yes, 0 = No) |
| `IsActiveMember` | ✅ Active member status (1 = Yes, 0 = No) |
| `EstimatedSalary` | 💵 Customer estimated salary |

</div>

---

## 📈 Key Insights from EDA

<div align="center">

| 🔍 Insight | 💼 Business Implication |
|---|---|
| 📉 **20.4% overall churn rate** | Significant revenue at risk — retention efforts needed |
| 🌍 **Germany has highest churn** | Target German customers with special retention offers |
| 👴 **Age 50–60 has 56.2% churn rate** | Highest risk group — prioritise retention for middle-aged customers |
| 🧑 **Age 40–50 has 34.0% churn rate** | Second highest risk group — early intervention recommended |
| 🧒 **Age <30 has only 7.5% churn rate** | Most loyal segment — leverage for referrals and upselling |

</div>

---

## ⚙️ Data Preprocessing

<div align="center">

| 🔢 Step | ⚙️ Detail |
|---|---|
| 🗑️ Drop columns | `RowNumber`, `CustomerId`, `Surname` removed |
| 🔤 One-Hot Encoding | `Geography` and `Gender` encoded using `pd.get_dummies(drop_first=True)` |
| 💾 Column list saved | `training_columns.pkl` saved to ensure consistent inference |
| ✂️ Train-Test Split | 80% train / 20% test, random state = 1 |
| 📏 Feature Scaling | `StandardScaler` — `fit_transform` on train, `transform` on test |

</div>

---

## 🤖 Model Training & Performance

Multiple models were evaluated with `class_weight='balanced'` applied to handle the 80/20 class imbalance.

<div align="center">

| 🤖 Model | 🎯 Accuracy |
|---|---|
| 📈 Logistic Regression | ~72% |
| 🌳 Decision Tree | ~76% |
| ✅ **Neural Network** | **~80%** |

</div>

**The Neural Network was selected as the final model** as it significantly outperforms the baseline models and captures complex, non-linear patterns in customer behaviour that simpler models miss. Decision Trees tend to overfit, and Logistic Regression assumes linear relationships — both limitations the Neural Network overcomes with its layered architecture and Dropout regularisation.

---

## 🧠 Neural Network Architecture

<div align="center">

| 🏗️ Layer | ⚙️ Configuration |
|---|---|
| ➡️ Input Layer | 11 features |
| 🔵 Dense Layer | 64 neurons (ReLU) |
| 🔄 Dropout | 0.3 |
| 🔵 Dense Layer | 32 neurons (ReLU) |
| 🔄 Dropout | 0.3 |
| 🎯 Output Layer | 1 neuron (Sigmoid) |

| ⚡ Training Config | 📊 Value |
|---|---|
| 📉 Loss Function | Binary Crossentropy |
| ⚙️ Optimizer | Adam |
| 🔁 Epochs | 50 |
| 📦 Batch Size | 32 |
| ⚖️ Class Weights | Applied to address 80/20 imbalance |

</div>

---

## 🔮 Inference Pipeline

At inference time three saved assets are loaded:

1. `churn_prediction_model.h5` — the trained neural network
2. `scaler.pkl` — the fitted `StandardScaler`
3. `training_columns.pkl` — the exact column list after one-hot encoding

This guarantees new customer data is encoded **identically** to how the training data was processed — no silent column mismatches.

---

## 🚀 Application Features

The deployed Streamlit dashboard includes:

- 🎛️ **Customer Input Panel** — credit score, age, tenure, balance, number of products, credit card status, active membership, estimated salary, geography, and gender
- 🤖 **Real Model Inference** — predictions from the trained neural network
- 🚦 **Three Risk Tiers** — High (>50%), Medium (30–50%), Low (<30%) with visual progress bar
- 💡 **Retention Suggestions** — contextual tips based on the customer's specific risk factors

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

## 💡 Business Recommendations

1. 🎯 **Target German customers** with special retention offers as they show higher churn probability
2. 💤 **Engage inactive members** through loyalty programs, personalised emails, or incentives
3. 👴 **Focus on customers aged 50–60** as this group has the highest churn rate at 56.2%
4. 🧑 **Monitor customers aged 40–50** as they represent the second highest risk group at 34.0%
5. 🎁 Introduce **personalised financial products** based on customer behaviour and risk score

---

## 🔭 Future Improvements

- [ ] 🌲 Improve model performance using **Gradient Boosting or XGBoost**
- [ ] 🔧 Perform **hyperparameter tuning** to further optimise prediction accuracy
- [ ] 📊 Incorporate **additional customer behaviour features** such as transaction frequency
- [ ] 🧪 Implement **A/B testing strategies** to evaluate churn reduction campaigns
- [ ] ⚡ Build a **real-time data pipeline** for automated churn monitoring
- [ ] 🔍 Add **SHAP values** for deeper model explainability

---

## 📋 Project Information

<div align="center">

| 📌 Field | 📝 Detail |
|---|---|
| 👩‍💻 **Created by** | Ayushi Rai |
| 🧠 **Model** | Neural Network (TensorFlow / Keras) |
| 🎯 **Test Accuracy** | ~80% |
| 📊 **Dataset** | Credit Card Customer Churn — Kaggle (10,000 records) |
| 📅 **Date** | March 2026 |

</div>

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

---

<div align="center">
  <a href="#-table-of-contents">⬆️ Back to Top</a>
</div>
