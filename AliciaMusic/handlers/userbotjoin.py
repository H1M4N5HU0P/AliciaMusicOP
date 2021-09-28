from AliciaMusic.callsmusic.callsmusic import client as Aliciamusic
from pyrogram import Client as Aliciabot
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from AliciaMusic.helpers.decorators import errors, authorized_users_only
from AliciaMusic.config import BOT_NAME as bn, BOT_USERNAME

@Aliciabot.on_message(filters.group & filters.command(["userbotjoin"]))
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Add me as admin of yor group first</b>",
        )
        return

    try:
        user = await Aliciamusic.get_me()
    except:
        user.first_name =  f"{bn}"

    try:
        await Aliciamusic.join_chat(invitelink)
        await Aliciamusic.send_message(message.chat.id,"I joined here as you requested")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>helper already in your chat</b>",
        )
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 Flood Wait Error 🛑 \n User {user.first_name} couldn't join your group due to heavy join requests for userbot! Make sure user is not banned in group."
            f"\n\nOr manually add @{BOT_USERNAME} to your Group and try again</b>",
        )
        return
    await message.reply_text(
            "<b>helper userbot joined your chat</b>",
        )
    
@Aliciamusic.on_message(filters.group & filters.command(["userbotleave"]))
async def rem(Aliciamusic, message):
    try:
        await Aliciamusic.leave_chat(message.chat.id)
    except:  
        await message.reply_text(
            f"<b>User couldn't leave your group! May be floodwaits."
            "\n\nOr manually kick me from to your Group</b>",
        )
        return
