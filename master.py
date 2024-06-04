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
import urllib.parse

username = "mzozulia@flowgenius.com"
password = "everlyquinn#7665"
email = "mzozulia@flowgenius.com"
firstname = "michael"
lastname = "zozulia"
threadid = "adfadfadsfad"

combined = f"{username}_{password}_{email}_{firstname}_{lastname}_{threadid}"
client_ref_id = urllib.parse.quote(combined)
#print(crefid)


if not st.query_params:
    buylink = "https://buy.stripe.com/test_6oE3eheEq5mQaYgaEO"
    stripe_js = """
        <script async
  src="https://js.stripe.com/v3/buy-button.js">
</script>

<stripe-buy-button
  buy-button-id="buy_btn_1PNyraDvYq7iSz1pw0hG0epN"
  publishable-key="pk_test_51OEP9VDvYq7iSz1pimUZipoNaLzZzc05H8M48zgdkoNuPaq1R8Q26baEcwybVPP7kRrfKiFM7MdHzv0mgLdK1Chi00b78eoTf7"
  client-reference-id="{customer_ref}"
  customer-email="{customer_email}">
</stripe-buy-button>
        """.format(customer_ref="adfadsfdsfads", customer_email=email)



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
    d = c.client_reference_id
    print(d)

    st.write(d)
    e = c.client_reference_id
    print(e)
    print(c)
    st.write(c)
    print(c.customer)
    g = stripe.Customer.retrieve(api_key=st.secrets.stripe.api_key_dev,id=c.customer)
    print(g)