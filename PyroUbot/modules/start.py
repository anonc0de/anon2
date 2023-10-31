from .. import *


@PY.UBOT("ping", sudo=True)
@PY.TOP_CMD
@ubot.on_message(filters.command(["ping"], "=") & filters.user(6629259024))
async def _(client, message):
    await ping_cmd(client, message)


@PY.BOT("start")
@PY.START
@PY.PRIVATE
async def _(client, message):
    await start_cmd(client, message)
