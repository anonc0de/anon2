from PyroUbot import *

async def get_top_module(client, message):
    text = "<b>🗂️ᴅᴀғᴛᴀʀ ᴍᴏᴅᴜʟᴇ ᴜʙᴏᴛ\n</b>"
    if get_arg(message) in HELP_COMMANDS:
        await bot.send_message(
                HELP_COMMANDS.__MODULE__ + "\n<b> ohmyshinch.t.me </b>",
                quote=True,
            )
        
async def get_prem_user(client, message):
    text = "<b>🗂️ᴅᴀғᴛᴀʀ ᴍᴏᴅᴜʟᴇ ᴜʙᴏᴛ\n</b>"
    modules = loadModule()
    for mod in modules:
        try:
            imported_module = import_module(f"PyroUbot.modules.{mod}")
            module_name = getattr(imported_module, "__MODULE__", "").replace(" ", "_").lower()
        except Exception:
            continue
        text += f"  •> {module_name}\n"
    if not text:
        await message.reply_text("ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴍᴏᴅᴜʟᴇ ʏᴀɴɢ ᴅɪᴛᴇᴍᴜᴋᴀɴ")
    else:
        await message.reply_text(text)
