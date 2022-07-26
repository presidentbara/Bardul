from configs import configs
from utils import convs
from pyrogram import Client, types, filters


@Client.on_message(filters.command("ambil") & filters.private)
async def ambil_handler(_, m: types.Message):
    if configs.owner_id == m.from_user.id:
        convs[m.from_user.id] = "ambil"
        return await m.reply("Silakan kirim link media telegram yang ingin di ambil")
    return await m.reply("Maaf, anda tidak memiliki izin untuk menggunakannya")
