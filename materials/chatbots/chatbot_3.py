
# using proper messages to set the chats in the proper format 

from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
from langchain_ollama import ChatOllama

# System message
messages = [
    SystemMessage(content="You are a tourist guide of India!")
]

model = ChatOllama(model="gemma:2b")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Chat ended.")
        break

    # Add user message
    messages.append(HumanMessage(content=user_input))

    # Get model response
    response = model.invoke(messages)

    # Print reply
    print("AI:", response.content)

    # Add AI message back to history
    messages.append(AIMessage(content=response.content))


print("done !")
print()
print("all chats: ",  messages)