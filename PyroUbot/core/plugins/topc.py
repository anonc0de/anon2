from PyroUbot import *

"""
async def get_top_module(client, message):
    vars = await all_vars(bot.me.id, "modules")
    txt = "📊ᴛᴏᴘ ᴄᴏᴍᴍᴀɴᴅ\n"
    for command, count in vars.items():
        txt += f" •> {command} : {count}\n"

    await message.reply(txt)
"""

async def get_top_modules(client, message):
    modules = await all_vars(client.me.id, "modules")
    sorted_modules = sorted(modules.items(), key=lambda item: item[1], reverse=True)
    
    txt = "📊ᴛᴏᴘ ᴄᴏᴍᴍᴀɴᴅ\n"
    total_count = 0
    
    for command, count in sorted_modules:
        txt += f" •> {command} : {count}\n"
        total_count += count
    
    txt += f"\nTotal Penggunaan: {total_count}"
