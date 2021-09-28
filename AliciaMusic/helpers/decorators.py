from typing import Callable

from pyrogram import Client as Aliciabot
from pyrogram.types import Message

from AliciaMusic.helpers.admins import get_administrators
from AliciaMusic.config import SUDO_USERS


def errors(func: Callable) -> Callable:
    async def decorator(client: Aliciabot, message: Message):
        try:
            return await func(client, message)
        except Exception as e:
            await message.reply(f"{type(e).__name__}: {e}")

    return decorator


def authorized_users_only(func: Callable) -> Callable:
    async def decorator(client: Aliciabot, message: Message):
        if message.from_user.id in SUDO_USERS:
            return await func(client, message)

        administrators = await get_administrators(message.chat)

        for administrator in administrators:
            if administrator == message.from_user.id:
                return await func(client, message)

    return decorator
