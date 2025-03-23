from flask import Flask, request, jsonify
import os
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Flask(__name__)

@app.route("/")
def home():
    return "Carrom Mini App is running!"

@app.route("/game")
def serve_game():
    return open("web/index.html").read()

@app.route("/result", methods=["POST"])
def handle_result():
    data = request.json
    session_id = data["session_id"]
    winner = data["winner"]

    # Send result back to Telegram bot
    chat_id = session_id.split("_")[0]
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        json={"chat_id": chat_id, "text": f"Game over! Winner: {winner}"}
    )

    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(port=5000)
  
