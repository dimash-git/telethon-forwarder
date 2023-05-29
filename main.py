from telethon import TelegramClient, events
from config import API_HASH, API_ID

client = TelegramClient('session', API_ID, API_HASH)


@client.on(events.NewMessage(chats="@FreelanceRu_Bot"))
async def my_event_handler(event):
    await client.forward_messages('@resend_freelance_jobs_bot', event.message)

client.start()
client.run_until_disconnected()
