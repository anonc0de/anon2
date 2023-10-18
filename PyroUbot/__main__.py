import asyncio

from pyrogram import idle
from pyrogram.errors import RPCError


from PyroUbot import *


async def main():
    await bot.start()
    for _ubot in await get_userbots():
        ubot_ = Ubot(**_ubot)
        try:
            await ubot_.start()
        except RPCError:
            await remove_ubot(int(_ubot["name"]))
            print(f"{_ubot['name']} Successfully Deleted From Database")
    await loadPlugins()
    await installPeer()
    await idle()

async def ex():
    await asyncio.sleep(60)
    await expiredUserbots()

if __name__ == "__main__":
    get_event_loop().create_task(ex())
    get_event_loop().run_until_complete(main())
