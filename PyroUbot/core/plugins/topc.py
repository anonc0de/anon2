from PyroUbot import *


async def get_top_module(client, message):
    vars = await all_vars(bot.me.id, "modules")
    sorted_modules = sorted(modules.query(), key=lambda item: item[1], reverse=True)
    txt = "📊ᴛᴏᴘ ᴄᴏᴍᴍᴀɴᴅ\n"
    for command, count in sorted_modules:
        txt += f" •> {command} : {count}\n"

    await message.reply(txt)
