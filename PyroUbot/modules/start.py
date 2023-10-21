from .. import *


@PY.UBOT("ping")
@PY.TOP_CMD
async def _(client, message):
    await ping_cmd(client, message)


@PY.BOT("start")
@PY.PRIVATE
async def _(client, message):
    await start_cmd(client, message)


@PY.BOT("roll")
async def _(client, message):
    await bet_command(client, message)


@PY.BOT("mulai")
async def _(client, message):
    await mulai_command(client, message)
