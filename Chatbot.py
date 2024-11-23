import streamlit as st
from datetime import datetime
import random

# Title and description of the app
st.title("Simple Streamlit Chatbot")
st.write("Welcome! This is a basic chatbot built with Streamlit. Type your message below and chat with me!")

# Define simple responses
responses = {
    "hello": ["Hello! How can I help you today?", "Hi there! How's it going?", "Hey! What's up?"],
    "how are you": ["I'm just a chatbot, but thanks for asking!", "Doing great, thanks!", "I'm here to assist you!"],
    "bye": ["Goodbye! Have a great day!", "See you later!", "Take care!"],
    "default": ["I'm not sure I understand. Can you rephrase?", "Can you provide more details?", "I'm here to help, but I didn't get that."]
}

# Function to get a response based on user input
def get_response(user_input):
    user_input = user_input.lower()
    for key in responses.keys():
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])

# Initialize session state for storing chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Text input for user message
user_input = st.text_input("You:", "", key="user_input_key")

# Display chat history
for chat in st.session_state.history:
    st.write(f"{chat['time']} - *{chat['sender']}*: {chat['message']}")

# Respond to user input
if st.button("Send") and user_input:
    # Add user input to chat history
    st.session_state.history.append({"sender": "You", "message": user_input, "time": datetime.now().strftime("%H:%M")})
    
    # Get the chatbot's response
    bot_response = get_response(user_input)
    
    # Add bot response to chat history
    st.session_state.history.append({"sender": "Bot", "message": bot_response, "time": datetime.now().strftime("%H:%M")})
    
    # Clear the input box by updating the widget’s key
    st.text_input("You:", "", key="new_key")  # Reset with a new key to clear the input box