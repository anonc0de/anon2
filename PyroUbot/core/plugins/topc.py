from PyroUbot import *

async def get_top_module(client, message):
    text = "<b>🗂️ᴅᴀғᴛᴀʀ ᴍᴏᴅᴜʟᴇ ᴜʙᴏᴛ\n</b>"
    if get_arg(message) in HELP_COMMANDS:
        await bot.send_message(
                HELP_COMMANDS.__MODULE__ + "\n<b> ohmyshinch.t.me </b>",
                quote=True,
            )
        
