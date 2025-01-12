import streamlit as st
from groq import Groq

# Set page config
st.set_page_config(page_title="Llama 3.3 70b")

api_key = st.secrets["API_KEY"]

client = Groq(api_key= api_key)

def model_response(text: str):

    chat_completion = client.chat.completions.create(
        messages = [
            {
                "role": "system",
                "content": "You are a helpful assitant",
            },
            {
                "role": "user",
                "content": text
            }
        ],
        model = "llama-3.3-70b-versatile",
        stream = True
    )

    for chunk in chat_completion:
        response = chunk.choices[0].delta.content
        if response is not None:
            yield response

# Build the streamlit application
st.title("Llama 3.3 70b")
st.subheader("by Utkarsh Gaikwad")

# Add text area
text = st.text_area("Ask any question : ")

# Add a button for generate
button = st.button(label="generate", type="primary")

# Generate response if button is pressed
if button:
    st.subheader("Model Response : ")
    st.write_stream(model_response(text))
