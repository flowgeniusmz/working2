import streamlit as st
from openai import OpenAI
import stripe
from supabase import create_client
from streamlit_extras.stylable_container import stylable_container as sc
from typing import List, Dict, Literal
from dataclasses import dataclass
import time
import json
from streamlit.components.v1 import html, components


if not st.query_params:
    buylink = "https://buy.stripe.com/test_5kA2ad53Q6qU4zS6ox"
    stripe_js = """
        <script async
    src="https://js.stripe.com/v3/buy-button.js">
    </script>

    <stripe-buy-button
    buy-button-id="buy_btn_1PNyraDvYq7iSz1pw0hG0epN"
    publishable-key="{}"
    >
    </stripe-buy-button>
        """.format(st.secrets.stripe.api_key_dev1)


    terms = st.checkbox(label="Agree", value=False)
    if terms:
        subscribe = st.button(label="Subscribe")
        if subscribe:
            html(stripe_js)
            st.image("spartakusai_payment_dev.png", caption="Scan the QR code to pay")
else:
    sessionid = st.query_params.session_id
    st.write(sessionid)
    c = stripe.checkout.Session.retrieve(id=sessionid, api_key=st.secrets.stripe.api_key_dev)
    st.write(c)

    