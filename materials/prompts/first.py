from langchain_ollama import ChatOllama

model = ChatOllama(model="gemma:2b")   # or any installed Ollama model

response = model.invoke("write 5 lines of poem on cricket")
print(response)
