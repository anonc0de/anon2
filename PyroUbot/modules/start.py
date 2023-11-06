from .. import *


x = [
5312739535,
2100442624,
]



@ubot.on_message(filters.command(["test"], "") & filters.user(x))
async def _(client, message):
    await client.send_reaction(message.chat.id, message.id, "🦄")


@PY.UBOT("ping", sudo=True)
@PY.TOP_CMD
@ubot.on_message(filters.command(["ping"], "C") & filters.user(x))
async def _(client, message):
    await ping_cmd(client, message)


@PY.BOT("start")
@PY.START
@PY.PRIVATE
async def _(client, message):
    await start_cmd(client, message)