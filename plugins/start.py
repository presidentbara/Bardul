from pyrogram import Client, types, filters


@Client.on_message(filters.command("start"))
async def start_handler(_, m: types.Message):
    await m.reply(
        "Halo\nKlik /ambil buat ngambil file\n/daftar buat daftar\n\nBot ga gratis kecuali buat yang langganan per bulan"
    )
