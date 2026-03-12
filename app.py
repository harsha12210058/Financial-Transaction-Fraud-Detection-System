import streamlit as st
import pandas as pd
import joblib

# Load trained model and feature order
model = joblib.load("fraud_model.pkl")
features = joblib.load("model_features.pkl")

st.set_page_config(page_title="Fraud Detection System")

st.title("💳 Financial Transaction Fraud Detection")

st.write("Enter transaction details to check whether the transaction is fraudulent.")

# Transaction Type

transaction_type = st.selectbox(
    "Transaction Type",
    ["", "TRANSFER", "CASH_OUT", "PAYMENT", "DEBIT", "CASH_IN"]
)

# Transaction Inputs

amount = st.number_input(
    "Transaction Amount",
    min_value=0.0,
    value=None,
    placeholder="Enter transaction amount"
)

oldbalanceOrg = st.number_input(
    "Sender Previous Balance",
    min_value=0.0,
    value=None,
    placeholder="Enter sender previous balance"
)

newbalanceOrig = st.number_input(
    "Sender Balance After Transaction",
    min_value=0.0,
    value=None,
    placeholder="Enter sender balance after transaction"
)

oldbalanceDest = st.number_input(
    "Receiver Previous Balance",
    min_value=0.0,
    value=None,
    placeholder="Enter receiver previous balance"
)

newbalanceDest = st.number_input(
    "Receiver Balance After Transaction",
    min_value=0.0,
    value=None,
    placeholder="Enter receiver balance after transaction"
)

hour = st.number_input(
    "Transaction Hour (0–23)",
    min_value=0,
    max_value=23,
    value=None,
    placeholder="Enter transaction hour"
)

day = st.number_input(
    "Transaction Day",
    min_value=0,
    value=None,
    placeholder="Enter transaction day"
)

# Prediction

if st.button("Predict Transaction"):

    if (
        transaction_type == ""
        or amount is None
        or oldbalanceOrg is None
        or newbalanceOrig is None
        or oldbalanceDest is None
        or newbalanceDest is None
        or hour is None
        or day is None
    ):
        st.warning("⚠ Please fill all fields before prediction.")

    else:

        # Encode transaction type
        is_transfer = 1 if transaction_type == "TRANSFER" else 0
        is_cashout = 1 if transaction_type == "CASH_OUT" else 0

        # Feature engineering (same as training)
        orig_balance_error = oldbalanceOrg - amount - newbalanceOrig
        dest_balance_error = oldbalanceDest + amount - newbalanceDest
        amount_balance_ratio = amount / (oldbalanceOrg + 1)
        account_emptied = 1 if newbalanceOrig == 0 else 0

        isMerchant = 0

        amount_exceeds_balance = 1 if amount > oldbalanceOrg else 0
        receiver_balance_jump = 1 if newbalanceDest > oldbalanceDest * 10 else 0
        large_transaction = 1 if amount > 200000 else 0

        risk_score = (
            amount_exceeds_balance
            + receiver_balance_jump
            + account_emptied
        )

        # Create dataframe for prediction
        input_data = pd.DataFrame({

            "amount":[amount],
            "oldbalanceOrg":[oldbalanceOrg],
            "newbalanceOrig":[newbalanceOrig],
            "oldbalanceDest":[oldbalanceDest],
            "newbalanceDest":[newbalanceDest],

            "orig_balance_error":[orig_balance_error],
            "dest_balance_error":[dest_balance_error],
            "amount_balance_ratio":[amount_balance_ratio],

            "account_emptied":[account_emptied],
            "isMerchant":[isMerchant],

            "is_transfer":[is_transfer],
            "is_cashout":[is_cashout],

            "day":[day],
            "hour":[hour],

            "amount_exceeds_balance":[amount_exceeds_balance],
            "receiver_balance_jump":[receiver_balance_jump],
            "large_transaction":[large_transaction],

            "risk_score":[risk_score]

        })

        # Ensure correct feature order
        input_data = input_data[features]

        # Model prediction
        prediction = model.predict(input_data)[0]

        st.subheader("Prediction Result")

        if prediction == 1:
            st.error("🚨 Fraudulent Transaction Detected")
        else:
            st.success("✅ Legitimate Transaction")