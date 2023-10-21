from .. import *


@PY.UBOT("ping")
@PY.TOP_CMD
async def _(client, message):
    await ping_cmd(client, message)


@PY.BOT("start")
@PY.PRIVATE
async def _(client, message):
    await start_cmd(client, message)


@PY.BOT("flip")
async def _(client, message):
    await flip_coin_command(client, message)


@PY.BOT("saldo")
async def _(client, message):
    await balance_command(client, message)
