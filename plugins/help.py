from pyrogram import Client, types, filters
from configs import configs


@Client.on_message(filters.command("help"))
async def help_msg(_, m: types.Message):
    text = f"""
Berikut ini adalah beberapa bantuan yang dapat digunakan:
/help - Menampilkan bantuan ini
/start - Menampilkan pesan awal

**Made With Love By [Owner](tg://user?id={configs.owner_id}) 💗**
    """
    await m.reply(text)
