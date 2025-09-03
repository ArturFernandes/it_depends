# app.py
from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    """Serves the main HTML page for the chat interface."""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Handles incoming chat messages and always responds with 'it depends'."""
    user_message = request.json.get('message')
    print(f"Received message: {user_message}")
    
    AI_POSSIBLE_RESPONSES = [
        "It depends.",
        "It depends on the context.",
        "It depends on various factors.",
        "It depends on your perspective.",
        "It depends on the situation.",
        "It depends on what you mean by that.",
        "It depends on how you look at it.",
        "It depends on the circumstances.",
        "It depends on the details.",
    ]

    return jsonify({'response': random.choice(AI_POSSIBLE_RESPONSES)})

if __name__ == '__main__':
    app.run(debug=True)
