from importlib import import_module

from PyroUbot import *

"""
for module, count in module_counts.items():
        print(f"Modul {module} digunakan sebanyak {count} kali.")
"""

async def get_top_module(client, message):
    module_results = await get_module_usage(message.command[1])

    if not module_results:
        await message.reply("Tidak ada hasil penggunaan modul yang ditemukan.")
    else:
        response = "Hasil penggunaan modul:\n"
        for result in module_results:
            module_name = getattr(imported_module, "__MODULE__", "").replace(" ", "_").lower()
            usage_count = result["usage_count"]
            response += f"Modul {module_name}: {usage_count} kali digunakan\n"
        await message.reply(response)
