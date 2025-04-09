import requests
import random as rd
from models.ior_model import recognize_object

# Global variable for quiz state
current_quiz = {"question": None, "answer": None}

# Main message processing function
def process_message(message):
    global current_quiz
    message = message.lower().strip()

    if current_quiz and current_quiz.get("question"):
        return check_quiz_answer(message)
    
    # Personalized responses
    if "your name" in message:
        return "I'm your friendly chatbot! You can call me ChatBot 🤖."
    elif "what can you do" in message:
        return "I can tell jokes, share facts, start quizzes, recognize objects, and chat with you!"
    elif "how are you" in message:
        return "I'm just a bot, but I'm doing great! Thanks for asking 😊. How can I help you today?"
    elif "thank you" in message or "thanks" in message:
        return "You're welcome! 😊 Let me know if there's anything else I can do for you."

    # Handle greetings
    if "hello" in message or "hi" in message or "hola" in message:
        return "Hello! 👋 How can I assist you today?"

    # Handle farewells
    if "bye" in message or "goodbye" in message or "adios" in message:
        return "Goodbye! 👋 Have a great day!"

    if "recognize" in message:
        return recognize_object(message)
    elif "joke" in message:
        return fetch_joke()
    elif "fact" in message:
        return get_enviroment_fact()
    elif "quiz" in message:
        return start_quiz()
    else:
        return "I'm not sure how to respond to that."

# Functions related to jokes
def fetch_joke():
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        if response.status_code == 200:
            joke_data = response.json()
            return f"{joke_data['setup']} ... {joke_data['punchline']}"
        else:
            return "Couldn't fetch a joke."
    except Exception as e:
        return "Error fetching joke."

# Functions related to facts
def get_enviroment_fact():
    facts = [
        "The Amazon rainforest produces more than 20% of the world's oxygen.",
        "Coral reefs support about 25% of all marine life.",
        "The Sahara Desert is larger than the entire United States.",
        "The Great Barrier Reef is the largest living structure on Earth.",
        "Oceans cover about 71% of the Earth's surface.",
        "Plastic pollution is a major threat to marine life.",
        "Climate change is causing sea levels to rise.",
        "Deforestation is a leading cause of climate change.",
        "Overfishing is depleting fish populations worldwide.",
    ]
    return rd.choice(facts)

# Functions related to quizzes
def start_quiz():
    global current_quiz
    quiz_questions = [
        {"question": "True or False: The Amazon rainforest produces 20% of the world's oxygen.", "answer": "true"},
        {"question": "What is the largest living structure on Earth?", "answer": "the great barrier reef"},
        {"question": "True or False: Coral reefs are found in freshwater.", "answer": "false"},
        {"question": "What is the largest desert in the world?", "answer": "the sahara desert"},
        {"question": "True or False: Oceans cover about 71% of the Earth's surface.", "answer": "true"},
        {"question": "What is a major threat to marine life?", "answer": "plastic pollution"},
        {"question": "True or False: Climate change is causing sea levels to rise.", "answer": "true"},
        {"question": "What is a leading cause of climate change?", "answer": "deforestation"},
        {"question": "True or False: Overfishing is depleting fish populations worldwide.", "answer": "true"},
    ]
    current_quiz = rd.choice(quiz_questions)
    return current_quiz["question"]

def check_quiz_answer(user_answer):
    global current_quiz
    if not current_quiz or not current_quiz.get("question"):
        return "There is no active quiz. Type 'quiz' to start one!"

    user_answer = user_answer.lower().strip()
    correct_answer = current_quiz["answer"].lower().strip()

    if user_answer == correct_answer:
        response = "Correct! 🎉 Great job!"
    else:
        response = f"That's not correct. The correct answer was: {correct_answer.capitalize()}."

    current_quiz = {"question": None, "answer": None}  # Reset quiz state
    return response

# Global variable for quiz state
current_quiz = {"question": None, "answer": None}

# Function to reset the chatbot
def reset_chatbot():
    global current_quiz
    current_quiz = {"question": None, "answer": None}  # Reset the quiz state
    print("Chatbot has been reset.")  # Optional: Log the reset action