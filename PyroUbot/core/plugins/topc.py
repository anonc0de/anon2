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


user_balances = {}


roulette_numbers = list(range(0, 37))


bet_types = {
    "straight_up": {"name": "Straight Up", "payout": 36},
    "even_odd": {"name": "Even/Odd", "payout": 2},
    "red_black": {"name": "Red/Black", "payout": 2},
    "low_high": {"name": "Low/High", "payout": 2},
}


async def mulai_command(client, message):
    user_id = message.from_user.id
    if user_id not in user_balances:
        user_balances[user_id] = 100.0
        await message.reply("Selamat datang di permainan roulette! Saldo awal Anda adalah 100 unit. Gunakan /bet untuk memasang taruhan.")


async def bet_command(client, message):
    user_id = message.from_user.id
    if user_id not in user_balances:
        await message.reply("Anda belum memiliki saldo. Gunakan /mulai untuk memulai.")
        return

    args = message.text.split(" ")[1:]
    if len(args) != 3:
        await message.reply("Penggunaan: /bet [jenis taruhan] [jumlah taruhan] [nomor/jenis]")
        return

    bet_type, amount, bet_selection = args[0], float(args[1]), args[2]

    if bet_type not in bet_types:
        await message.reply("Jenis taruhan tidak valid.")
        return

    if amount <= 0 or amount > user_balances[user_id]:
        await message.reply("Jumlah taruhan tidak valid atau saldo tidak mencukupi.")
        return

    if bet_type == "straight_up" and bet_selection not in map(str, roulette_numbers):
        await message.reply("Nomor taruhan straight up tidak valid.")
        return
    elif bet_type in ["even_odd", "red_black", "low_high"]:
        valid_selections = ["even", "odd", "red", "black", "low", "high"]
        if bet_selection not in valid_selections:
            await message.reply("Pilihan taruhan tidak valid.")
            return

    result = random.choice(roulette_numbers)
    payout = determine_payout(bet_type, bet_selection, result)
    user_balances[user_id] += payout - amount
    await message.reply(f"Hasil roulette: {result} - {bet_types[bet_type]['name']}\nSaldo Anda sekarang: {user_balances[user_id]}")


def determine_payout(bet_type, bet_selection, result):
    if bet_type == "straight_up":
        return bet_types[bet_type]["payout"] if result == int(bet_selection) else 0
    elif bet_type == "even_odd":
        return bet_types[bet_type]["payout"] if (result % 2 == 0 and bet_selection == "even") or (result % 2 != 0 and bet_selection == "odd") else 0
    elif bet_type == "red_black":
        red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        return bet_types[bet_type]["payout"] if ((result in red_numbers) and bet_selection == "red") or ((result not in red_numbers) and bet_selection == "black") else 0
    elif bet_type == "low_high":
        return bet_types[bet_type]["payout"] if (result >= 1 and result <= 18 and bet_selection == "low") or (result >= 19 and result <= 36 and bet_selection == "high") else 0

