from .. import *


# @PY.UBOT("ping")
@ubot.on_message(ubot.cmd_prefix("ping"))
@PY.SUDO
@PY.TOP_CMD
async def _(client, message):
    await ping_cmd(client, message)


@PY.BOT("start")
@PY.PRIVATE
async def _(client, message):
    await start_cmd(client, message)
