from PyroUbot import *


@PY.UBOT("setsudo")
async def _(client, message):
    await add_sudo(client, message)
