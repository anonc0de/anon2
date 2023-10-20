from importlib import import_module

from PyroUbot import *

"""
for module, count in module_counts.items():
        print(f"Modul {module} digunakan sebanyak {count} kali.")
"""

async def get_top_module(client, message):
    imported_module = import_module(f"PyroUbot/modules")
    module_name = getattr(imported_module, "__MODULE__", "").replace(" ", "_").lower()

    usage_count = await get_module_usage(module_name)

    if usage_count is not None:
        response += f"•> {module_name} : {usage_count} ."
    else:
        response += f"•> {module_name} : 0."

    await message.reply(response)


"""
for user_id in await get_seles():
        try:
            user = await bot.get_users(user_id)
            user = f"<a href=tg://user?id={user.id}>{user.first_name} {user.last_name or ''}</a> > <code>{user.id}</code>"
        except Exception:
            continue
        text += f"   •> {user}\n"
    if not text:
        await message.reply_text("Tᴛɪᴅᴀᴋ ᴀᴅᴀ ᴘᴇɴɢɢᴜɴᴀ ʏᴀɴɢ ᴅɪᴛᴇᴍᴜᴋᴀɴ")
    else:
        await message.reply_text(text)

"""
