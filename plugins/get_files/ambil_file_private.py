from utils import conv_flt, download_media
from pyrogram import Client, types, filters, errors
from clients import user


@Client.on_message(conv_flt("ambil_c") & filters.private)
async def get_private_file(_, m: types.Message):
    link = m.text
    await m.reply("Mencoba untuk masuk kedalam channel.")
    try:
        await user.join_chat(link)
    except errors.UserAlreadyParticipant:
        pass
    except errors.RPCError as e:
        await m.reply(
            f"Terjadi Kesalahan Internal\nError: \n{e}\nLapor ke @shohih_abdul"
        )
    await m.reply("Berhasil masuk kedalam channel.")
    await download_media(user, m, m.from_user.id)
