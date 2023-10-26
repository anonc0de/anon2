from PyroUbot import *

__MODULE__ = "image"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɪᴍᴀɢᴇ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>rbg</code> [ʀᴇᴘʟʏ ᴛᴏ ᴘʜᴏᴛᴏ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴀᴘᴜs ʟᴀᴛᴀʀ ʙᴇʟᴀᴋᴀɴɢ ɢᴀᴍʙᴀʀ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>blur</code> [ʀᴇᴘʟʏ ᴛᴏ ᴘʜᴏᴛᴏ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴇʀɪᴋᴀ ᴇꜰᴇᴋ ʙʟᴜʀ ᴋᴇ ɢᴀᴍʙᴀʀ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>miror</code> [ʀᴇᴘʟʏ ᴛᴏ ᴘʜᴏᴛᴏ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴇʀɪᴋᴀɴ ᴇꜰᴇᴋ ᴄᴇʀᴍɪɴ ᴋᴇ ɢᴀᴍʙᴀʀ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>negative</code> [ʀᴇᴘʟʏ ᴛᴏ ᴘʜᴏᴛᴏ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴇʀɪᴋᴀɴ ᴇꜰᴇᴋ ɴᴇɢᴀᴛɪᴠᴇ ᴋᴇ ɢᴀᴍʙᴀʀ
"""


@PY.UBOT("rbg", SUDO=True)
@PY.TOP_CMD
async def _(client, message):
    await rbg_cmd(client, message)


@PY.UBOT("blur", SUDO=True)
@PY.TOP_CMD
async def _(client, message):
    await blur_cmd(client, message)


@PY.UBOT("negative", SUDO=True)
@PY.TOP_CMD
async def _(client, message):
    await negative_cmd(client, message)


@PY.UBOT("miror", SUDO=True)
@PY.TOP_CMD
async def _(client, message):
    await miror_cmd(client, message)
