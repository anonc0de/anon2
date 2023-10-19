from importlib import import_module

from PyroUbot import *

"""
for module, count in module_counts.items():
        print(f"Modul {module} digunakan sebanyak {count} kali.")
"""

async def get_top_module(client, message):
    text = "<b>🗂️ ᴅᴀғᴛᴀʀ ᴍᴏᴅᴜʟᴇ ᴜʙᴏᴛ 🗂️</b>"
    module_results = usage_module()
    for result in module_results:
        try:
            module_name = result["module_name"]
            usage_count = result["usage_count"]
        except Exception:
            continue
        text += f"\n •> {module_name}: {usage_count} kali digunakan"
    if not text:
        await message.reply_text("Tidak ada modul yang ditemukan.")
    else:
        await message.reply_text(text)
