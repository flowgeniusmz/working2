import streamlit as st
from openai import OpenAI
from supabase import create_client
from streamlit_extras.stylable_container import stylable_container as sc
from typing import Literal
import stripe
import time
import json

# 1. 
st.set_page_config(page_icon=st.secrets.appconfig.app_icon, page_title=st.secrets.appconfig.app_name, layout=st.secrets.appconfig.app_layout, initial_sidebar_state=st.secrets.appconfig.app_initial_sidebar)

# 2. 
client = OpenAI(api_key=st.secrets.openai.api_key)
sclient = create_client(supabase_key=st.secrets.supabase.api_key_admin, supabase_url=st.secrets.supabase.url)

# 3. 
# Render --> User Type --> User Info --> Payment --> Login --. Welcome --- NOTE: Existing user skip user info and payment, already paid user goges to login - all users requried to enter username and login to authenticate
class UserState:
    def __init__(self):
        self.userstate7_sessionstate_controller()
        self.controller()

    def controller(self):
        if "userstate" not in st.session_state:
            st.session_state.userstate = 0
        if st.query_params:
            st.session_state.userstate = 3
            self.userstate3()
        elif st.session_state.userstate == 0:
            self.userstate0()
        elif st.session_state.userstate == 1:
            self.userstate1()
        elif st.session_state.userstate == 2:
            self.userstate2()
        elif st.session_state.userstate == 3:
            self.userstate3()
        elif st.session_state.userstate == 4:
            self.userstate4()
        else:
            self.userstate9_error()
    
    def userstate0(self):
        self.userstate7_sessionstate_guestchat()
        header_container = st.container(border=False)
        with header_container:
            header_cols = st.columns([10 , 2])
            with header_cols[0]:
                title = "SpartakusAI"
                subtitle = "Welcome"
                st.markdown(f"""<span style="font-weight: bold; font-size: 2em; color:#4A90E2;">{title} </span> <span style="font-weight: bold; color:#333333; font-size:1.3em;">{subtitle}</span>""", unsafe_allow_html=True)
            with header_cols[1]:
                usertype_pop = st.popover(label="Sign In or Join Now", disabled=False,  use_container_width=True)
                with usertype_pop:
                    newuserbutton2 = st.button("Join Now", type="primary", key="newuserbutton2", use_container_width=True)
                    existuserbutton2 = st.button("Sign In", type="primary", key="existuserbutton2", use_container_width=True)
        st.divider()
        body_container = st.container(border=False)
        with body_container:
            style1 = "{border: 2px solid rgba(40, 94, 159, 0.75); background-color: rgba(255, 255, 255, 0.75); border-radius: 0.5rem; padding: 1em; overflow: hidden; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2); transition: 0.3s; box-sizing: border-box;}"
            style2 = "{border: 2px solid rgba(0, 0, 0, 0.2); background-color: rgba(40, 94, 159, 0.75); border-radius: 0.5rem; padding: 1em; overflow: hidden; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2); transition: 0.3s; box-sizing: border-box;}"
            sc_outer = sc(key="dafds", css_styles=style2)
            with sc_outer:
                sc_inner = sc(key="adfdsfadszfasd", css_styles=style1)
                with sc_inner:
                    body_container2 = st.container(border=False)
                    with body_container2:
                        body_cols = st.columns([1, 20, 1, 20, 1])
                        with body_cols[1]:
                            existuserbutton1 = st.button("Sign In", type="primary", key="existuserbutton1", use_container_width=True)
                        with body_cols[3]:
                            newuserbutton1 = st.button("Join Now", type="primary", key="newuserbutton1", use_container_width=True)
        st.divider()
        asst_container = st.container(border=False)
        with asst_container:
            style1 = "{border: 2px solid rgba(40, 94, 159, 0.75); background-color: rgba(255, 255, 255, 0.75); border-radius: 0.5rem; padding: 1em; overflow: hidden; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2); transition: 0.3s; box-sizing: border-box;}"
            style2 = "{border: 2px solid rgba(0, 0, 0, 0.2); background-color: rgba(40, 94, 159, 0.75); border-radius: 0.5rem; padding: 1em; overflow: hidden; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2); transition: 0.3s; box-sizing: border-box;}"
            sc_outer = sc(key="adfadfadsfa", css_styles=style2)
            with sc_outer:
                sc_inner = sc(key="adsfd", css_styles=style1)
                with sc_inner:
                    self.chat_container = st.container(border=False, height=250)
                    with self.chat_container:
                        for guestmessage in st.session_state.guestthreadmessages:
                            with st.chat_message(name=guestmessage.role):
                                st.markdown(body=guestmessage.content[0].text.value)
            prompt_container = st.container(border=False)
            with prompt_container:
                guestprompt = st.chat_input(placeholder="Chat with Sparty here...", key="guestchatprompt")
        if newuserbutton1 or newuserbutton2:
            st.session_state.usertype = "new"
            self.userstate8_callback(userstate_number=1)
        if existuserbutton1 or existuserbutton2:
            st.session_state.usertype = "existing"
            self.userstate8_callback(userstate_number=4)
        if guestprompt:
            self.userstate8_guestchat(guestprompt=guestprompt)
        st.divider()
            
    @st.experimental_dialog(title="New User Registration", width="large")
    def userstate1(self):
        st.session_state.userinfo['username'] = st.text_input(label="Username", key="username")
        st.session_state.userinfo['password'] = st.text_input(label="Password", key="password", type="password")
        st.session_state.userinfo['email'] = st.text_input(label="Email Address", key="email")
        st.session_state.userinfo['firstname'] = st.text_input(label="First Name", key="firstname")
        st.session_state.userinfo['lastname'] = st.text_input(label="Last Name", key="lastname")
        st.session_state.userinfo['businessname'] = st.text_input(label="Business Name", key="businessname")
        st.session_state.userinfo['businessaddress'] = st.text_input(label="Business Address", key="businessaddress")
        st.session_state.userinfo['userrole'] = st.radio(label="User Role", key="userrole", options=["Admin, Client, Carrier"], index=None, horizontal=True)
        submit_btn = st.button(label="Submit", type="primary")
        if submit_btn:
            self.userstate8_callback(userstate_number=2)

    @st.experimental_dialog(title="Payment", width="large")
    def userstate2(self):
        st.session_state.checkoutsession = stripe.checkout.Session.create(api_key= st.secrets.stripe.api_key_dev, mode= st.session_state.checkoutmode, ui_mode= st.session_state.checkoutuimode, line_items= st.session_state.lineitems, success_url=st.session_state.successurl, cancel_url= st.session_state.cancelurl)
        st.session_state.checkoutsessionid = st.session_state.checkoutsession.id
        st.session_state.checkoutsessionurl = st.session_state.checkoutsession.url
        st.markdown("You will now be **redirected to Stripe** to submit payment. **Click the button** below to proceed.")
        agree = st.checkbox("accept", value=False)
        if agree:
            btn = st.link_button(label="Proceed to Payment", url=st.session_state.checkoutsessionurl)
        #if btn:
            #self.userstate8_callback(userstate_number=3)
    
    @st.experimental_dialog(title="Existing User Login", width="large")
    def userstate3(self):
        st.session_state.userinfo['username'] = st.text_input(label="Username", key="username")
        st.session_state.userinfo['password'] = st.text_input(label="Password", key="password", type="password")
        submit_btn = st.button(label="Submit", type="primary")
        if submit_btn:
            self.userstate8_callback(userstate_number=4)

    def userstate4(self):
        st.switch_page(page="pages/1_🏠_Home.py")

    def userstate7_sessionstate_controller(self):
        if "initialized" not in st.session_state:
            self.userstate7_sessionstate_initial()
        elif not st.session_state.initialized:
            self.userstate7_sessionstate_initial()

    def userstate7_sessionstate_initial(self):
        st.session_state.initialized = True
        st.session_state.userstate = 0
        st.session_state.usertype = "guest"
        ### Userinfo
        st.session_state.userinfo = {"username": None, "password": None, "email": None, "businessname": None, "businessaddress": None, "firstname": None, "lastname": None, "fullname": None, "createddate": None, "threadid": None, "vectorstoreid": None, "userrole": None}
        st.session_state.username = None
        st.session_state.password = None
        st.session_state.email = None
        st.session_state.firstname = None
        st.session_state.lastname = None
        st.session_state.fullname = None
        st.session_state.businessname = None
        st.session_state.businessaddress = None
        st.session_state.userrole = None
        st.session_state.threadid = None
        st.session_state.vectorid = None
        st.session_state.createddate = None
        ### Guestchat
        st.session_state.guestthreadid = None
        st.session_state.guestpromptid = None
        st.session_state.guestresponse = None
        st.session_state.guestresponseid = None
        st.session_state.guestprompt = None
        st.session_state.guestmessages = [{"role": "assistant", "content": "Hi I'm Sparty! How can I help you?"}]
        st.session_state.guestthreadmessages = []
        st.session_state.guestrunid = None
        st.session_state.guestrun = None
        # Checkout
        st.session_state.query_params = st.query_params
        st.session_state.query_params_empty = not bool(st.query_params)
        st.session_state.checkoutmode = "subscription"
        st.session_state.checkoutuimode = "hosted"
        st.session_state.lineitems = [{"price": st.secrets.stripe.price_dev, "quantity": 1}]
        st.session_state.checkoutsession = None
        st.session_state.checkoutsessionid = st.query_params.get("session_id", None)
        st.session_state.checkoutsessionurl = None
        st.session_state.cancelurl = "http://localhost:8501/"
        st.session_state.successurl = "http://localhost:8501/?session_id={CHECKOUT_SESSION_ID}"+f"&username={st.session_state.username}"
        st.session_state.checkoutpayload = {"api_key": st.secrets.stripe.api_key_dev, "mode": st.session_state.checkoutmode, "ui_mode": st.session_state.checkoutuimode, "line_items": st.session_state.lineitems, "success_url": st.session_state.successurl, "cancel_url": st.session_state.cancelurl}
        #st.session_state.checkoutpayload1 = {"api_key": st.secrets.stripe.api_key_dev, "id": st.session_state.session_id}
        #Lists
        st.session_state.userroles = st.secrets.streamlit.userroles
        st.session_state.usertypes = st.secrets.streamlit.usertypes
        st.session_state.paymenttypes = st.secrets.streamlit.paymenttypes

    def userstate7_sessionstate_guestchat(self):
        client = OpenAI(api_key=st.secrets.openai.api_key)
        if st.session_state.guestthreadid is None:
            st.session_state.guestthreadid = client.beta.threads.create().id
        elif st.session_state.guestthreadid is not None:
            if "guestthreadmessages" not in st.session_state:
                st.session_state.guestthreadmessages = []
            st.session_state.guestthreadmessages = client.beta.threads.messages.list(thread_id=st.session_state.guestthreadid)    

    def userstate8_callback(self, userstate_number):
        st.session_state.userstate = userstate_number
        st.rerun()

    @st.experimental_fragment
    def userstate8_guestchat(self, guestprompt):
        # self.userstate7_sessionstate_guestchat()
        client = OpenAI(api_key=st.secrets.openai.api_key)
        st.session_state.guestprompt = guestprompt
        with self.chat_container:
            with st.chat_message("user"):
                st.markdown(guestprompt)
        st.session_state.guestpromptid = client.beta.threads.messages.create(role="user", content=st.session_state.guestprompt, thread_id=st.session_state.guestthreadid)
        st.session_state.guestrun = client.beta.threads.runs.create(thread_id=st.session_state.guestthreadid, assistant_id=st.secrets.openai.assistant_id)
        st.session_state.guestrunid = st.session_state.guestrun.id
        while st.session_state.guestrun.status == "in_progress" or st.session_state.guestrun.status == "queued":
            time.sleep(1)
            st.toast("Processing chat")
            st.session_state.guestrun = client.beta.threads.runs.retrieve(run_id=st.session_state.guestrun.id, thread_id=st.session_state.guestthreadid)
            if st.session_state.guestrun.status == "completed":
                st.toast("Complete")
                st.session_state.guestthreadmessages = client.beta.threads.messages.list(thread_id=st.session_state.guestthreadid)
                for guestresponse in st.session_state.guestthreadmessages:
                    if guestresponse.role == "assistant" and guestresponse.run_id == st.session_state.guestrun.id:
                        st.session_state.guestresponse = guestresponse.content[0].text.value
                        st.session_state.guestresponseid = guestresponse.id
                        with self.chat_container:
                            with st.chat_message(name="assistant"):
                                st.markdown(st.session_state.guestresponse)

    def userstate9_error(self):
        st.error("ERROR")

user_state = UserState()


