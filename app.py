from flask import Flask, render_template, jsonify
import os
import random

app = Flask(__name__)

# Sample cursor features to demonstrate
CURSOR_FEATURES = [
    {
        "title": "Smart Code Completion",
        "description": "AI-powered code completion that understands context and intent",
        "icon": "🤖"
    },
    {
        "title": "Real-time Collaboration",
        "description": "Work together seamlessly with built-in collaboration features",
        "icon": "👥"
    },
    {
        "title": "Intelligent Refactoring",
        "description": "Automated code refactoring with AI assistance",
        "icon": "✨"
    },
    {
        "title": "Git Integration",
        "description": "Seamless Git operations with visual feedback",
        "icon": "🔄"
    },
    {
        "title": "Random Number Generator",
        "description": "Click to generate a random number between 47 and 101",
        "icon": "🎲",
        "link": "/random"
    },
    {
        "title": "Snake Game",
        "description": "Play the classic Snake game right in your browser",
        "icon": "🐍",
        "link": "/snake"
    }
]

@app.route('/')
def home():
    return render_template('index.html', features=CURSOR_FEATURES)

@app.route('/api/features')
def get_features():
    return jsonify(CURSOR_FEATURES)

@app.route('/random')
def random_number():
    number = random.randint(47, 101)
    return render_template('random.html', number=number)

@app.route('/snake')
def snake_game():
    return render_template('snake.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port) 