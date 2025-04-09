from flask import Flask, request, jsonify, render_template
from services.chatbot_service import process_message  # Import the process_message function

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")  # Get the user's message from the request
    if not user_message:
        return jsonify({"response": "Please enter a message."})  # Handle empty messages

    # Use process_message to dynamically generate a response
    bot_response = process_message(user_message)
    return jsonify({"response": bot_response})  # Return the bot's response as JSON

if __name__ == "__main__":
    app.run(debug=True)