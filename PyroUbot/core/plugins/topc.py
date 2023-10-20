from importlib import import_module

from PyroUbot import *

"""
for module, count in module_counts.items():
        print(f"Modul {module} digunakan sebanyak {count} kali.")
"""

async def get_top_module(client, message):
    module_name = message.command[1].replace("_", " ")
    usage_count = await get_module_usage(module_name)

    if usage_count is not None:
        response = f"Modul {module_name} telah digunakan sebanyak {usage_count} kali."
    else:
        response = f"Tidak ada hasil penggunaan modul {module_name} yang ditemukan."

    await message.reply(response)
