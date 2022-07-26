from os import environ

from dotenv import load_dotenv
from pyrogram import types

load_dotenv()
btn = types.InlineKeyboardButton
markup = types.InlineKeyboardMarkup


class Configs:
    api_id = environ.get("API_ID")
    api_hash = environ.get("API_HASH")
    bot_token = environ.get("BOT_TOKEN")
    session_name = environ.get("SESSION_NAME") or "session"
    if owner_id := environ.get("OWNER_ID"):
        owner_id = int(owner_id)


configs = Configs()
