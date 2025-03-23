from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
import os
import requests

app = Flask(__name__, template_folder="templates")
socketio = SocketIO(app, cors_allowed_origins="*")

BOT_TOKEN = os.getenv("BOT_TOKEN")

@app.route("/")
def home():
    return "Carrom Game Server Running!"

@app.route("/game")
def game():
    return render_template("game.html")

@socketio.on("strike")
def handle_strike(data):
    emit("update_striker", data, broadcast=True)

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
    
