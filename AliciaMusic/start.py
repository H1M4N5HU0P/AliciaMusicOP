from pyrogram import Client as Aliciabot
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from AliciaMusic.config import BOT_NAME, BOT_USERNAME, BOT_PIC, SUPPORT_CHANNEL, ASSISTANT_USERNAME, OWNER_USERNAME


@Aliciabot.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start_(client: Aliciabot, message: Message):
    await message.reply_text(
        f"""<b>Hey there {format(
        message.from_user.mention)}![🤓]({BOT_PIC})
        
I am {BOT_NAME}

I can play songs in your group's VC🤗

To listen songs add me to your group..

And don't forgot to promote me with all rights!🥰

Otherwise I can't play songs!🥺👉👈

Use the buttons below to know more about me..😊
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton("😎OWNER😎", url=f"https://t.me/{OWNER_USERNAME}"),                
                    InlineKeyboardButton("📄COMMANDS📄", url=f"https://telegra.ph/MUSIC-BOT-COMMANDS-09-28")
                     ],[
                    InlineKeyboardButton("💥SUPPORT CHANNEL💥", url=f"https://t.me/{SUPPORT_CHANNEL}"),
                    InlineKeyboardButton("🔥SUPPORT GROUP🔥", url=f"https://t.me/{SUPPORT_GROUP}")
                     ],[
                    InlineKeyboardButton("🎸ASSISTANT 🎸", url=f"https://t.me/{SUPPORT_GROUP}"),
                    InlineKeyboardButton("⚡REPO⚡", url=f"https://github.com/H1M4N5HU0P/AliciaMusicOP")
                     ],[
                    InlineKeyboardButton("➕ ADD TO YOUR GROUP ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ]
            ]
        ),
    )


@Aliciabot.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(client: Aliciabot, message: Message):
      await message.reply_text(f"""**{BOT_NAME} is online**🥰""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("😎OWNER😎", url=f"https://t.me/{OWNER_USERNAME}"),
                    InlineKeyboardButton("⚡REPO⚡", url=f"https://github.com/H1M4N5HU0P/AliciaMusicOP")
                ]
            ]
        )
   )


@Aliciabot.on_message(filters.command("help") & filters.private & ~filters.channel)
async def help(client: Aliciabot, message: Message):
    await message.reply_text(
        f"""<b>Hey there {format(
        message.from_user.mention)}! [Click here](https://telegra.ph/MUSIC-BOT-COMMANDS-09-28) to know about my Commands.⚡🔥
        """)
        

@Aliciabot.on_message(filters.command("commands") & filters.private & ~filters.channel)
async def commands(client: Aliciabot, message: Message):
    await message.reply_text(
        f"""<b>Hey there {format(
        message.from_user.mention)}! [Click here](https://telegra.ph/MUSIC-BOT-COMMANDS-09-28) to know about my Commands.⚡🔥
        """)
        
