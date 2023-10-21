import asyncio
import random

from PyroUbot import *



async def get_top_module(client, message):
    vars = await all_vars(client.me.id, "modules")
    sorted_vars = sorted(vars.items(), key=lambda item: item[1], reverse=True)

    command_count = 999
    text = message.text.split()

    if len(text) == 2:
        try:
            command_count = min(max(int(text[1]), 1), 10)
        except ValueError:
            pass

    total_count = sum(count for _, count in sorted_vars[:command_count])

    txt = "<b>📊 ᴛᴏᴘ ᴄᴏᴍᴍᴀɴᴅ</b>\n\n"
    for command, count in sorted_vars[:command_count]:
        txt += f"<b> •> {command} : {count}</b>\n"

    txt += f"\n<b>📈 ᴛᴏᴛᴀʟ: {total_count} ᴄᴏᴍᴍᴀɴᴅ</b>"

    await message.reply(txt)


def spin_slot_machine():
    symbols = ["🍒", "🍋", "🍊", "🔔", "🛎️", "💰"]
    result = [random.choice(symbols) for _ in range(3)]
    return result


async def animate_slot_result(message, result):
    animated_message = ""
    for symbol in result:
        animated_message += symbol
        await asyncio.sleep(1)
        await message.reply(f"Hasil slot: {animated_message}")

