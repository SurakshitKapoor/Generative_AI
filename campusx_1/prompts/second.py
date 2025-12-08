
import streamlit as st
from langchain_ollama import ChatOllama

model = ChatOllama(model="gemma:2b")

st.header("Research Tool")

user_input = st.text_input("enter your text here...")

if st.button("Start"):
    # st.text("some random text")

    response = model.invoke(user_input)
    st.write(response.content)