import streamlit as st
from classes.class0_pagesetup import PageSetup

# 1. Set ST PAGE CONFIG
st.set_page_config(page_icon=st.secrets.app.icon, page_title=st.secrets.app.title, layout=st.secrets.app.layout, initial_sidebar_state=st.secrets.app.sidebar)

# 2. Set Page Setup
pagenumber = 1
PageSetup(pagenumber=pagenumber).display_auto()
