

from pydantic import BaseModel, Field
from typing import List, Annotated
from langchain_ollama import ChatOllama

# ---------- Pydantic Schema ----------
class Review(BaseModel):
    keywords: List[str] = Field(..., description="list 5 important keywords based on theme")
    summary: str
    sentiment: str = Field(..., description="pos, neg, or neutral")
    advantages: List[str] = Field(..., description="3 pros")
    disadvantages: List[str] = Field(..., description="3 cons")

# ---------- LLM with structured output ----------
llm = ChatOllama(model="gemma:2b")
structured_llm = llm.with_structured_output(Review)

# ---------- Query ----------
response = structured_llm.invoke("""
The Indian education system focuses heavily on theoretical learning...
""")

print(response)
print(type(response))
