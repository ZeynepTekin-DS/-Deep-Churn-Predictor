import streamlit as st
import pandas as pd
import joblib

# Page Configuration
st.set_page_config(page_title="ChurnGuard AI", layout="centered")

# Load the Champion Model
@st.cache_resource
def load_model():
    # Ensure your file is named 'customer_model.pkl' in your HF repo
    return joblib.load('customer_model.pkl')

model = load_model()

# --- MAIN HEADER ---
st.title("🛡️ ChurnGuard AI: Customer Attrition Predictor")
st.markdown(f"""
This application utilizes a high-performance **XGBoost** algorithm to analyze the probability of customer churn. 
Our underlying model achieved a **0.9144 ROC-AUC** score during validation.
""")

st.divider()
st.subheader("📋 Enter Customer Details")

# --- INPUT AREA (CENTRALIZED) ---
col1, col2, col3 = st.columns(3)

with col1:
    gender = st.selectbox("Gender (0:M, 1:F)", [0, 1])
    SeniorCitizen = st.selectbox("Senior Citizen (0:No, 1:Yes)", [0, 1])
    Partner = st.selectbox("Has Partner? (0:No, 1:Yes)", [0, 1])
    Dependents = st.selectbox("Has Dependents? (0:No, 1:Yes)", [0, 1])

with col2:
    tenure = st.slider("Tenure (Months)", 0, 72, 12)
    IsNewCustomer = st.selectbox("Is New Customer? (0:No, 1:Yes)", [0, 1])
    TotalServices = st.slider("Total Services Used", 0, 10, 3)
    PaymentMethod = st.selectbox("Payment Method Code", [0, 1, 2, 3])

with col3:
    MonthlyCharges = st.number_input("Monthly Charges", 0.0, 200.0, 50.0)
    TotalCharges = st.number_input("Total Charges", 0.0, 10000.0, 500.0)
    AvgMonthly = st.number_input("Avg Monthly Spend", 0.0, 200.0, 50.0)
    Risk_Score = st.slider("Calculated Risk Score", 0, 500, 100)

# Creating the DataFrame for prediction
data = {
    'gender': gender, 'SeniorCitizen': SeniorCitizen, 'Partner': Partner,
    'Dependents': Dependents, 'tenure': tenure, 'PaymentMethod': PaymentMethod,
    'MonthlyCharges': MonthlyCharges, 'TotalCharges': TotalCharges,
    'AvgMonthly': AvgMonthly, 'Risk_Score': Risk_Score,
    'IsNewCustomer': IsNewCustomer, 'TotalServices': TotalServices
}
input_df = pd.DataFrame(data, index=[0])

st.divider()
st.subheader("🔍 Input Summary")
st.write(input_df)

if st.button("Run Prediction Analysis", use_container_width=True):
    # Perform Inference
    prediction_proba = model.predict_proba(input_df)[0, 1]
    
    st.subheader("📊 Analysis Results")
    if prediction_proba > 0.5:
        st.error(f"⚠️ ALERT: Churn Probability is {prediction_proba*100:.2f}%")
        st.markdown("**Strategic Recommendation:** High risk of attrition detected. Immediate retention action required, such as loyalty discounts or personalized engagement.")
    else:
        st.success(f"✅ SECURE: Loyalty Probability is {(1-prediction_proba)*100:.2f}%")
        st.markdown("**Strategic Recommendation:** Customer sentiment appears stable. Maintain current service quality and monitor for future behavioral changes.")

    # Critical Alert for engineered feature
    if Risk_Score > 200:
        st.warning("🚨 **Critical Note:** The Risk Score exceeds the safety threshold of 200!")