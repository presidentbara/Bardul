from configs import configs
from pyrogram import Client

user = Client(
    name="user", api_id=configs.api_id, api_hash=configs.api_hash, session_string=configs.session_name, in_memory=True
)

bot = Client(
    name="bot",
    api_id=configs.api_id,
    api_hash=configs.api_hash,
    bot_token=configs.bot_token,
    in_memory=True,
    plugins={
        "root": "plugins",
    },
)
