import streamlit as st
from streamlit_extras.stylable_container import stylable_container as sc
from typing import Literal

class PageSetup:
    def __init__(self, pagenumber: int):
        self.page = pagenumber
        self.initialize()

    def initialize(self):
        self._initialize_page_attributes()
        self._initialize_styles()
        self._initialize_page_style()

    def display_auto(self):
        self._display_header_auto()
        self._display_overview()
    
    def display_manual(self):
        self._display_header_manual(divider="True", title="SpartakusAI", subtitle= "Welcome")

    def _initialize_page_attributes(self):
        self.title = st.secrets.pages.titles[self.page]
        self.subtitle = st.secrets.pages.subtitles[self.page]
        self.icon = st.secrets.pages.icons[self.page]
        self.description = st.secrets.pages.descriptions[self.page]
        self.about = st.secrets.pages.abouts[self.page]
        self.header = st.secrets.pages.headers[self.page]
        self.path = st.secrets.pages.paths[self.page]
        self.count = st.secrets.pages.count
        self.countoffset = self.count - 1
        self.stylepath = "config/style.css"

    def _initialize_styles(self):
        self.style1 = "{border: 2px solid rgba(40, 94, 159, 0.75); background-color: rgba(255, 255, 255, 0.75); border-radius: 0.5rem; padding: 1em; overflow: hidden; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2); transition: 0.3s; box-sizing: border-box;}"
        self.style2 = "{border: 2px solid rgba(0, 0, 0, 0.2); background-color: rgba(40, 94, 159, 0.75); border-radius: 0.5rem; padding: 1em; overflow: hidden; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2); transition: 0.3s; box-sizing: border-box;}"

    def _initialize_page_style(self):
        with open(self.stylepath) as css:
            self.pagestyle = st.markdown(f'<style>{css.read()}</style>' , unsafe_allow_html= True)

    def _display_header_auto(self, divider: bool=True):
        headercols = st.columns([10,2])
        with headercols[0]:
            self._display_header_title(type="auto")
        with headercols[1]:
            self._display_header_popmenu()
        if divider:
            st.divider()

    def _display_header_manual(self, divider: bool=True, title: str=None, subtitle: str=None):
        self.title_display = st.markdown(f"""<span style="font-weight: bold; font-size: 2em; color:#285E9F;">{title} </span> <span style="font-weight: bold; color:#4A90E2; font-size:1.3em;">{subtitle}</span>""", unsafe_allow_html=True)
        if divider:
            st.divider()

    def _display_header_title(self, type: Literal["auto", "manual"], title: str=None, subtitle: str=None):
        if type == "auto":
            self.title_display = st.markdown(f"""<span style="font-weight: bold; font-size: 2em; color:#285E9F;">{self.title} </span> <span style="font-weight: bold; color:#4A90E2; font-size:1.3em;">{self.subtitle}</span>""", unsafe_allow_html=True)
        elif type == "manual":
            self.title_display = st.markdown(f"""<span style="font-weight: bold; font-size: 2em; color:#285E9F;">{title} </span> <span style="font-weight: bold; color:#4A90E2; font-size:1.3em;">{subtitle}</span>""", unsafe_allow_html=True)

    def _display_header_popmenu(self):
        self.menu_display = st.popover(label="🧭 Menu", disabled=False, use_container_width=True)
        with self.menu_display:
            for i in range(self.count):
                st.page_link(page=st.secrets.pages.paths[i], label=st.secrets.pages.subtitles[i], disabled=(self.page == i))

    def _display_overview(self):
        self.get_styled_header(type="gray", text=self.header)
        st.markdown(body=self.description)
        st.divider()
    
    def get_styled_container(self, height: int = None, border: bool=False):
        outerstyle = sc(key="outercontainer", css_styles=self.style2)
        with outerstyle:
            innerstyle = sc(key="innercontainer", css_styles=self.style1)
            with innerstyle:
                if height is not None:
                    container = st.container(height=height, border=border)
                else:
                    container = st.container(border=border)
        return container

    def get_styled_header(self, type: Literal["gray", "green", "blue"], text: str):
        if type == "blue":
            self.header_display = st.markdown(f"""<span style="font-weight: bold; color:#4A90E2; font-size:1.3em;">{text}</span>""", unsafe_allow_html=True)
        elif type == "gray":
            self.header_display = st.markdown(f"""<span style="font-weight: bold; color:#333333; font-size:1.3em;">{text}</span>""", unsafe_allow_html=True)
        elif type == "green": 
            self.header_display = st.markdown(f"""<span style="font-weight: bold; color:#00b084; font-size:1.3em;">{text}</span>""", unsafe_allow_html=True)

    
       

