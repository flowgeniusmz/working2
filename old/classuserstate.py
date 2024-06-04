import streamlit as st
from openai import OpenAI
from supabase import create_client
from streamlit_extras.stylable_container import stylable_container as sc
from typing import Literal
import stripe
import time
import json

class UserStateManager:
    def __init__(self):
        self.initialize()

    def initialize(self):
        self.userstate = st.session_state.userstate


class UserState_0_Render:
    def __init__(self):
        self.display()

    def display(self):
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
            body_container2 = self.styled_container(border=False)
            with body_container2:
                body_cols = st.columns([1, 20, 1, 20, 1])
                with body_cols[1]:
                    existuserbutton1 = st.button("Sign In", type="primary", key="existuserbutton1", use_container_width=True)
                with body_cols[3]:
                    newuserbutton1 = st.button("Join Now", type="primary", key="newuserbutton1", use_container_width=True)
        st.divider()
        asst_container = st.container(border=False)
        with asst_container:
            self.chat_container = self.styled_container(border=False, height=250)
            with self.chat_container:
                for guestmessage in st.session_state.guestthreadmessages:
                    with st.chat_message(name=guestmessage.role):
                        st.markdown(body=guestmessage.content[0].text.value)
            self.prompt_container = st.container(border=False)
            with self.prompt_container:
                self.guestprompt = st.chat_input(placeholder="Chat with Sparty here...", key="guestchatprompt")
        st.divider()

    def styled_container(self, border: bool=False, height: int=None):
        style1 = "{border: 2px solid rgba(40, 94, 159, 0.75); background-color: rgba(255, 255, 255, 0.75); border-radius: 0.5rem; padding: 1em; overflow: hidden; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2); transition: 0.3s; box-sizing: border-box;}"
        style2 = "{border: 2px solid rgba(0, 0, 0, 0.2); background-color: rgba(40, 94, 159, 0.75); border-radius: 0.5rem; padding: 1em; overflow: hidden; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2); transition: 0.3s; box-sizing: border-box;}"
        sc_outer = sc(key="adfadfadfadfdfaadfa", css_styles=style2)
        with sc_outer:
            sc_inner = sc(key="adsfd", css_styles=style1)
            with sc_inner:
                if height is not None:
                    container = st.container(height=height, border=border)
                else:
                    container = st.container(border=border)
        return container
    
    