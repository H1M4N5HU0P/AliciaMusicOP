from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from config import OWNER, BG_IMAGE, SUPPORT_GROUP, ASSISTANT_USERNAME, BOT_USERNAME, UPDATES_CHANNEL

@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hey there {format(
        message.from_user.mention)}![🤓]({BG_IMAGE})
        
I am {bn}

I can play songs in your group's VC🤗

To listen songs add me to your group..

And don't forgot to promote me with all rights!🥰

Add my assistant👉 {ASSISTANT_USERNAME} to listen music

Use the buttons below to know more about me..😊
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton("OWNER", url="https://t.me/{OWNER}"), InlineKeyboardButton("REPO", url="https://github.com/H1M4N5HU0P/AliciaMusicOP")
                ],[
                    InlineKeyboardButton("UPDATES CHANNEL", url="https://t.me/{UPDATES_CHANNEL}"), InlineKeyboardButton("SUPPORT GROUP", url="https://t.me/{SUPPORT_GROUP}")
                 ],
                 [
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ]
            ]
        ),
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(client: Client, message: Message):
      await message.reply_text("""**{bn} is online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "OWNER", url="https://t.me/{OWNER}")
                ]
            ]
        )
   )


@Client.on_message(filters.command("help") & filters.private & ~filters.channel)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hey there {format(
        message.from_user.mention)}!\n
**COMMANDS FOR GROUP**
/play <song name> - play song you requested
/play <reply to audio> - play replied file
/dplay <song name> - play song you requested via deezer
/splay <song name> - play song you requested via jio saavn
/ytplay <song name> - Directly play song via Youtube Music
/playlist - Show now playing list
/current - Show now playing
/song <song name> - download songs you want quickly
/search <query> - search videos on youtube with details
/deezer <song name> - download songs you want quickly via deezer
/saavn <song name> - download songs you want quickly via saavn
/video <song name> - download videos you want quickly

**ONLY ADMINS COMMAND**
/player - open music player settings panel
/pause - pause song play
/resume - resume song play
/skip - play next song
/end - stop music play
/userbotjoin - invite assistant to your chat
/userbotleave - remove assistant from your chat
/admincache - Refresh admin list
/musicplayer [on/off]` - Enable/Disable Music Player

**COMMAND FOR CHANNELS**
/userbotjoinchannel` - invite assistant to your chat
* channel is also can be used instead of c

        """)
        

@Client.on_message(filters.command("commands") & filters.private & ~filters.channel)
async def commands(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hey there {format(
        message.from_user.mention)}!
**COMMANDS FOR GROUP**
/play <song name> - play song you requested
/play <reply to audio> - play replied file
/dplay <song name> - play song you requested via deezer
/splay <song name> - play song you requested via jio saavn
/ytplay <song name> - Directly play song via Youtube Music
/playlist - Show now playing list
/current - Show now playing
/song <song name> - download songs you want quickly
/search <query> - search videos on youtube with details
/deezer <song name> - download songs you want quickly via deezer
/saavn <song name> - download songs you want quickly via saavn
/video <song name> - download videos you want quickly

**ONLY ADMINS COMMAND**
/player - open music player settings panel
/pause - pause song play
/resume - resume song play
/skip - play next song
/end - stop music play
/userbotjoin - invite assistant to your chat
/userbotleave - remove assistant from your chat
/admincache - Refresh admin list
/musicplayer [on/off]` - Enable/Disable Music Player

**COMMAND FOR CHANNELS**
/userbotjoinchannel` - invite assistant to your chat
* channel is also can be used instead of c
        """)
        
        
        