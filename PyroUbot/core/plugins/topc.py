from PyroUbot import *

"""
async def get_top_module(client, message):
    vars = await all_vars(bot.me.id, "modules")
    sorted_vars = sorted(vars.items(), key=lambda item: item[1], reverse=True)
    total_count = sum(count for _, count in sorted_vars)
    
    txt = "📊ᴛᴏᴘ ᴄᴏᴍᴍᴀɴᴅ\n"
    for command, count in sorted_vars:
        txt += f" •> {command} : {count}\n"

    txt += f"Total: {total_count} commands"

    await message.reply(txt)
    """


async def get_top_module(client, message):
    vars = await all_vars(client.me.id, "modules")
    sorted_vars = sorted(vars.items(), key=lambda item: item[1], reverse=True)

    command_count = 5
    text = message.text.split()

    if len(text) == 2:
        try:
            command_count = min(max(int(text[1]), 1), 10)
        except ValueError:
            pass

    total_count = sum(count for _, count in sorted_vars[:command_count])

    txt = "📊ᴛᴏᴘ ᴄᴏᴍᴍᴀɴᴅ\n"
    for command, count in sorted_vars[:command_count]:
        txt += f" •> {command} : {count}\n"

    txt += f"📈ᴛᴏᴛᴀʟ: {total_count} ᴄᴏᴍᴍᴀɴᴅ"

    await message.reply(txt)

