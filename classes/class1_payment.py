import streamlit as st
import stripe
from streamlit.components.v1 import html

class Payment:
    def __init__(self):
        self.initialize_attributes()

    def initialize_attributes(self):
        self.runmode = st.secrets.stripe.runmode
        self.mode = st.secrets.stripe.mode
        self.uimode = st.secrets.stripe.uimode
        self.client_reference_id = "adfadf"
        self.customer_email = "mzozulia@flowgneius.com"
        if self.runmode == "test":
            self._initialize_attributes_test()
        elif self.runmode == "live":
            self._initialize_attributes_live()

    def _initialize_attributes_test(self):
        self.api_key = st.secrets.stripe.api_key_dev
        self.pub_key = st.secrets.stripe.pub_key_dev
        self.buy_link = st.secrets.stripe.buylink_dev
        self.buy_btn = st.secrets.stripe.buybuttonid_dev
        self.prod = st.secrets.stripe.prod_dev
        self.price = st.secrets.stripe.price_dev
        self.redirect_url = st.secrets.stripe.redirecturl_dev
        self.qrcode_path = st.secrets.stripe.qrcode_dev

    def _initialize_attributes_live(self):
        self.api_key = st.secrets.stripe.api_key
        self.pub_key = st.secrets.stripe.pub_key
        self.buy_link = st.secrets.stripe.buylink
        self.buy_btn = st.secrets.stripe.buybuttonid
        self.prod = st.secrets.stripe.prod
        self.price = st.secrets.stripe.price
        self.redirect_url = st.secrets.stripe.redirecturl
        self.qrcode_path = st.secrets.stripe.qrcode

    def display_payment(self):
        container = st.container(border=False)
        with container:
            self._display_button()
            self._display_qrcode()

    def _display_qrcode(self):
        self.qrcode = st.image(image=self.qrcode_path, caption="Scan the QR code to pay!", width=100)

    def _display_button(self):
        self._display_button_stripejs()
        self._display_button_html()

    def _display_button_html(self):
        self.buybutton = html(self.stripejs)

    def _display_button_stripejs(self):
        self.stripejs_template = """
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
        self.stripejs = self.stripejs_template.format(buybuttonid=self.buy_btn, publishablekey=self.pub_key, clientrefid=self.client_reference_id, customeremail=self.customer_email)