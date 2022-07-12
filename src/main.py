import asyncio
import configparser

from pyrogram import Client

config = configparser.ConfigParser()
config.read("cfg.ini")

api_id = config.get("CFG", "API_ID")
api_hash = config.get("CFG", "API_HASH")
print("сделано @inchdev (tg)")


async def main():
    file = open("chats.txt", "r")
    file = str(file.read())
    text = file.split("\n")
    num = 0
    async with Client("s", api_id, api_hash) as app:
        for val in text:
            val = val.replace("@", '')
            val = val.replace("https://t.me/joinchat/", "")
            val = val.replace("joinchat/", "")
            try:
                await asyncio.sleep(30)
                await app.join_chat(val)
                num += 1
                if num == 5:
                    num = 0
                    await asyncio.sleep(240)
                print(f"Подписался на канал/чат @{val}")
            except Exception as e:
                print(e)
                num += 1
                if num == 5:
                    num = 0
                    await asyncio.sleep(240)


asyncio.run(main())
