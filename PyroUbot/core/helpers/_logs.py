from pyrogram.enums import ChatType

from PyroUbot import *


async def create_logs(client):
    logs = await client.create_channel(f"Logs Ubot: {bot.me.username}")
    await client.set_chat_photo(
        logs.id,
        video="storage/logs.mp4",
    )
    return logs.id


async def forward_logs(client, message):
    logs = await get_vars(client.me.id, "ID_LOGS")
    on_logs = await get_vars(client.me.id, "ON_LOGS")
    if logs and on_logs:
        if message.chat.type == ChatType.PRIVATE:
            type = "ᴘʀɪᴠᴀᴛᴇ"
            from_user = message.chat
        elif message.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP):
            type = "ɢʀᴏᴜᴘ"
            from_user = message.from_user
        rpk = f"[{from_user.first_name} {from_user.last_name or ''}](tg://user?id={from_user.id})"
        link = f"[ᴋʟɪᴋ ᴅɪsɪɴɪ]({message.link})"
        await client.send_message(
            int(logs),
            f"""
<b>📩 ᴀᴅᴀ ᴘᴇsᴀɴ ᴍᴀsᴜᴋ</b>
    <b>•> ᴛɪᴘᴇ ᴘᴇsᴀɴ:<b> <code>{type}</code>
    <b>•> ʟɪɴᴋ ᴘᴇsᴀɴ:<b> {link}
    
<b>⤵️ ᴅɪʙᴀᴡᴀʜ ɪɴɪ ᴀᴅᴀʟᴀʜ ᴘᴇsᴀɴ ᴛᴇʀᴜsᴀɴ ᴅᴀʀɪ: {rpk}</b>
""",
        )
        return await message.forward(int(logs)
