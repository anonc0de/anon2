from importlib import import_module

from PyroUbot import *

"""
for module, count in module_counts.items():
        print(f"Modul {module} digunakan sebanyak {count} kali.")
"""

async def get_top_module(client, message):
    text = "<b>🗂️ ᴅᴀғᴛᴀʀ ᴍᴏᴅᴜʟᴇ ᴜʙᴏᴛ 🗂️</b>"
    for module, count in module_counts.items():
        try:
            # Mencoba mengubah modul ke dalam format yang diinginkan
            module_name = "ping"
            module_counts = module_usage(module_name)
        except Exception:
            continue
        text += f"\n •> {module_name}: {count} kali digunakan"
    if not text:
        await message.reply_text("Tidak ada modul yang ditemukan.")
    else:
        await message.reply_text(text)
