
# creating a list to store all conversations

from langchain_ollama import ChatOllama


model = ChatOllama(model="gemma:2b") 

all_chats = []

while True:
    user_input = input("You: ")
    all_chats.append(user_input)

    if user_input == "exit":
        break

    result = model.invoke(all_chats)
    all_chats.append(result.content)

    print("AI: ", result.content)



print("done!")
