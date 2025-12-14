import streamlit as st

st.set_page_config(page_title="Helix Universe", layout="centered")

st.title("Helix Universe")
st.subheader("Intelligent Answers. Visual Imagination.")

user_input = st.text_input("Ask something:")

if user_input:
    st.write("You asked:", user_input)
    st.write("AI response will appear here.")

