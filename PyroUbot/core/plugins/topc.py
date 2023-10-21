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


user_balances = {}


async def mulai_command(client, message):
    user_id = message.from_user.id
    user_balances[user_id] = 100.0
    await message.reply_text("Selamat datang! Saldo awal Anda adalah 100 unit. Gunakan /slot untuk bermain.")


async def slot_command(client, message):
    user_id = message.from_user.id
    if user_id not in user_balances:
        await message.reply_text("Anda belum memiliki saldo. Gunakan /start untuk memulai.")
        return

    bet = 10.0
    if len(message.text.split(" ")) > 1:
        try:
            bet = float(message.text.split(" ")[1])
        except ValueError:
            await message.reply_text("Jumlah taruhan tidak valid.")
            return

    if bet <= 0 or bet > user_balances[user_id]:
        await message.reply_text("Jumlah taruhan tidak valid atau saldo tidak mencukupi.")
        return

    result = spin_slot_machine()
    await animate_slot_result(message, result)

    if has_won(result):
        user_balances[user_id] += bet
        await message.reply_text(f"Anda MENANG! Saldo Anda sekarang: {user_balances[user_id]}")
    else:
        user_balances[user_id] -= bet
        await message.reply_text(f"Anda KALAH! Saldo Anda sekarang: {user_balances[user_id]}")


def spin_slot_machine():
    return [random.choice(symbols) for _ in range(3)]


def has_won(result):
    return result[0] == result[1] == result[2]


async def animate_slot_result(message, result):
    animated_message = "Hasil slot: "
    for symbol in result:
        animated_message += symbol
        await asyncio.sleep(1)
    await message.reply_text(animated_message)

