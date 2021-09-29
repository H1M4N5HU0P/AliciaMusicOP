import os
import requests
from pyrogram import Client as Aliciabot

from AliciaMusic.config import API_ID, API_HASH, BOT_TOKEN
from AliciaMusic.callsmusic.callsmusic import run


bot = Aliciabot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="AliciaMusic.handlers")
)

bot.start()
run()

