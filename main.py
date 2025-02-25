from datetime import datetime

print("Hello! I'm a simple chatbot. Type 'bye' to exit.")

# Dictionary of basic responses
responses = {
    "hello": "Hi there! How can I help you?",
    "how are you": "I'm just a program, but I'm doing fine!",
    "what is your name": "I'm a chatbot created by you!",
    "bye": "Goodbye! Have a great day!",
    "default": "I'm not sure how to respond to that."
}

# Chatbot loop
while True:
    user_input = input("You: ").strip().lower()  # Clean input: remove extra spaces and convert to lowercase

    if user_input == 'bye':
        print("Chatbot:", responses["bye"])
        break

    # Handle dynamic time request
    elif 'time' in user_input:
        current_time = datetime.now().strftime("%I:%M %p")  # Fetching correct local time
        print("Chatbot: The current time is", current_time)

    # Match known responses
    elif user_input in responses:
        print("Chatbot:", responses[user_input])

    # Default response for unknown input
    else:
        print("Chatbot:", responses["default"])
