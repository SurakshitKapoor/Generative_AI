
# building a reusable prompt template in json form

from langchain_core.prompts import PromptTemplate

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

template.save("./prompts/template.json")