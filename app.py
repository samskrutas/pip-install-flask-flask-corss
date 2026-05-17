from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows your HTML page to talk to Python

# Shared data storage
leaderboard = []

@app.route('/scores', methods=['GET', 'POST'])
def handle_scores():
    if request.method == 'POST':
        data = request.json
        leaderboard.append({"name": data['name'], "score": data['score']})
        # Sort leaderboard so the lowest number of attempts is first
        leaderboard.sort(key=lambda x: x['score'])
        return jsonify({"status": "success", "leaderboard": leaderboard[:5]})
    
    return jsonify({"leaderboard": leaderboard[:5]})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
