from pyrogram import types, filters, Client

convs = {}
info = {}


def conv_flt(conv_level: str):
    async def func(_, __, m: types.Message):
        return convs.get(m.from_user.id) == conv_level

    return filters.create(func, "ConvFilter")


async def download_media(c: Client, m: types.Message, from_user_id: int):
    chat_id = info.get(m.from_user.id, {}).get("chat_id")
    msg_id = info.get(m.from_user.id, {}).get("msg_id")
    x = await c.get_chat(chat_id)
    msg = await c.get_messages(x.id, msg_id)
    accepted_files = ["AUDIO", "VOICE", "VIDEO", "DOCUMENT", "PHOTO"]
    if msg.media.name not in accepted_files:
        return await m.reply("File ini tidak dapat di ambil")
    text = "Downloading..."
    x = await m.reply(text)
    media = await msg.download(progress=progress_for_pyrogram, progress_args=(x, text))
    text = "Download sukses\nMengupload..."
    upload_msg = await x.reply(text)
    send_media = getattr(m, f"reply_{msg.media.value}")
    await send_media(
        media,
        progress=progress_for_pyrogram,
        progress_args=(upload_msg, text),
    )


async def progress_for_pyrogram(cur, tot, m: types.Message, text: str):
    print(f"{(cur * 100 / tot):.1f}%")
    await m.edit(f"{text}\n{(cur * 100 / tot):.1f}%")
