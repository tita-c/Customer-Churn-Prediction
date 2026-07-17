import streamlit as st
import pickle
import pandas as pd


# Load saved files
model = pickle.load(open("churn_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
features = pickle.load(open("feature_names.pkl", "rb"))


# Page configuration
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)


st.title("📊 Customer Churn Prediction System")

st.write(
    "Enter customer details to predict churn probability."
)


# Input fields

tenure = st.slider(
    "Customer Tenure (Months)",
    0,
    72,
    12
)

monthly_charges = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    value=70.0
)

total_charges = st.number_input(
    "Total Charges",
    min_value=0.0,
    value=1000.0
)


contract = st.selectbox(
    "Contract Type",
    [
        "Month-to-month",
        "One year",
        "Two year"
    ]
)


internet = st.selectbox(
    "Internet Service",
    [
        "DSL",
        "Fiber optic",
        "No"
    ]
)


payment = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer",
        "Credit card"
    ]
)


if st.button("Predict Churn"):


    # Create empty dataframe with same features
    input_data = pd.DataFrame(
        0,
        index=[0],
        columns=features
    )


    # Fill numerical values
    input_data["tenure"] = tenure
    input_data["MonthlyCharges"] = monthly_charges
    input_data["TotalCharges"] = total_charges


    # Fill categorical encoded values

    if contract == "One year":
        input_data["Contract_One year"] = 1

    elif contract == "Two year":
        input_data["Contract_Two year"] = 1


    if internet == "Fiber optic":
        input_data["InternetService_Fiber optic"] = 1

    elif internet == "No":
        input_data["InternetService_No"] = 1


    if payment == "Electronic check":
        input_data["PaymentMethod_Electronic check"] = 1


    # Scaling
    input_scaled = scaler.transform(input_data)


    # Prediction
    prediction = model.predict(input_scaled)

    probability = model.predict_proba(input_scaled)[0][1]


    st.subheader("Prediction Result")


    if prediction[0] == 1:

        st.error(
            "⚠️ Customer is likely to churn"
        )

        st.write(
            f"Churn Probability: {probability*100:.2f}%"
        )

    else:

        st.success(
            "✅ Customer is likely to stay"
        )

        st.write(
            f"Churn Probability: {probability*100:.2f}%"
        )
