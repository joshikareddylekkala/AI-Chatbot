import streamlit as st

st.title("Smart FAQ Chatbot 🤖")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display old messages
for msg in st.session_state.messages:
    st.write(msg)

user_input = st.text_input("You:", key="input")

def chatbot_response(question):
    question = question.lower()
    
    if "hello" in question or "hi" in question:
        return "Hello! How can I help you?"
    
    elif "ai" in question or "artificial intelligence" in question:
        return "AI stands for Artificial Intelligence. It helps machines think like humans."
    
    elif "python" in question:
        return "Python is a popular programming language used for AI and web apps."
    
    elif "internship" in question:
        return "This is my AI internship project at Code Alpha."
    
    elif "your name" in question:
        return "I am your smart chatbot assistant 🤖"
    
    elif "bye" in question:
        return "Goodbye! Have a great day 😊"
    
    else:
        return "Hmm 🤔 I am still learning. Can you ask something else?"

if st.button("Send"):
    response = chatbot_response(user_input)
    
    st.session_state.messages.append(f"You: {user_input}")
    st.session_state.messages.append(f"Bot: {response}")