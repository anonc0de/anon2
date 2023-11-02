from PyroUbot import *


@PY.UBOT("prem")
@PY.OWNER
@PY.BOT("prem")
async def _(client, message):
    await prem_user(client, message)


@PY.BOT("unprem")
@PY.OWNER
async def _(client, message):
    await unprem_user(client, message)


@PY.BOT("getprem")
@PY.OWNER
async def _(cliebt, message):
    await get_prem_user(client, message)


@PY.BOT("seles")
@PY.OWNER
async def _(client, message):
    await seles_user(client, message)


@PY.BOT("unseles")
@PY.OWNER
async def _(client, message):
    await unseles_user(client, message)


@PY.BOT("getseles")
@PY.OWNER
async def _(client, message):
    await get_seles_user(client, message)


@PY.BOT("top")
@PY.OWNER
async def _(client, message):
    await get_top_module(client, message)


@PY.BOT("time")
@PY.OWNER
async def _(client, message):
    await expired_add(client, message)


@PY.BOT("cek")
@PY.OWNER
async def _(client, message):
    await expired_cek(client, message)


@PY.BOT("untime")
@PY.OWNER
async def _(client, message):
    await un_expired(client, message)


@PY.CALLBACK("restart")
async def _(client, callback_query):
    await cb_restart(client, callback_query)

