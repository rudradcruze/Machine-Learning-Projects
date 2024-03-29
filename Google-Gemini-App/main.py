import os

import streamlit as st
from streamlit_option_menu import option_menu

working_directory = os.path.dirname(os.path.abspath(__file__))

# setting up the page configuration
st.set_page_config(
    page_title="Gemini AI",
    page_icon="🧠",
    layout="centered"
)

with st.sidebar:
    selected = option_menu("Gemini AI",
                           ["ChatBot",
                            "Image Captioning",
                            "Embed Text",
                            "Ask me anything"],
                           menu_icon='robot', icons=['chat-dots-fill', 'file-earmark-image',
                                                     'textarea-t', 'patch-question-fill'],
                           default_index=0)
