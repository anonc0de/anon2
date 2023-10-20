from PyroUbot import *


async def get_top_module(client, message):
    vars = await all_vars(bot.me.id, "modules")
    txt = "ketik text\n"
    for command, count in vars.items():
        txt += f"•> {command} - {count}\n"

    await message.reply(txt)
