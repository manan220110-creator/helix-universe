import streamlit as st
import requests

st.set_page_config(page_title="Helix Universe", layout="centered")

st.title("Helix Universe")
st.subheader("Intelligent Answers. Visual Imagination.")

# ✅ THIS LINE IS IMPORTANT — DO NOT CHANGE THE NAME
HF_API_TOKEN = st.secrets["HF_API_TOKEN"]

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"

headers = {
    "Authorization": f"Bearer {HF_API_TOKEN}"
}

def query(prompt):
    response = requests.post(
        API_URL,
        headers=headers,
        json={"inputs": prompt}
    )
    return response.json()

user_input = st.text_input("Ask something:")

if user_input:
    with st.spinner("Thinking..."):
        result = query(user_input)

        if isinstance(result, list) and "generated_text" in result[0]:
            st.write(result[0]["generated_text"])
        else:
            st.error("AI did not return a response. Try again.")
HF_API_TOKEN = "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"


