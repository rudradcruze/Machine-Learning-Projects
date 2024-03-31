import os

from PIL import Image
import streamlit as st
from streamlit_option_menu import option_menu

from gemini_utility import (load_gemini_pro_model,
                            gemini_pro_vision_response,
                            embedding_model_response)

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
                            "Image Description",
                            "Embed Text",
                            "Ask me anything"],
                           menu_icon='robot', icons=['chat-dots-fill', 'file-earmark-image',
                                                     'textarea-t', 'patch-question-fill'],
                           default_index=0)


# function to translate role between gemini-pro and streamlit terminology
def translate_role_for_streamlit(user_role):
    if user_role == 'model':
        return "assistant"
    else:
        return user_role


if selected == 'ChatBot':
    model = load_gemini_pro_model()

    # Initialize chat session in streamlit if not already present
    if "chat_session" not in st.session_state:
        st.session_state.chat_session = model.start_chat(history=[])

    # streamlit page title
    st.title("🤖 ChatBot")

    # display the chat history
    for message in st.session_state.chat_session.history:
        with st.chat_message(translate_role_for_streamlit(message.role)):
            st.markdown(message.parts[0].text)

    # input filed for user's message
    user_prompt = st.chat_input("Ask Gemini-Pro...")

    if user_prompt:
        st.chat_message("user").markdown(user_prompt)

        gemini_response = st.session_state.chat_session.send_message(user_prompt)

        # display gemini-pro response
        with st.chat_message("assistant"):
            st.markdown(gemini_response.text)

if selected == 'Image Description':
    # streamlit page title
    st.title("📷 Image Description")

    updated_image = st.file_uploader("Upload an image...", type=["png", "jpg", "jpeg"])

    if st.button("Get Description"):
        image = Image.open(updated_image)
        col1, col2 = st.columns(2)

        with col1:
            resize_image = image.resize((800, 500))
            st.image(resize_image)

        default_prompt = ("Generate a short caption for the image provided above. The caption should capture the "
                          "essence of the scene and include relevant details such as objects, actions, and emotions "
                          "depicted in the image.")

        caption = gemini_pro_vision_response(default_prompt, image)

        with col2:
            st.info(caption)

if selected == 'Embed Text':
    st.title("🔠 Embed Text")

    # input text box
    input_text = st.text_area(label="", placeholder="Enter the text to get the embeddings")

    if st.button("Get Embeddings"):
        response = embedding_model_response(input_text)
        st.markdown(response)

