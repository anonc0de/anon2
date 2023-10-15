import asyncio

from pyrogram import idle

from PyroUbot import *


async def start_ubot(user_id, _ubot):
    ubot_ = Ubot(**_ubot)
    try:
        await asyncio.wait_for(ubot_.start(), timeout=30)
        await ubot_.join_chat("MutualanConsterly")
    except asyncio.TimeoutError:
        await remove_ubot(user_id)
        await add_prem(user_id)
        await sending_user(user_id)
        print(f"[𝗜𝗡𝗙𝗢] - ({user_id}) 𝗧𝗜𝗗𝗔𝗞 𝗗𝗔𝗣𝗔𝗧 𝗠𝗘𝗥𝗘𝗦𝗣𝗢𝗡")
    except:
        await remove_ubot(user_id)
        await rm_all(user_id)
        await remove_all_vars(user_id)
        await rem_pref(user_id)
        await rem_expired_date(user_id)
        for X in await get_chat(user_id):
            await remove_chat(user_id, X)
        print(f"✅ {user_id} 𝗕𝗘𝗥𝗛𝗔𝗦𝗜𝗟 𝗗𝗜𝗛𝗔𝗣𝗨𝗦")


async def main():
    ubots = await get_userbots()
    tasks = []
    for ubot in ubots:
        task = asyncio.create_task(safe_start_ubot(int(ubot["name"]), ubot))
        tasks.append(task)
    try:
        await asyncio.gather(*tasks, bot.start())
        await asyncio.gather(loadPlugins(), installPeer(), idle())
    except KeyboardInterrupt:
        print("KeyboardInterrupt - Stopping the program.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    loop = asyncio.get_event_loop_policy().get_event_loop()
    loop.create_task(expiredUserbots())
    loop.run_until_complete(main())
