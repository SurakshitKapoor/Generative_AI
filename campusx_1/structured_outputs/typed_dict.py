

from langchain_ollama import ChatOllama
from typing import TypedDict, List, Annotated

class Review(TypedDict):
    keywords: Annotated[List[str], "list 5 important keywords based on the passed theme"]
    summary: str
    sentiment: Annotated[str, "choose either pos, neg, or neutral"]
    advantages: Annotated[List[str], "mention 3 advantages of passed content"]
    disadvantages: Annotated[List[str], "mention 3 disadvantages of passed content"]


model = ChatOllama(model="gemma3:1b")

structured_output = model.with_structured_output(Review, strict = True)

response = structured_output.invoke("""
The Indian education system is a blend of strong academic foundations and diverse learning pathways. 
It places heavy emphasis on theoretical knowledge, structured exams, and competitive entrance tests. 
While this approach has produced skilled professionals in fields like engineering, medicine, and technology, 
it often leaves limited space for creativity and practical learning. Over the years, reforms like the National Education 
Policy (NEP 2020) have aimed to make education more flexible, skill-oriented, and student-centric. Despite challenges 
such as unequal access and high competition, the system continues to evolve toward a more holistic and modern learning
environment.
""")

print("response of model:", response)
print()
print("type is:", type(response))
print()
print(response["summary"])
print()
print(response["keywords"])
print()
print(response["pros"])


