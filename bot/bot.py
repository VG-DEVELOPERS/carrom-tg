from pyrogram import Client, filters
import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
WEB_APP_URL = os.getenv("WEB_APP_URL")

bot = Client("carrom_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.command("start"))
def start(client, message):
    message.reply_text(
        "🎱 Welcome to Carrom Mini App!\n"
        "🎮 /play_with_friend - Invite a friend\n"
        "🤖 /play_with_bot - Play vs bot\n"
        "ℹ️ /help - Learn how to play"
    )

@bot.on_message(filters.command("play_with_friend"))
def play_with_friend(client, message):
    game_link = f"{WEB_APP_URL}/game"
    message.reply_text(f"🎮 Click to play: {game_link}", reply_markup=InlineKeyboardMarkup(
        [[InlineKeyboardButton("Play Now", web_app=WebAppInfo(url=game_link))]]
    ))

@bot.on_message(filters.command("play_with_bot"))
def play_with_bot(client, message):
    game_link = f"{WEB_APP_URL}/game?mode=bot"
    message.reply_text(f"🤖 Click to play: {game_link}", reply_markup=InlineKeyboardMarkup(
        [[InlineKeyboardButton("Play Now", web_app=WebAppInfo(url=game_link))]]
    ))

bot.run()
