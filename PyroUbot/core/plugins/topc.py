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



async def flip_coin_command(client, message):
    user_id = message.from_user.id
    if user_id not in user_balances:
        user_balances[user_id] = 100.0  # Saldo awal 100 unit
    if len(message.text.split(" ")) > 1:
        try:
            bet = float(message.text.split(" ")[1])
            if bet <= 0 or bet > user_balances[user_id]:
                await message.reply("Jumlah taruhan tidak valid atau saldo tidak mencukupi.")
                return
            result = random.choice(coin_sides)
            if result == "Heads":
                user_balances[user_id] += bet
            else:
                user_balances[user_id] -= bet
            await message.reply(f"Hasil pelemparan koin: {result}\nSaldo Anda sekarang: {user_balances[user_id]}")
        except ValueError:
            await message.reply("Jumlah taruhan tidak valid.")
    else:
        await message.reply("Penggunaan: /flip [jumlah taruhan]")



async def balance_command(client, message):
    user_id = message.from_user.id
    if user_id in user_balances:
        await message.reply(f"sᴀʟᴅᴏ : {user_balances[user_id]}")
    else:
        await message.reply("Anda belum memiliki saldo. Gunakan /flip untuk bermain.")

