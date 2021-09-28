# Pyrogram String Session Generator Made By @H1M4N5HU0P
# Alicia Pyrogram String Session Generator
# Join @MafiaBot_Support For Future Updates
# Kang With Credits

import asyncio

from pyrogram import Client as Aliciabot

print("""\nWelcome To Alicia Pyrogram String Session\nGenerator By @H1M4N5HU0P\n\n""")
print("""Enter Your Valid Details To Continue!\n\n """)

print("Enter your app information from my.telegram.org/apps below.\n\n")

async def main():
    api_id = int(input("API ID: "))
    api_hash = input("API HASH: ")
    async with Aliciabot(":memory:", api_id=api_id, api_hash=api_hash) as app:
        await app.send_message("me", f"""<b>**Pyrogram String Session**\n\n`{await app.export_session_string()}`\n\n**Pyrogram String Session By Alicia Music Bot Join For Updates @MafiaBot_Support<\b>""")
        print("Thanks For Using Alicia Pyrogram String Generator Your String Session Successfully Saved In Your Telegram!!")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
