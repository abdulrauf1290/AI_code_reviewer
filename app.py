import openai
from openai import OpenAI
import streamlit as st

# Read the API key and setup an OpenAI Client (assuming .env file exists)
from dotenv import dotenv_values
config =dotenv_values(".env")

client =OpenAI(api_key=config["OPENAI_API_KEY"])

from streamlit import balloons  # Import for balloons

st.snow()
st.title('🤖AI Python Code Reviewer🚀')
st.subheader("💻 Review your python code here.⚙️🛠️")

prompt = st.text_area("Enter your Code snippets...📝 ")
if st.button("Generate") == True:
    balloons()  # Display balloons
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """You are a helpful AI Assistant .
                                                 Given a python code you review the code find the bugs🐛, errors and  fix the bugs 🐛 by providing the corrected code."""},
            {"role": "user", "content": prompt},
        ]
    )

    if response.choices:
        review = response.choices[0].message.content
        st.write(review)
    else:
        st.write("❌ An error occurred during code review. Please try again.")





    
