import asyncio

from pyrogram.enums import ChatType

from PyroUbot import OWNER_ID, bot, ubot


async def get_global_id(client, query):
    chats = []
    chat_types = {
        "global": [ChatType.CHANNEL, ChatType.GROUP, ChatType.SUPERGROUP],
        "group": [ChatType.GROUP, ChatType.SUPERGROUP],
        "users": [ChatType.PRIVATE],
    }
    async for dialog in client.get_dialogs(limit=None):
        if dialog.chat.type in chat_types[query]:
            chats.append(dialog.chat.id)

    return chats


async def install_my_peer(client):
    users = [
        dialog.chat.id
        async for dialog in client.get_dialogs(limit=None)
        if dialog.chat.type == ChatType.PRIVATE
    ]
    groups = [
        dialog.chat.id
        async for dialog in client.get_dialogs(limit=None)
        if dialog.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP)
    ]
    client_id = client.me.id

    client._get_my_peer[client_id] = {"pm": users, "gc": groups}


async def installPeer():
    tasks = [install_my_peer(client) for client in ubot._ubot]
    await asyncio.gather(*tasks, return_exceptions=True)
    await bot.send_message(OWNER_ID, "✅ sᴇᴍᴜᴀ ᴘᴇᴇʀ_ɪᴅ ʙᴇʀʜᴀsɪʟ ᴅɪɪɴsᴛᴀʟʟ")
