import os
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import tensorflow as tf

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

# ── Load trained model assets ─────────────────────────────────────────────────
@st.cache_resource
def load_assets():
    base    = os.path.dirname(__file__)
    model   = tf.keras.models.load_model(
                  os.path.join(base, "../models/churn_prediction_model.keras"))
    scaler  = joblib.load(os.path.join(base, "../models/scaler.pkl"))
    columns = joblib.load(os.path.join(base, "../models/training_columns.pkl"))
    return model, scaler, columns

model, scaler, training_columns = load_assets()

# ── Inference ─────────────────────────────────────────────────────────────────
def predict_churn(customer: dict) -> float:
    """
    Encode, scale, and predict churn probability for one customer.
    Relies on training_columns.pkl to guarantee column alignment with training.
    """
    df_input = pd.DataFrame([customer])
    df_input = pd.get_dummies(df_input, columns=["Geography", "Gender"], drop_first=True)
    df_input = df_input.reindex(columns=training_columns, fill_value=0)
    scaled   = scaler.transform(df_input)
    prob     = model.predict(scaled, verbose=0)[0][0]
    return float(prob)

# ── Header ────────────────────────────────────────────────────────────────────
st.title("📊 Customer Churn Prediction Dashboard")
st.write("Predict whether a bank customer is likely to churn.")

col1, col2, col3 = st.columns(3)
col1.metric("Model Type", "Customer Churn")
col2.metric("Algorithm",  "Neural Network")
col3.metric("Accuracy",   "~85%")

st.markdown("---")

# ── Sidebar inputs ────────────────────────────────────────────────────────────
st.sidebar.header("Customer Information")

credit_score = st.sidebar.slider("Credit Score",             300,  850,  600)
age          = st.sidebar.slider("Age",                       18,   90,   35)
tenure       = st.sidebar.slider("Tenure (Years with Bank)",   0,   10,    3)
balance      = st.sidebar.number_input("Account Balance",
                   min_value=0.0, max_value=250000.0, value=50000.0,
                   step=1000.0, format="%.2f")
num_products = st.sidebar.selectbox("Number of Products", [1, 2, 3, 4])
has_cr_card  = st.sidebar.selectbox("Has Credit Card",    ["Yes", "No"])
is_active    = st.sidebar.selectbox("Active Member",      ["Yes", "No"])
salary       = st.sidebar.number_input("Estimated Salary",
                   min_value=0.0, max_value=250000.0, value=100000.0,
                   step=1000.0, format="%.2f")

# Geography and Gender — critical predictive features
st.sidebar.markdown("---")
geography = st.sidebar.selectbox("Geography", ["France", "Germany", "Spain"])
gender    = st.sidebar.selectbox("Gender",    ["Female", "Male"])

# ── Main area ─────────────────────────────────────────────────────────────────
st.header("Customer Details")
st.write("Enter customer information in the sidebar to predict churn risk.")

# Summary table
with st.expander("📋 Review entered customer details", expanded=False):
    summary = {
        "Credit Score"      : credit_score,
        "Age"               : age,
        "Tenure (years)"    : tenure,
        "Account Balance"   : f"${balance:,.2f}",
        "Number of Products": num_products,
        "Has Credit Card"   : has_cr_card,
        "Active Member"     : is_active,
        "Estimated Salary"  : f"${salary:,.2f}",
        "Geography"         : geography,
        "Gender"            : gender,
    }
    st.table(pd.DataFrame(summary.items(), columns=["Field", "Value"]))

# ── Prediction ────────────────────────────────────────────────────────────────
if st.button("Predict Customer Churn", type="primary"):

    customer = {
        "CreditScore"    : credit_score,
        "Age"            : age,
        "Tenure"         : tenure,
        "Balance"        : balance,
        "NumOfProducts"  : num_products,
        "HasCrCard"      : 1 if has_cr_card == "Yes" else 0,
        "IsActiveMember" : 1 if is_active   == "Yes" else 0,
        "EstimatedSalary": salary,
        "Geography"      : geography,
        "Gender"         : gender,
    }

    prob = predict_churn(customer)

    st.markdown("---")
    st.subheader("🎯 Prediction Result")

    res_col1, res_col2 = st.columns(2)
    with res_col1:
        st.metric("Churn Probability", f"{prob:.1%}")
    with res_col2:
        if prob > 0.5:
            st.error("🔴 HIGH RISK — This customer is likely to churn")
        elif prob > 0.3:
            st.warning("🟡 MEDIUM RISK — This customer may churn")
        else:
            st.success("🟢 LOW RISK — This customer is unlikely to churn")

    st.markdown("**Risk Level**")
    st.progress(prob)

    # ── Retention tips ────────────────────────────────────────────────────────
    st.markdown("---")
    st.subheader("💡 Retention Suggestions")
    tips = []
    if geography == "Germany":
        tips.append("📍 German customers show higher churn rates — consider a targeted retention offer.")
    if 40 <= age <= 60:
        tips.append("👤 Customers aged 40–60 are at higher churn risk — personalised outreach recommended.")
    if is_active == "No":
        tips.append("💤 Inactive members are more likely to churn — re-engagement campaign advised.")
    if num_products == 1:
        tips.append("📦 Single-product customers churn more — consider cross-selling another product.")
    if balance == 0:
        tips.append("💰 Zero balance customers show elevated churn — investigate account usage.")

    if tips:
        for tip in tips:
            st.markdown(f"- {tip}")
    else:
        st.markdown("✅ No major risk factors detected for this customer profile.")

# ── About ─────────────────────────────────────────────────────────────────────
st.markdown("---")
st.subheader("About This Project")
st.write("""
This application predicts whether a bank customer is likely to churn based on
demographic and financial attributes such as credit score, age, balance, geography,
and product usage.

The goal is to help financial institutions identify high-risk customers and
take proactive retention actions.

**Model:** Neural Network (TensorFlow / Keras)
**Dataset:** Credit Card Customer Churn — Kaggle (10,000 records)
**Key churn indicators:** Geography, Age, Active membership status
""")

st.markdown("---")
st.write("Project: Customer Churn Prediction | Built with Streamlit")
