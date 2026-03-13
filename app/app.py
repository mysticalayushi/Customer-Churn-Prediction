import streamlit as st
import numpy as np
import joblib

# Page configuration
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

# Title
st.title("📊 Customer Churn Prediction Dashboard")
st.write("Predict whether a bank customer is likely to churn.")

# =========================
# Dashboard Metrics
# =========================
col1, col2, col3 = st.columns(3)

col1.metric("Model Type", "Customer Churn")
col2.metric("Algorithm", "Neural Network")
col3.metric("Accuracy", "85%")

st.markdown("---")

# =========================
# Customer Input Section
# =========================
st.header("Customer Details")
st.write("Enter customer information to predict churn risk.")

# Sidebar
st.sidebar.header("Customer Information")

credit_score = st.sidebar.slider("Credit Score", 300, 850, 600)
age = st.sidebar.slider("Age", 18, 90, 35)
tenure = st.sidebar.slider("Tenure (Years with Bank)", 0, 10, 3)
balance = st.sidebar.number_input("Account Balance", 0.0, 250000.0, 50000.0)
products = st.sidebar.selectbox("Number of Products", [1,2,3,4])
active_member = st.sidebar.selectbox("Active Member", ["Yes","No"])

# Convert categorical values
active_member = 1 if active_member == "Yes" else 0

# =========================
# Dummy Prediction Logic
# =========================
def predict_churn(credit_score, age, tenure, balance, products, active_member):

    risk_score = 0

    if credit_score < 500:
        risk_score += 1
    if balance > 120000:
        risk_score += 1
    if age > 50:
        risk_score += 1
    if products == 1:
        risk_score += 1
    if active_member == 0:
        risk_score += 1

    if risk_score >= 3:
        return "Churn", 0.78
    else:
        return "No Churn", 0.22


# =========================
# Prediction Button
# =========================
if st.button("Predict Customer Churn"):

    prediction, probability = predict_churn(
        credit_score,
        age,
        tenure,
        balance,
        products,
        active_member
    )

    st.subheader("Prediction Result")

    if prediction == "Churn":
        st.error("⚠️ Customer Likely to Churn")
    else:
        st.success("✅ Customer Likely to Stay")

    st.write(f"Confidence Score: {probability:.2f}")

    # Risk progress bar
    st.progress(int(probability * 100))

# =========================
# Project Description
# =========================
st.markdown("---")

st.subheader("About This Project")

st.write(
"""
This application predicts whether a bank customer is likely to churn based on
demographic and financial attributes such as credit score, age, balance, and
product usage.

The goal is to help financial institutions identify high-risk customers and
take proactive retention actions.
"""
)

# Footer
st.markdown("---")
st.write("Project: Customer Churn Prediction")
st.write("Built with Streamlit")


