from importlib import import_module

from PyroUbot import *


async def get_top_module(client, message):
    text = "<b>🗂️ᴅᴀғᴛᴀʀ ᴍᴏᴅᴜʟᴇ ᴜʙᴏᴛ\n</b>"
    modules = loadModule()
    for module_name in modules:
        count = await get_module_usage(module_name)
        text += f"•> {module_name.replace('_', ' ')} : {count} \n"
    if not text:
        await message.reply_text("ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴍᴏᴅᴜʟᴇ ʏᴀɴɢ ᴅɪᴛᴇᴍᴜᴋᴀɴ")
    else:
        await message.reply_text(text)

"""
async def get_top_module(client, message):
    moduler = loadModule() 
    imported_module = import_module(f"PyroUbot.modules.{moduler}")
    module_name = getattr(imported_module, "__MODULE__", "").replace(" ", "_").lower()

    usage_count = await get_module_usage(module_name)

    if usage_count is not None:
        response += f"•> {module_name} : {usage_count} ."
    else:
        response += f"•> {module_name} : 0."

    await message.reply(response)



for user_id in await get_seles():
        try:
            user = await bot.get_users(user_id)
            user = f"<a href=tg://user?id={user.id}>{user.first_name} {user.last_name or ''}</a> > <code>{user.id}</code>"
        except Exception:
            continue
        text += f"   •> {user}\n"
    if not text:
        await message.reply_text("Tᴛɪᴅᴀᴋ ᴀᴅᴀ ᴘᴇɴɢɢᴜɴᴀ ʏᴀɴɢ ᴅɪᴛᴇᴍᴜᴋᴀɴ")
    else:
        await message.reply_text(text)

"""
