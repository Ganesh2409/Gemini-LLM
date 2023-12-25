from dotenv import load_dotenv

load_dotenv() ## loading all the environment variables 

import streamlit as st 
import os
import google.generativeai as genai

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

### function to load gemini pro model and get response 
model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text
st.set_page_config(page_title="Q&A DEMO")

st.header("GEMINI LLM APPLICATION")
input = st.text_input("INPUT: ",key="input")
submit = st.button("ASK THE QUESTION")

if submit:
    response = get_gemini_response(input)
    st.write(response)




