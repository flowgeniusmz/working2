import streamlit as st
from streamlit.components.v1 import html

def get_stripe_js():
    runmode = st.secrets.stripe.runmode
    clientrefid = "TESTING"
    customeremail = "test@test.com"
    if runmode == "test":
        buylink = st.secrets.stripe.buylink_dev
        buybuttonid = st.secrets.stripe.buybuttonid_dev
        pubkey = st.secrets.stripe.pub_key_dev
    elif runmode == "live":
        buylink = st.secrets.stripe.buylink
        buybuttonid = st.secrets.stripe.buybuttonid
        pubkey = st.secrets.stripe.pub_key

    stripejs_template = """
                <script async
                src="https://js.stripe.com/v3/buy-button.js">
                </script>

                <stripe-buy-button
                buy-button-id="{buybuttonid}"
                publishable-key="{publishablekey}"
                client-reference-id="{clientrefid}"
                customer-email="{customeremail}"
                >
                </stripe-buy-button>            
                """
    stripejs = stripejs_template.format(buybuttonid=buybuttonid, publishablekey=pubkey, clientrefid=clientrefid, customeremail=customeremail)
    print(stripejs)
    return stripejs

def display_stripejs(stripejs):
    html(stripejs)

