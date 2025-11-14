import pandas as pd
import streamlit as st
import warnings

import joblib
import importlib

# Suppress sklearn version mismatch warnings
warnings.filterwarnings("ignore", category=UserWarning, module="sklearn.base")


def load_model(path="Fraud_detection.pkl"):
    # Monkeypatch for sklearn internals that changed between versions.
    try:
        ct = importlib.import_module("sklearn.compose._column_transformer")
        if not hasattr(ct, "_RemainderColsList"):
            class _RemainderColsList(list):
                pass

            setattr(ct, "_RemainderColsList", _RemainderColsList)
    except Exception:
        # If sklearn isn't available or the module layout differs, continue
        pass

    try:
        return joblib.load(path)
    except Exception as e:
        st.error(f"Failed to load model: {e}")
        return None


model = load_model()

st.title("Fraud Detection Prediction App")

st.markdown("Please enter the transaction details and use the predict button")

st.divider()

transaction_type = st.selectbox("Transaction Type", ["TRANSFER", "PAYMENT", "CASH_OUT", "DEPOSIT"])
amount = st.number_input("Amount", min_value=0.0, value=1000.0)
oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value=0.0, value=10000.0)
newbalanceOrig = st.number_input("New Balance (Sender)", min_value=0.0, value=9000.0)
oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0, value=10000.0)
newbalanceDest = st.number_input("New Balance (Receiver)", min_value=0.0, value=0.0)

if st.button("Predict"):
    if model is None:
        st.error("Model is not loaded. Cannot make predictions.")
    else:
        input_data = pd.DataFrame([
            {
                "type": transaction_type,
                "amount": amount,
                "oldbalanceOrg": oldbalanceOrg,
                "newbalanceOrig": newbalanceOrig,
                "oldbalanceDest": oldbalanceDest,
                "newbalanceDest": newbalanceDest,
            }
        ])

        try:
            prediction = model.predict(input_data)[0]
            st.subheader(f"Prediction :")
            if prediction == 1:
                st.error("This transaction can be fraud")
            else:
                st.success("This transaction looks like not a fraud")
        except Exception as e:
            st.error(f"Prediction failed: {e}")