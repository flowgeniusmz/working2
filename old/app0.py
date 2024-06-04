import streamlit as st
import stripe
from supabase import create_client
from openai import OpenAI
from streamlit_extras.stylable_container import stylable_container as sc
from config import pagesetup as ps
from typing import Literal

# 1. Set 'st.set_page_config' (NOTE: Must be first streamlit call in app)
st.set_page_config(page_icon=st.secrets.appconfig.app_icon, page_title=st.secrets.appconfig.app_name, layout=st.secrets.appconfig.app_layout, initial_sidebar_state=st.secrets.appconfig.app_initial_sidebar)

# 2. Set page styling
with open("config/style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

# 3. Set background image
background_image = "http://www.spartakusai.com/main.png"
st.markdown(f"""<style>.stApp {{background-image: linear-gradient(rgba(255, 255, 255, 0.7), rgba(255, 255, 255, 0.95)), url({background_image});background-size: cover; /* Make sure the image covers the entire background */background-repeat: no-repeat; /* Do not repeat the image */background-attachment: fixed; /* Make sure the image is fixed on the screen */background-position: center; /* Center the image */}}</style>""",unsafe_allow_html=True)

# 4. Set Header Container
header_container = st.container(border=False)
with header_container:
    header_cols = st.columns([1, 20, 1, 2, 1])
    with header_cols[1]:
        title = "SpartakusAI"
        subtitle = "Welcome"
        st.markdown(f"""<span style="font-weight: bold; font-size: 2em; color:#4A90E2;">{title} </span> <span style="font-weight: bold; color:#333333; font-size:1.3em;">{subtitle}</span>""", unsafe_allow_html=True)
    with header_cols[3]:
        usertype_pop = st.popover(label="Sign In or Join Now", disabled=False,  use_container_width=True)
        with usertype_pop:
            newuserbutton2 = st.button("Join Now", type="primary")
            existuserbutton2 = st.button("Sign In", type="primary")
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
                    existuserbutton1 = st.button("Sign In", type="primary")
                with body_cols[3]:
                    newuserbutton1 = st.button("Join Now", type="primary")
if newuserbutton1 or newuserbutton2:
    st.session_state.usertype = "new"
if existuserbutton1 or existuserbutton2:
    st.session_state.usertype = "existing"