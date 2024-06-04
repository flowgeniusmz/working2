import streamlit as st
from classes.class0_pagesetup import PageSetup
from classes.class1_payment import Payment

# 1. Set ST PAGE CONFIG
st.set_page_config(page_icon=st.secrets.app.icon, page_title=st.secrets.app.title, layout=st.secrets.app.layout, initial_sidebar_state=st.secrets.app.sidebar)

# 2. Set Page Setup
pagenumber = 0
PageSetup(pagenumber=pagenumber).display_manual()

c = st.checkbox("proceed")
if c:
    Payment().display_payment()