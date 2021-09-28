from AliciaMusic.callsmusic.callsmusic import client as Aliciamusic
from pyrogram import filters
from pyrogram.types import Chat, Message, User
from AliciaMusic.config import BOT_USERNAME

@Aliciamusic.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: Aliciamusic, message: Message):
  await Aliciamusic.send_message(message.chat.id, f"Hi there, This is a music assistant service .\n\n ❗️ Rules:\n   - No chatting allowed\n   - No spam allowed \n\n 👉 **SEND GROUP INVITE LINK OR USERNAME IF USERBOT CAN'T JOIN YOUR GROUP.**\n\n ⚠️ Disclamer: If you are sending a message here it means admin will see your message and join chat\n    - Don't add this user to secret groups.\n   - Don't Share private info here\n\n Add @{BOT_USERNAME} And Me to your group make us admin and enjoy vc music!!😉")
  return                        
