import streamlit as st
from config import pagesetup as ps
from typing import Literal
from supabase import create_client as supaClient
from openai import OpenAI as oaiClient
import stripe

if "userstate" not in st.session_state:
    st.session_state.userstate = 0
    st.session_state.usertype = None
    st.session_state.userinfo = {"username": None, "password": None, "email": None, "businessname": None, "businessaddress": None, "firstname": None, "lastname": None, "fullname": None, "createddate": None, "threadid": None, "vectorstoreid": None, "userrole": None}
    st.session_state.paytype = None
    st.session_state.payinfo = {"checkoutsession": None, "id": None, "url": None}

    st.session_state.usertypes = ["guest", "new", "existing"]
    st.session_state.paytypes = ["paid", "unpaid"]
    st.session_state.userroles = ["Admin", "Client", "Carrier"]

elif st.session_state.userstate == 0:
    st.write("0")


elif st.session_state.userstate == 1:
    st.write("1")

elif st.session_state.userstate == 2:
    st.write("2")

elif st.session_state.userstate == 3: 
    st.write("3")

elif st.session_state.userstate == 4: 
    st.write("4")

elif st.session_state.userstate == 5: 
    st.write("5")

else:
    st.error("ERROR")


class UserState:
    def __init__(self):
        self.userstate9_sessionstate()
    def controller(self):
        if st.session_state.userstate == 0:
            self.userstate0_render()
        elif st.session_state.userstate == 1:
            self.userstate1_usertype()
        elif st.session_state.userstate == 2:
            self.userstate2_userinfo()
        elif st.session_state.userstate == 3: 
            self.userstate3_payment()
        elif st.session_state.userstate == 4: 
            self.userstate4_login()
        elif st.session_state.userstate == 5: 
            self.userstate5_welcome()
        else:
            self.userstate9_error

    def userstate0_render(self):
        st.write("a")
    
    def userstate1_usertype(self):
        st.write("a")
    
    def userstate2_userinfo(self):
        st.write("a")
    
    def userstate3_payment(self):
        st.write("a")

    def userstate4_login(self):
        st.write("a")

    def userstate5_welcome(self):
        self.userstate9_navhome()


    def userstate8_createcheckout(self):
        st.session_state.checkoutsession = stripe.checkout.Session.create(**st.session_state.checkoutpayload)
        st.session_state.sessionid = st.session_state.checkoutsession.id
        st.session_state.sessionurl = st.session_state.checkoutsession.url
    
    def userstate8_retrievecheckout(self):
        st.session_state.checkoutsession = stripe.checkout.Session.retrieve(**st.session_state.checkoutpayload1)

    def userstate8_createvectorstore(self):
        oclient = oaiClient(api_key=st.secrets.openai.api_key)
        name = f"SpartakusAI - {st.session_state.userinfo['fullname']}"
        vector = oclient.beta.vector_stores.create(name=name)
        vectorid = vector.id
        st.session_state.userinfo['vectorstoreid'] = vectorid

    def userstate8_createthread(self):
        oclient = oaiClient(api_key=st.secrets.openai.api_key)
        tool_resources = {"file_search": {"vector_store_ids": [st.session_state.userinfo['vectorstoreid']]}}
        thread = oclient.beta.threads.create(tool_resources=tool_resources)
        threadid = thread.id
        st.session_state.userinfo['threadid'] = threadid

    def userstate8_authuser(self):
        username = st.session_state.userinfo['username']
        password = st.session_state.userinfo['password']
        sclient = supaClient(supabase_key=st.secrets.supabase.api_key_admin, supabase_url=st.secrets.supabase.url)
        response = sclient.table("users").select(st.session_state.selectstring).eq(column="username", value=username).eq(column="password", value=password).execute()
        if response.data:
            st.session_state.loginstatus = "success"
            st.session_state.logindata = response.data[0]
        else:
            st.session_state.loginstatus = "error"

    def userstate8_createuser(self):
        sclient = supaClient(supabase_key=st.secrets.supabase.api_key_admin, supabase_url=st.secrets.supabase.url)
        response = sclient.table("users").insert(json=st.session_state.userinfo).execute()
        if response.data:
            st.session_state.loginstatus = "success"
            st.session_state.logindata = response.data[0]
        else:
            st.session_state.loginstatus = "error"
    
    @st.experimental_dialog(title="New User Registration", width="large")
    def userstate8_newuserdialog(self):
        st.session_state.usertype = "new"
        st.session_state.userinfo['username'] = st.text_input(label="Username", key="_username")
        st.session_state.userinfo['password'] = st.text_input(label="Password", key="_password")
        st.session_state.userinfo['email'] = st.text_input(label="Email", key="_email")
        st.session_state.userinfo['firstname'] = st.text_input(label="First Name", key="_firstname")
        st.session_state.userinfo['lastname'] = st.text_input(label="Last Name", key="_lastname")
        st.session_state.userinfo['businessname'] = st.text_input(label="Business Name", key="_businessname")
        st.session_state.userinfo['businessaddress'] = st.text_input(label="Business Address", key="_businessaddress")
        st.session_state.userinfo['userrole'] = st.radio(label="User Role", key="_userrole", options=st.session_state.userroles, horizontal=True, index=None)
        btn = st.button(label="Submit", type="primary")
    
    def userstate9_navhome(self):
        st.switch_page(page="1_🏠_Home.py")

    def userstate9_error(self):
        st.error("ERROR")

    def userstate9_sessionstate(self):
        if "userstate" not in st.session_state:
            st.session_state.userstate = 0
            st.session_state.usertype = None
            st.session_state.userinfo = {"username": None, "password": None, "email": None, "businessname": None, "businessaddress": None, "firstname": None, "lastname": None, "fullname": None, "createddate": None, "threadid": None, "vectorstoreid": None, "userrole": None}
            st.session_state.paytype = None
            st.session_state.payinfo = {"checkoutsession": None, "id": None, "url": None}
            st.session_state.checkoutsession = None
            st.session_state.checkoutsessionid = st.query_params.get('session_id', None)
            st.session_state.checkoutsessionurl = None
            st.session_state.loginstatus = None
            st.session_state.logindata = None

            st.session_state.usertypes = ["guest", "new", "existing"]
            st.session_state.paytypes = ["paid", "unpaid"]
            st.session_state.loginstatuses = ["success", "error"]
            st.session_state.checkoutmode = "subscriptions"
            st.session_state.checkoutuimode = "hosted"
            st.session_state.lineitems = [{"price": st.secrets.stripe.price_dev, "quantity": 1}]
            st.session_state.cancelurl = "http://localhost:8501/"
            st.session_state.successurl = "http://localhost:8501/?session_id={CHECKOUT_SESSION_ID}"
            st.session_state.checkoutpayload = {"api_key": st.secrets.stripe.api_key_dev, "mode": st.session_state.checkoutmode, "ui_mode": st.session_state.checkoutuimode, "line_items": st.session_state.lineitems, "success_url": st.session_state.successurl, "cancel_url": st.session_state.cancelurl}
            st.session_state.checkoutpayload1 = {"api_key": st.secrets.stripe.api_key_dev, "id": st.session_state.session_id}
            st.session_state.userroles = ["Admin", "Client", "Carrier"]
            st.session_state.selectstring = "'username', 'password', 'email', 'firstname', 'lastname', 'fullname', 'vectorstoreid', 'threadid', 'createddate', 'userrole', 'businessname', 'businessaddress', 'form_036', 'form_125', 'form_126', 'form_127', 'form_130', 'form_133', 'form_137', 'form_140'"
            st.session_state.headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36','Accept-Language': 'en-US,en;q=0.9','Accept-Encoding': 'identity'}
