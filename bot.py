from pyrogram import Client, filters
import requests
import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
WEB_APP_URL = os.getenv("WEB_APP_URL")  # Heroku Web App URL

bot = Client("carrom_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.command("start"))
def start(client, message):
    message.reply_text(
        "🎱 Welcome to Carrom!\n\n"
        "🎮 /play_with_friend - Invite a friend\n"
        "🤖 /play_with_bot - Play vs bot"
    )

@bot.on_message(filters.command("play_with_friend"))
def invite_friend(client, message):
    message.reply_text("Tag a friend and ask them to reply with `/carrom [amount]` to join!")

@bot.on_message(filters.command("carrom"))
def start_match(client, message):
    parts = message.text.split()
    if len(parts) < 2:
        return message.reply_text("Usage: /carrom [amount]")
    
    amount = parts[1]
    
    # Generate a session ID
    session_id = f"{message.chat.id}_{message.from_user.id}"
    
    game_link = f"{WEB_APP_URL}/game?session_id={session_id}"
    
    message.reply_text(f"Game started! Click to play: {game_link}")

@bot.on_message(filters.command("play_with_bot"))
def play_with_bot(client, message):
    session_id = f"{message.chat.id}_bot"
    game_link = f"{WEB_APP_URL}/game?session_id={session_id}"
    
    message.reply_text(f"Game vs Bot started! Click to play: {game_link}")

bot.run()
