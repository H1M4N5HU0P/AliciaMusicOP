from pyrogram import Client as Aliciabot
from pytgcalls import PyTgCalls

from AliciaMusic import config
from AliciaMusic.callsmusic.queues import queues

client = Aliciabot(config.SESSION_NAME, config.API_ID, config.API_HASH)
pytgcalls = PyTgCalls(client)


@pytgcalls.on_stream_end()
def on_stream_end(chat_id: int) -> None:
    queues.task_done(chat_id)

    if queues.is_empty(chat_id):
        pytgcalls.leave_group_call(chat_id)
    else:
        pytgcalls.change_stream(
            chat_id, queues.get(chat_id)["file"]
        )


run = pytgcalls.run
