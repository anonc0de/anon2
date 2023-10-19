from importlib import import_module

from PyroUbot import *

"""
for module, count in module_counts.items():
        print(f"Modul {module} digunakan sebanyak {count} kali.")
"""

async def get_top_module(client, message):
    text = "<b>🗂️ ᴅᴀғᴛᴀʀ ᴍᴏᴅᴜʟᴇ ᴜʙᴏᴛ 🗂️</b>"
    for module, count in await module_usage():
        try:
            module_name = module.replace(" ", "_").lower()
        except Exception:
            continue
        text += f"\n •> {module_name}: {count} kali digunakan"
    if not text:
        await message.reply_text("Tidak ada modul yang ditemukan.")
    else:
        await message.reply_text(text)
