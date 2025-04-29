import streamlit as st
import numpy as np
import joblib
import requests
import io

# --- Download the model from GitHub ---
url = 'https://raw.githubusercontent.com/LuisaPolicarpo/Hotel/main/cancellation_model.pkl'
response = requests.get(url)
model = joblib.load(io.BytesIO(response.content))

# --- Page Title ---
st.title("🏨 Hotel Booking Cancellation Predictor")
st.markdown("Predict whether a hotel booking will be canceled and take smart actions to reduce risk.")

# --- Sidebar Inputs ---
st.sidebar.header("📋 Booking Information")

lead_time = st.sidebar.slider("Lead Time (days)", min_value=0, max_value=500, value=100)
adr = st.sidebar.number_input("Average Daily Rate (ADR)", min_value=0.0, max_value=500.0, value=100.0)

deposit_type = st.sidebar.selectbox("Deposit Type", ["No Deposit", "Non Refund", "Refundable"])
customer_type = st.sidebar.selectbox("Customer Type", ["Transient", "Group", "Contract", "Transient-Party"])
market_segment = st.sidebar.selectbox("Market Segment", ["Online TA", "Direct", "Corporate", "Offline TA/TO"])

total_of_special_requests = st.sidebar.slider("Total Special Requests", min_value=0, max_value=5, value=0)
booking_changes = st.sidebar.slider("Booking Changes", min_value=0, max_value=10, value=0)
previous_cancellations = st.sidebar.slider("Previous Cancellations", min_value=0, max_value=10, value=0)
is_repeated_guest = st.sidebar.selectbox("Repeated Guest?", ["No", "Yes"])
is_repeated_guest = 1 if is_repeated_guest == "Yes" else 0

# --- Predict ---
if st.button("Predict Cancellation"):

    # Encoding deposit_type
    deposit_type_no_deposit = 1 if deposit_type == "No Deposit" else 0
    deposit_type_non_refund = 1 if deposit_type == "Non Refund" else 0

    # Encoding customer_type
    customer_type_contract = 1 if customer_type == "Contract" else 0
    customer_type_group = 1 if customer_type == "Group" else 0
    customer_type_transient_party = 1 if customer_type == "Transient-Party" else 0

    # Encoding market_segment
    market_segment_corporate = 1 if market_segment == "Corporate" else 0
    market_segment_direct = 1 if market_segment == "Direct" else 0
    market_segment_offline = 1 if market_segment == "Offline TA/TO" else 0

    input_data = np.array([[
        lead_time,
        adr,
        deposit_type_no_deposit,
        deposit_type_non_refund,
        customer_type_contract,
        customer_type_group,
        customer_type_transient_party,
        market_segment_corporate,
        market_segment_direct,
        market_segment_offline,
        total_of_special_requests,
        booking_changes,
        previous_cancellations,
        is_repeated_guest
    ]])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠️ This booking is likely to be CANCELED!")

        st.subheader("🛠 Suggested Actions to Reduce Cancellation Risk:")
        offer_discount = st.checkbox("📧 Send 5% discount email")
        offer_breakfast = st.checkbox("🍳 Add free breakfast")
        allow_late_checkout = st.checkbox("🕐 Allow late check-in/out")

        if offer_discount or offer_breakfast or allow_late_checkout:
            st.success("✅ Actions selected! Make sure to notify the guest.")
    else:
        st.success("✅ This booking is likely to be CONFIRMED!")
