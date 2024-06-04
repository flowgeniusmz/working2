import streamlit as st
import stripe
successurl = "http://localhost:8501/?session_id={CHECKOUT_SESSION_ID}"
cancelurl = "http://localhost:8501/"
checkoutpayload = {"api_key": st.secrets.stripe.api_key_dev, "mode": "subscription", "ui_mode": "hosted", "line_items": [{"price": st.secrets.stripe.price_dev, "quantity": 1}], "success_url": successurl, "cancel_url": cancelurl}

ch = stripe.checkout.Session.create(**checkoutpayload)
print(ch)