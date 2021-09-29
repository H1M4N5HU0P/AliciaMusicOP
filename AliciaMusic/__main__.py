import requests
from pyrogram import Client as Aliciabot

from .callsmusic.callsmusic import run
from config import API_ID, API_HASH, BOT_TOKEN


bot = Aliciabot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="AliciaMusic.handlers")
)

bot.start()
run()

