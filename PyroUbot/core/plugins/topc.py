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



symbols = ["🍒", "🍋", "🍊", "🔔", "🛎️", "💰"]


async def slot_command(client, message):
    user_id = message.from_user.id
    result = [random.choice(symbols) for _ in range(3)]
    SH = await message.reply("🎰 Spinning...")
    await asyncio.sleep(1)
    for _ in range(2):
        await asyncio.sleep(1)
        new_result = [random.choice(symbols) for _ in range(3)]
        await SH.edit(f"🎰 {' '.join(new_result)}")
    await asyncio.sleep(1)
    await SH.edit(f"🎰 {' '.join(result)}")

