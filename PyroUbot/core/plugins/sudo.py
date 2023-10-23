from PyroUbot import *

"""
async def add_sudo(client, message):
    user = await client.get_users(user_id)
    user_id = (await client.get_users(user_id)).id
    sudoer = await add_to_vars(client.me.id, "SUDO_USERS", user_id)
    
    if user_id not in sudoer:
        await message.reply(f"<b>{user.first_name} {user.last_name or ''} add to sudo</b>")
"""


async def add_sudo(client, message):
    try:
        msg = await message.reply("ᴍᴇᴍᴘʀᴏsᴇs...", quote=True)
        if len(message.command) < 3:
            return await msg.edit("<b>ᴛᴏʟᴏɴɢ ᴍᴀsᴜᴋᴋᴀɴ ǫᴜᴇʀʏ ᴅᴀɴ ᴠᴀʟᴇᴜ ɴʏᴀ</b>")
        query_mapping = {"sudo": "SUDO_USERS"}
        command, mapping, valeu = message.command[:3]
        if mapping.lower() in query_mapping:
            query_var = query_mapping[mapping.lower()]
            await set_vars(client.me.id, query_var, valeu)
            return await msg.edit(
                f"<b> <code>{query_var} added</b>"
            )
    except Exception as error:
        await msg.edit(str(error))
