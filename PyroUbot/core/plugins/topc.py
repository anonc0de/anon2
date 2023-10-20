from PyroUbot import *


async def get_top_modules(client, message):
    text = "<b>🗂️ᴅᴀғᴛᴀʀ ᴍᴏᴅᴜʟᴇ ᴜʙᴏᴛ\n</b>"
    me_id = client.me.id
    modules = await all_vars(me_id, "modules")
    if not modules:
        await message.reply_text("ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴍᴏᴅᴜʟᴇ ʏᴀɴɢ ᴅɪᴛᴇᴍᴜᴋᴀɴ")
    else:
        for module in modules:
            text += f"•>{module} \n"
        await message.reply_text(text)
