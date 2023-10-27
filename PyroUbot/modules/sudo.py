"""
yang hapus credits pantatnya bisulan
create by: https://t.me/NorSodikin 
"""


from PyroUbot import *


@PY.UBOT("addsudo")
@PY.TOP_CMD
async def _(client, message):
    msg = await message.reply("sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs...")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(
            "➡️ Hᴀʀᴀᴘ ʙᴀʟᴀs ᴋᴇ ᴜsᴇʀ ᴀᴛᴀᴜ ᴋᴇᴛɪᴋ ᴜsᴇʀ_ɪᴅ ʏᴀɴɢ ɪɴɢɪɴ ᴅɪᴛᴀᴍʙᴀʜᴋᴀɴ ᴋᴇ ᴅᴀғᴛᴀʀ sᴜᴅᴏ"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    sudo_users = await get_list_from_vars(client.me.id, "SUDO_USERS", "DB_SUDO")

    if user.id in sudo_users:
        return await msg.edit(
            f"✨ {user.first_name} {user.last_name or ''} sᴜᴅᴀʜ ʙᴇʀᴀᴅᴀ ᴅᴀʟᴀᴍ ᴅᴀғᴛᴀʀ sᴜᴅᴏ"
        )

    try:
        await add_to_vars(client.me.id, "SUDO_USERS", user.id, "DB_SUDO")
        return await msg.edit(
            f"✅ {user.first_name} {user.last_name or ''} ʙᴇʀʜᴀsɪʟ ᴅɪᴛᴀᴍʙᴀʜᴋᴀɴ ᴋᴇ ᴅᴀғᴛᴀʀ sᴜᴅᴏ"
        )
    except Exception as error:
        return await msg.edit(error)


@PY.UBOT("delsudo")
@PY.TOP_CMD
async def _(client, message):
    msg = await message.reply("sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs...")
    user_id = await extract_user(message)
    if not user_id:
        return await message.reply(
            "➡️ Hᴀʀᴀᴘ ʙᴀʟᴀs ᴋᴇ ᴜsᴇʀ ᴀᴛᴀᴜ ᴋᴇᴛɪᴋ ᴜsᴇʀ_ɪᴅ ʏᴀɴɢ ɪɴɢɪɴ ᴅɪᴛᴀᴍʙᴀʜᴋᴀɴ ᴋᴇ ᴅᴀғᴛᴀʀ sᴜᴅᴏ"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    sudo_users = await get_list_from_vars(client.me.id, "SUDO_USERS", "DB_SUDO")

    if user.id not in sudo_users:
        return await msg.edit(
            f"✨ {user.first_name} {user.last_name or ''} ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴅᴀʟᴀᴍ ᴅᴀғᴛᴀʀ sᴜᴅᴏ"
        )

    try:
        await remove_from_vars(client.me.id, "SUDO_USERS", user.id, "DB_SUDO")
        return await msg.edit(
            f"❌ {user.first_name} {user.last_name or ''} ʙᴇʀʜᴀsɪʟ ᴅɪʜᴀᴘᴜs ᴅᴀʀɪ ᴅᴀғᴛᴀʀ sᴜᴅᴏ"
        )
    except Exception as error:
        return await msg.edit(error)


@PY.UBOT("getsudo")
@PY.TOP_CMD
async def _(client, message):
    msg = await message.reply("sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs...")
    sudo_users = await get_list_from_vars(client.me.id, "SUDO_USERS", "DB_SUDO")

    if not sudo_users:
        return await message.reply("ᴅᴀғᴛᴀʀ sᴜᴅᴏ ᴋᴏsᴏɴɢ")

    sudo_list = []
    for user_id in sudo_users:
        try:
            user = await client.get_users(int(user_id))
            sudo_list.append(
                f" ├ {user.first_name} {user.last_name or ''} | {user.id}"
            )
        except:
            continue

    if sudo_list:
        response = (
            "❏ ᴅᴀғᴛᴀʀ sᴜᴅᴏ:\n"
            + "\n".join(sudo_list)
            + f"\n ╰ ᴛᴏᴛᴀʟ sᴜᴅᴏ_ᴜsᴇʀs: {len(sudo_list)}"
        )
        return await msg.edit(response)
    else:
        return await msg.edit("ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴɢᴀᴍʙɪʟ ᴅᴀғᴛᴀʀ sᴜᴅᴏ sᴀᴀᴛ ɪɴɪ")
