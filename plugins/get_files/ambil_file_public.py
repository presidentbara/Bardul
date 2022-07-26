import re

from pyrogram import Client, filters, types, errors
from pyrogram.enums import MessageEntityType

from clients import user
from plugins.bypasser.bypass_bot import bypass_bot
from utils import convs, info, download_media


@Client.on_message(filters.regex('https') & filters.private)
async def get_public_file(c: Client, m: types.Message):
    if not m.entities or m.entities[0].type != MessageEntityType.URL:
        return
    url = m.text
    if match := re.search(r"https://t.me/([^/]+)/(\d+)/?(\d+)?", url):
        if match[1] == "c":
            convs[m.from_user.id] = "ambil_c"
            info[m.from_user.id] = {
                "chat_id": int(f"-100{match[2]}"),
                "msg_id": int(match[3]),
            }
            try:
                await user.get_chat(int(f"-100{match[2]}"))
                return await download_media(user, m, m.from_user.id)
            except errors.RPCError:
                return await m.reply(
                    "Berikan link grup/channel private nya\nKlik /cancel jika ingin membatalkan"
                )
        info[m.from_user.id] = {
            "chat_id": int(match[1]) if isinstance(match[1], int) else match[1],
            "msg_id": int(match[2]),
        }
        return await download_media(c, m, m.from_user.id)
    if match := re.search(
        r"^(?:https?://)?(?:www\.)?t(?:elegram)?\.(?:org|me|dog)/([\w\d_]+)\?start=([\d\w_]+)$",
        url,
    ):
        usn = match[1]
        query = match[2]
        return await bypass_bot(usn, query, m.from_user.id)
