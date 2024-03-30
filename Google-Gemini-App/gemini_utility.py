import os
import json
import google.generativeai as genai

# get the working directory
working_directory = os.path.dirname(os.path.realpath(__file__))

config_file_path = f"{working_directory}/config.json"
config_data = json.load(open(config_file_path))

# loading the api key
GOOGLE_API_KEY = config_data["GOOGLE_API_KEY"]

# configuring google.generativeai with api key
genai.configure(api_key=GOOGLE_API_KEY)


# function to load gemini-pro-model for chatbot
def load_gemini_pro_model():
    gemini_pro_model = genai.GenerativeModel("gemini-pro")
    return gemini_pro_model


# function for image captioning
def gemini_pro_vision_response(prompt, image):
    gemini_pro_vision_model = genai.GenerativeModel("gemini-pro-vision")
    response = gemini_pro_vision_model.generate_content([prompt, image])
    result = response.text
    return result
