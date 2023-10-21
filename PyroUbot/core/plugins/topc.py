import random
from PyroUbot import *


coin_sides = ["Heads", "Tails"]

user_balances = {}


async def get_top_module(client, message):
    vars = await all_vars(client.me.id, "modules")
    sorted_vars = sorted(vars.items(), key=lambda item: item[1], reverse=True)

    command_count = 100
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



def flip_coin_command(client, message):
    user_id = message.from_user.id
    if user_id not in user_balances:
        user_balances[user_id] = 100.0 
    if len(message.text.split(" ")) > 1:
        try:
            bet, choice = message.text.split(" ")[1], message.text.split(" ")[2].capitalize()
            if choice not in coin_sides:
                await message.reply("Pilihan tidak valid. Gunakan 'Heads' atau 'Tails'.")
                return
            bet = float(bet)
            if bet <= 0 or bet > user_balances[user_id]:
                await message.reply("Jumlah taruhan tidak valid atau saldo tidak mencukupi.")
                return
            result = random.choice(coin_sides)
            if result == choice:
                user_balances[user_id] += bet
                await message.reply(f"Hasil pelemparan koin: {result}\nAnda MENANG! Saldo Anda sekarang: {user_balances[user_id]}")
            else:
                user_balances[user_id] -= bet
                await message.reply(f"Hasil pelemparan koin: {result}\nAnda KALAH! Saldo Anda sekarang: {user_balances[user_id]}")
        except ValueError:
            await message.reply("Penggunaan: /flip [jumlah taruhan] [Heads/Tails]")
    else:
        await message.reply("Penggunaan: /flip [jumlah taruhan] [Heads/Tails]")



async def balance_command(client, message):
    user_id = message.from_user.id
    if user_id in user_balances:
        await message.reply(f"sᴀʟᴅᴏ : {user_balances[user_id]}")
    else:
        await message.reply("Anda belum memiliki saldo. Gunakan /flip untuk bermain.")

