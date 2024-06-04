import streamlit as st
import stripe
from supabase import create_client
from openai import OpenAI
from streamlit_extras.stylable_container import stylable_container as sc
from config import pagesetup as ps
from typing import Literal

if "userinfo" not in st.session_state:
    st.session_state.userinfo = {"username": None, "password": None, "email": None, "firstname": None, "lastname": None, "fullname": None, "businessname": None, "businessaddress": None, "userrole": None, "createddate": None, "threadid": None, "vectorstoreid": None}
    
if "userstate" not in st.session_state:
    st.session_state.userinfo = {"username": None, "password": None, "email": None, "firstname": None, "lastname": None, "fullname": None, "businessname": None, "businessaddress": None, "userrole": None, "createddate": None, "threadid": None, "vectorstoreid": None}
    if st.query_params:
        st.session_state.userstate = 4
        st.session_state.paytype = "paid"
        st.session_state.usertype = "new"
    else:
        st.session_state.userstate = 0
        st.session_state.paytype = None
        st.session_state.usertype = "guest"

elif st.session_state.userstate == 0:
    btn_new = st.button("new user")
    btn_exist = st.button("existing user")

    if btn_new:
        st.session_state.userstate = 1
        st.session_state.usertype = "new"
    
    if btn_exist:
        st.session_state.userstate = 4
        st.session_state.usertype = "existing"
        st.session_state.paytype = "paid"