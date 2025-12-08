
from langchain_ollama import OllamaLLM

model = OllamaLLM(model="gemma:2b")


# response = model.invoke("Say hello! can you assist me in AI and ML?")
response = model.invoke("write a 5 lines of poem on cricket")
print(response)