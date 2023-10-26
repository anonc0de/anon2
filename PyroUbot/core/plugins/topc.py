from PyroUbot import *


async def get_top_module(client, message):
    vars = await all_vars(bot.me.id, "modules")
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


async def add_sudo(client, message):
    try:
        msg = await message.reply("ᴍᴇᴍᴘʀᴏsᴇs...", quote=True)
        if len(message.command) < 3:
            return await msg.edit("<b>ᴛᴏʟᴏɴɢ ᴍᴀsᴜᴋᴋᴀɴ ǫᴜᴇʀʏ ᴅᴀɴ ᴠᴀʟᴇᴜ ɴʏᴀ</b>")
        query_mapping = {"sudo": "SUDO_USERS"}
        command, mapping, valeu = message.command[:3]
        if mapping.lower() in query_mapping:
            query_var = query_mapping[mapping.lower()]
            await set_vars(client.me.id, query_var, valeu)
            return await msg.edit(
                f"<b> <code>user added</b>"
            )
    except Exception as error:
        await msg.edit(str(error))
        

