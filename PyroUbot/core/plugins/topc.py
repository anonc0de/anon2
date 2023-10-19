"""
from importlib import import_module

from PyroUbot.modules import loadModule

from PyroUbot import *

async def get_top_module(client, message):
    text = "<b>🗂️ᴅᴀғᴛᴀʀ ᴍᴏᴅᴜʟᴇ ᴜʙᴏᴛ\n</b>"
    modules = loadModule()
    for mod in modules:
        try:
            imported_module = import_module(f"PyroUbot.modules.{mod}")
            module_name = getattr(imported_module, "__MODULE__", "").replace(" ", "_").lower()
        except Exception:
            continue
        text += f"•> {module_name} : \n"
    if not text:
        await message.reply_text("ᴛɪᴅᴀᴋ")
    else:
        await message.reply_text(text)
"""
