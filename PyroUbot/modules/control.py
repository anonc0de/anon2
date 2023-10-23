from PyroUbot import *

__MODULE__ = "control"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴄᴏɴᴛʀᴏʟ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>setprefix</code> [sɪᴍʙᴏʟ ᴘʀᴇғɪx]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴜʙᴀʜ ᴘʀᴇғɪx/ʜᴀɴᴅʟᴇʀ ᴄᴏᴍᴍᴀɴᴅ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>setemoji</code> [ǫᴜᴇʀʏ] [ᴠᴀʟᴇᴜ]
  <b>• ǫᴜᴇʀʏ: </b>
       <b>•> PONG </b>
       <b>•> MENTION </b>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ᴛᴀᴍᴘɪʟᴀɴ ᴘᴀᴅᴀ ᴘɪɴɢ</b>

"""



@PY.UBOT("setprefix")
@PY.TOP_CMD
async def _(client, message):
    await setprefix(client, message)

@PY.UBOT("setemoji")
@PY.TOP_CMD
async def _(client, message):
    await change_emot(client, message)

