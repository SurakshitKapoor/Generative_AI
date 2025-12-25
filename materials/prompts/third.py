
# Dynamic prompting with Streamlit + LangChain + Ollama

import streamlit as st
from langchain_core.prompts import PromptTemplate
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
# PromptTemplate creation
# ---------------------------
template = PromptTemplate(
    template=(
        "Summarize the career of {player}, an Indian cricketer, "
        "in {format_type} matches. Highlight their main strength: {strength}. "
        "Keep the summary short, accurate, and limited to 5 lines. "
        "Do not hallucinate or make up statistics."
    ),
    input_variables=['player', 'format_type', 'strength'],
)

# ---------------------------
# LangChain + Ollama
# ---------------------------
llm = ChatOllama(model="gemma:2b")  # Ensure the model is installed

if st.button("Generate Summary"):
    prompt_text = template.format(
        player=player,
        format_type=format_type,
        strength=strength
    )
    summary = llm.invoke(prompt_text)
    
    st.subheader("Cricket Summary:")
    st.write(summary.content)
