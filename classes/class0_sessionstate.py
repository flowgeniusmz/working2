import streamlit as st
from dataclasses import dataclass, field
from typing import Literal, List, Dict


class SessionState:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key not in st.session_state:
                st.session_state[key] = value

    @classmethod
    def get(cls, **kwargs):
        if 'session_state_instance' not in st.session_state:
            st.session_state.session_state_instance = cls(**kwargs)
        return st.session_state.session_state_instance

    def update(self, **kwargs):
        for key, value in kwargs.items():
            st.session_state[key] = value

    def get_value(self, key):
        return st.session_state.get(key, None)
    



    # @staticmethod
    # def convert_and_get(user_session: UserSession = None, checkout_session: CheckoutSession = None):
    #     kwargs = {}
    #     if user_session:
    #         kwargs.update(vars(user_session))
    #     if checkout_session:
    #         kwargs.update(vars(checkout_session))
    #     return SessionState.get(**kwargs)

    # @staticmethod
    # def convert_and_update(user_session: UserSession = None, checkout_session: CheckoutSession = None):
    #     kwargs = {}
    #     if user_session:
    #         kwargs.update(vars(user_session))
    #     if checkout_session:
    #         kwargs.update(vars(checkout_session))
    #     session_state_instance = SessionState.get()
    #     session_state_instance.update(**kwargs)


