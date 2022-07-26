from pyrogram import idle
from clients import user, bot


async def main():
    print("[ BOT ] Bot Starting")
    await bot.start()
    print("[ USER ] User Starting")
    await user.start()
    print("[ CLIENT ] All Client Starting, Idling Now.")
    await idle()
    print("[ CLIENT ] All Client Stopping, Exiting Now.")


if __name__ == "__main__":
    bot.run(main())
