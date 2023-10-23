from .. import *


# @PY.UBOT("ping")
@ubot.on_message(filters.command("ping"))
@PY.TOP_CMD
# @PY.SUDO
async def _(client, message):
    await ping_cmd(client, message)


@PY.BOT("start")
@PY.PRIVATE
async def _(client, message):
    await start_cmd(client, message)
