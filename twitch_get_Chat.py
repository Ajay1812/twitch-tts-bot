from twitchio.ext import commands
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import io
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('TOKEN')
CHANNEL = os.getenv('CHANNEL')
BOT_USER = os.getenv('BOT_USER')

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

        try:
            # Generate speech to a memory stream
            mp3_fp = io.BytesIO()
            tts = gTTS(text=text, lang='en')
            tts.write_to_fp(mp3_fp)
            mp3_fp.seek(0)

            # Load and play using pydub
            audio = AudioSegment.from_file(mp3_fp, format="mp3")
            play(audio)

        except Exception as e:
            print("❌ TTS Error:", e)

if __name__ == "__main__":
    bot = Bot()
    bot.run()
