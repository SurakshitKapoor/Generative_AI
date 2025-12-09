

# Dynamic prompting with Streamlit + LangChain + Ollama

import streamlit as st
from langchain_core.prompts import load_prompt
from langchain_ollama import ChatOllama

# ---------------------------
# Streamlit UI
# ---------------------------
player = st.selectbox(
    'Choose your favourite cricketer',
    ["Virat Kohli", "Rohit Sharma", "KL Rahul", "Jasprit Bumrah", 
     "Ravindra Jadeja", "Hardik Pandya", "Shubman Gill", "Rishabh Pant", 
     "Mohammed Shami", "Yuzvendra Chahal"]
)

format_type = st.selectbox(
    "Select the format type:",
    ["T20", "ODI", "Test"]
)

strength = st.selectbox(
    "Select their main strength:",
    ["Batting", "Bowling", "All-rounder", "Captaincy", "Fielding"]
)


# ---------------------------
model = ChatOllama(model="gemma:2b")  

template = load_prompt("./prompts/template.json")

if st.button("Generate Summary"):
    
    prompt_text = template.format(
        player=player,
        format_type=format_type,
        strength=strength
    )
    summary = model.invoke(prompt_text)
    
    st.subheader("Cricket Summary:")
    st.write(summary.content)
