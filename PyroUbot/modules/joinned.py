from PyroUbot import *

__MODULE__ = "joinleave"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴊᴏɪɴʟᴇᴀᴠᴇ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>kickme</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ ɢʀᴜᴘ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>join</code> [ᴜꜱᴇʀɴᴀᴍᴇɢᴄ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴊᴏɪɴ ᴋᴇ ɢʀᴜᴘ ᴍᴇʟᴀʟᴜɪ ᴜꜱᴇʀɴᴀᴍᴇ 

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>leaveallgc</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ ꜱᴇᴍᴜᴀ ɢʀᴜᴘ 

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>leaveallch</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ ꜱᴇᴍᴜᴀ ᴄʜᴀɴɴᴇʟ 

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>leave</code> [ᴜꜱᴇʀɴᴀᴍᴇɢᴄ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ ɢʀᴜᴘ ᴍᴇʟᴀʟᴜɪ ᴜꜱᴇʀɴᴀᴍᴇ
"""


@PY.UBOT("kickme", SUDO=True)
@PY.GROUP
@PY.TOP_CMD
async def _(client, message):
    await leave(client, message)


@PY.UBOT("join", SUDO=True)
@PY.TOP_CMD
async def _(client, message):
    await join(client, message)


@PY.UBOT("leaveallgc", SUDO=True)
@PY.TOP_CMD
async def _(client, message):
    await kickmeall(client, message)


@PY.UBOT("leaveallch", SUDO=True)
@PY.TOP_CMD
async def _(client, message):
    await kickmeallch(client, message)


