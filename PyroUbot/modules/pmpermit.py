# yang hapus credits pantat nya bisulan
# create by @NorSodikin
# request by RANGGA SAPUTRA

from PyroUbot import *

__MODULE__ = "pmpermit"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴘᴍᴘᴇʀᴍɪᴛ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}pmpermit (on/off)</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴋᴛɪғᴋᴀɴ ᴅᴀɴ ᴍᴇɴᴏɴᴀᴋᴛɪғᴋᴀɴ ᴘᴍᴘᴇʀᴍɪᴛ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}pmlogs (on/off)</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴋᴛɪғᴋᴀɴ ᴅᴀɴ ᴍᴇɴᴏɴᴀᴋᴛɪғᴋᴀɴ ᴘᴍʟᴏɢs

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}ok or {PREFIX[0]}setuju</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪᴊɪɴᴋᴀɴ sᴇsᴇᴏʀᴀɴɢ ᴜɴᴛᴜᴋ ᴘᴍ ᴀɴᴅᴀ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}no or {PREFIX[0]}tolak</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴏʟᴀᴋ sᴇsᴇᴏʀᴀɴɢ ᴜɴᴛᴜᴋ ᴘᴍ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}setpm (ǫᴜᴇʀʏ) (ᴠᴀʟᴜᴇ)</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴛᴜʀ ᴠᴀʀɪᴀʙᴇʟ ᴛᴇxᴛ_ᴘᴍᴘᴇʀᴍɪᴛ ᴅᴀɴ ʟɪᴍɪᴛ_ᴘᴍ

   <b>•> ǫᴜᴇʀʏ:</b>
       •> <code>PIC</code>
       •> <code>TEXT</code>
       •> <code>LOGS</code>
       •> <code>LIMIT</code>
"""


@ubot.on_message(
    filters.private
    & filters.incoming
    & ~filters.me
    & ~filters.bot
    & ~filters.via_bot
    & ~filters.service,
    group=69,
)
async def _(client, message):
    await pm_anu(client, message)


@PY.UBOT("setpm")
async def _(client, message):
    await pm_set(client, message)


@PY.UBOT("pmpermit")
async def _(client, message):
    await pm_on_off(client, message)


@PY.UBOT("pmlogs")
async def _(client, message):
    await pm_logs(client, message)


@PY.INLINE("pm_pr")
async def _(client, message):
    await pm_sh(client, message)


@PY.UBOT("ok|setuju")
@PY.PRIVATE
async def _(client, message):
    await pm_ok(client, message)


@PY.UBOT("no|tolak")
@PY.PRIVATE
async def _(client, message):
    await pm_no(client, message)





