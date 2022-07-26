import random
import asyncio
from pyrogram import filters, types
from pyrogram.raw.functions.messages import StartBot
from pyrogram.raw.types import InputUser
from clients import user, bot
import re


async def bypass_bot(bot_username: str, deep_link_query: str, user_id: int):
    bot_url = f"https://t.me/{bot_username}?start={deep_link_query}"
    bot_peer = await user.resolve_peer(bot_username)
    await user.invoke(
        StartBot(
            bot=InputUser(user_id=bot_peer.user_id, access_hash=bot_peer.access_hash),
            peer=bot_peer,
            random_id=random.randint(0, 2 ** 46),
            start_param=deep_link_query,
        )
    )

    @user.on_message(filters.user(bot_username) & filters.incoming)
    async def get_last_msg(_, m: types.Message):
        if m.reply_markup and m.reply_markup.inline_keyboard:
            keyboards = m.reply_markup.inline_keyboard
            for keyboard in keyboards:
                for keybord in keyboard:
                    if keybord.url == bot_url:
                        continue
                    await asyncio.sleep(3)
                    await user.join_chat(keybord.url)
            return await bypass_bot(bot_username, deep_link_query, user_id)
        if m.media:
            media = await m.download()
            send_media = getattr(bot, f"send_{m.media.value}")
            kwargs = {
                m.media.value: media,
                "chat_id": user_id,
            }
            await send_media(**kwargs)
        if m.entities and m.entities[0].url:
            if match := re.match(r"^(?:https?://)?(?:www\.)?t(?:elegram)?\.(?:org|me|dog)/([\w\d_]+)\?start=([\d\w_]+)$", m.text):
                usn = match[1]
                query = match[2]
                return await bypass_bot(usn, query, user_id)
