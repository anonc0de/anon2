from .. import *


@PY.UBOT("ping")
@PY.SUDO("ping")
@PY.TOP_CMD
async def _(client, message):
    await ping_cmd(client, message)


@PY.BOT("start")
@PY.START
@PY.PRIVATE
async def _(client, message):
    await start_cmd(client, message)
