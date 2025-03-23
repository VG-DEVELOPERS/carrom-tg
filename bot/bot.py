from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
WEB_APP_URL = os.getenv("WEB_APP_URL")  # Your Heroku app URL

bot = Client("carrom_bot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

@bot.on_message(filters.command("start"))
def start(_, message):
    message.reply_text(
        "🎯 Welcome to Carrom Game! Choose an option:",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Play with Friend", callback_data="play_friend")],
            [InlineKeyboardButton("Play with Bot", callback_data="play_bot")]
        ])
    )

@bot.on_callback_query()
def callback(_, query):
    if query.data == "play_friend":
        game_link = f"{WEB_APP_URL}/game?mode=friend"
    elif query.data == "play_bot":
        game_link = f"{WEB_APP_URL}/game?mode=bot"

    query.message.reply_text(
        f"🎮 Click below to play:\n{game_link}",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Play Now", web_app={"url": game_link})]
        ])
    )

bot.run()
