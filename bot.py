from twitchio.ext import commands
from dotenv import load_dotenv
import os
from tts_handler import enqueue_tts, start_tts_worker

load_dotenv()

TOKEN = os.getenv('TOKEN')
CHANNEL = os.getenv('CHANNEL')
BOT_USER = os.getenv('BOT_USER')

start_tts_worker()  # Start the background TTS processing thread

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(
            token=TOKEN,
            prefix='!',
            initial_channels=[CHANNEL]
        )

    async def event_ready(self):
        print(f"✅ TTS Bot is live as {self.nick}")

    async def event_message(self, message):
        if message.author.name.lower() == BOT_USER.lower():
            return

        text = f"{message.author.name} says: {message.content}"
        print(text)
        enqueue_tts(text)

if __name__ == "__main__":
    bot = Bot()
    bot.run()
