import os

import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai

#load environment variables
load_dotenv()

#Configure Streamlit page settings
st.set_page_config(
    page_title='Chat with Gemini-Pro',
    page_icon=":brain", #Favicon option
    layout="centered", #Page layout option
)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

#set up Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
#loading
model = gen_ai.GenerativeModel("gemini-pro")


#function to translate roles between Gemini-Pro and Streamlit terminology
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role

# Initialize chart session in Streamlit if not already present
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

#Display the chatbot's title on the page
st.title("🎃 Gemini Pro - ChatBot")

#display the chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# Inputs field for user's messsage
user_prompt = st.chat_input("Ask Gemini-Pro...")
if user_prompt:
    #add user's messgae to chart and display
    st.chat_message('user').markdown(user_prompt)

    #Send user's message to Gemini-Pro and get the response
    gemini_response = st.session_state.chat_session.send_message(user_prompt)

    #display Gemini-Pros response
    with st.chat_message('assistant'):
        st.markdown(gemini_response.text)




