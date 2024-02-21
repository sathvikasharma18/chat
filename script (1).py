def simple_chatbot(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a chatbot, but I'm here to help you!"
    elif "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    elif "thank you" in user_input:
        return "You're welcome! If you need further assistance, feel free to ask."
    else:
        return "I'm sorry, I didn't understand that. Could you please rephrase or ask something else?"

print("Welcome to the Simple Chatbot. Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = simple_chatbot(user_input)
    print("Chatbot:", response)
