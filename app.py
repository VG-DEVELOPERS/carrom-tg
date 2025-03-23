from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
import os
import requests

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

BOT_TOKEN = os.getenv("BOT_TOKEN")

@app.route("/")
def home():
    return "Carrom Mini App is Running!"

@socketio.on("strike")
def handle_strike(data):
    emit("update_board", data, broadcast=True)  # Broadcast striker movement

@app.route("/result", methods=["POST"])
def game_result():
    data = request.json
    winner = data["winner"]
    chat_id = data["chat_id"]

    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        json={"chat_id": chat_id, "text": f"🏆 Game Over! Winner: {winner}"}
    )
    return jsonify({"status": "success"})

if __name__ == "__main__":
    socketio.run(app, debug=True, port=5000)
    
