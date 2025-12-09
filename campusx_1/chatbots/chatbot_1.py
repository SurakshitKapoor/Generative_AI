
# chatbot with no past information -> not remember past conversations
from langchain_ollama import ChatOllama


model = ChatOllama(model="gemma:2b") 


while True:
    user_input = input("You: ")
    if user_input == "exit":
        break
    result = model.invoke(user_input)
    print("AI: ", result.content)



print("done!")
