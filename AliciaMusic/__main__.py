import os
import requests
from pyrogram import Client as Aliciabot

from catmusic.config import API_ID, API_HASH, BOT_TOKEN
from catmusic.callsmusic.callsmusic import run


bot = catmusic(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="catmusic.handlers")
)

bot.start()
run()

