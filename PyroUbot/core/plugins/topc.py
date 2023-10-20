from PyroUbot import *


async def get_top_module(client, message):
    vars = await all_vars(bot.me.id, "modules")
    sorted_vars = sorted(vars.items(), key=lambda item: item[1], reverse=True)
    total_count = sum(count for _, count in sorted_vars)
    
    txt = "📊ᴛᴏᴘ ᴄᴏᴍᴍᴀɴᴅ\n"
    for command, count in sorted_vars:
        txt += f" •> {command} : {count}\n"

    txt += f"Total: {total_count} commands"

    await message.reply(txt)
