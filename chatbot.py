import streamlit as st

# Define the function to handle user input and generate responses
def get_bot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        return "Hello! How can I assist you with your healthcare needs today?"

    # Responses related to common diseases
    elif "fever" in user_input:
        return ("Fever can be caused by various factors such as infections. "
                "It's important to stay hydrated and rest. Over-the-counter medications like acetaminophen or ibuprofen "
                "can help reduce fever. If the fever persists or is very high, please consult a healthcare professional.")

    elif "headache" in user_input:
        return ("Headaches can be caused by stress, dehydration, or other factors. "
                "Make sure to drink water and rest in a quiet, dark room. Over-the-counter pain relievers like ibuprofen or "
                "acetaminophen can help. If the headache is severe, frequent, or persistent, consider seeing a doctor.")

    elif "cough" in user_input:
        return ("A cough could be due to a cold, allergies, or respiratory infections. "
                "Stay hydrated, use cough drops, and consider a humidifier. If the cough is persistent or accompanied by "
                "other symptoms like fever, seek medical advice.")

    elif "covid" in user_input or "coronavirus" in user_input:
        return ("If you're experiencing symptoms related to COVID-19, such as fever, cough, or loss of taste and smell, "
                "it's important to get tested and isolate yourself to prevent spreading the virus. Follow guidelines provided "
                "by health authorities, and seek medical attention if symptoms worsen.")

    elif "diabetes" in user_input:
        return ("Diabetes is a chronic condition that affects how your body processes blood sugar (glucose). "
                "Managing diabetes involves regular monitoring of blood sugar levels, following a healthy diet, staying active, "
                "and taking prescribed medications or insulin. Preventive measures include maintaining a healthy weight, eating "
                "a balanced diet, and regular physical activity.")

    elif "hypertension" in user_input or "high blood pressure" in user_input:
        return ("Hypertension, or high blood pressure, increases the risk of heart disease and stroke. "
                "Treatment includes lifestyle changes such as reducing salt intake, eating a balanced diet, exercising regularly, "
                "and taking prescribed medications. Regular monitoring of blood pressure is essential.")

    elif "asthma" in user_input:
        return ("Asthma is a condition in which your airways narrow and swell, making breathing difficult. "
                "Treatment involves avoiding triggers, using inhalers, and taking prescribed medications. "
                "It's important to follow your asthma action plan and seek emergency care if symptoms worsen.")

    elif "malaria" in user_input:
        return ("Malaria is a mosquito-borne disease caused by parasites. Symptoms include fever, chills, and flu-like illness. "
                "Prevention involves using mosquito nets, repellents, and antimalarial drugs when traveling to high-risk areas. "
                "Treatment typically includes antimalarial medications prescribed by a healthcare provider.")

    elif "flu" in user_input or "influenza" in user_input:
        return ("Influenza, or the flu, is a contagious respiratory illness caused by influenza viruses. "
                "Prevention includes annual flu vaccination, frequent handwashing, and avoiding close contact with sick individuals. "
                "Treatment involves rest, hydration, and over-the-counter medications to relieve symptoms. Antiviral drugs may be prescribed.")

    elif "common cold" in user_input:
        return ("The common cold is a viral infection of the upper respiratory tract. Symptoms include a runny nose, sore throat, and cough. "
                "Prevention includes frequent handwashing and avoiding close contact with infected individuals. Treatment focuses on relieving symptoms "
                "through rest, hydration, and over-the-counter medications.")

    elif "thank you" in user_input or "thanks" in user_input:
        return "You're welcome! Feel free to ask if you have any other questions."

    else:
        return "I'm not sure how to respond to that. Could you please provide more details or ask a different question?"

# Streamlit app
st.title("🤖 Simple Healthcare Chatbot")
st.write("Welcome! Ask me anything related to healthcare, and I'll do my best to assist you.")

# Sidebar for interaction
st.sidebar.title("💬 Interaction Options")
st.sidebar.write("Select a topic or ask a specific question.")

# Predefined questions to guide the user
predefined_questions = [
    "Tell me about fever.",
    "What should I do for a headache?",
    "How can I treat a cough?",
    "What are the symptoms of COVID-19?",
    "How to manage diabetes?",
    "What are the treatments for high blood pressure?",
    "Tell me about asthma.",
    "How to prevent malaria?",
    "What is the flu, and how can I treat it?",
    "What are the symptoms and treatment of the common cold?"
]

# Dropdown menu for predefined questions
selected_question = st.sidebar.selectbox("Select a common question", predefined_questions)

# Display the question if selected
if selected_question:
    st.write(f"**You asked:** {selected_question}")
    response = get_bot_response(selected_question)
    st.write(f"**Bot:** {response}")

# Text input for custom questions
user_input = st.text_input("Or type your own question here:")

# Button to submit the custom question
if st.button("Ask the Bot"):
    if user_input:
        response = get_bot_response(user_input)
        st.write(f"**Bot:** {response}")
    else:
        st.write("Please enter a question!")

# Expandable section for more information
with st.expander("ℹ️ About this chatbot"):
    st.write("""
        This simple healthcare chatbot is designed to provide general information about common health conditions.
        Please note that this bot is not a substitute for professional medical advice, diagnosis, or treatment.
        Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.
    """)
