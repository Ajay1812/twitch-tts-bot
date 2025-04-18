# 🟣 Twitch TTS Bot 🎙️

A real-time Twitch bot that reads out messages from your chat using **Text-to-Speech (TTS)**. Perfect for streamers who want to make their chat more interactive and fun.

> Built with Python, TwitchIO, gTTS, and pydub.

---

## 🎯 Features

- ✅ Reads out chat messages in real-time (TTS)
- ✅ In-memory audio playback (no file saving)
- ✅ Easy setup with `.env` file

## 🧰 Requirements

- Python 3.9+
- `ffmpeg` installed (for decoding mp3)
- Twitch account and a registered app (for OAuth token)

---

## 📦 Installation

1. **Clone the repo**

```bash
git clone https://github.com/Ajay1812/twitch-tts-bot.git
cd twitch-tts-bot
```

2. **Create and activate a virtual environment**

```sh
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**

```sh
pip3 install -r requirements.txt
```

4. **Set up environment variables**

    Create a **.env** file in the root folder:

```ini
# .env
TOKEN=oauth:your_oauth_token_here
CHANNEL=your_channel_name
BOT_USER=your_bot_username
```

> ⚠️ Get your OAuth token from your Twitch Developer Console. Redirect URL can be http://localhost.


## 🧠 How It Works
- Connects to your Twitch chat using TwitchIO

- Every new chat message is converted to speech using gTTS

- The audio is played directly from memory using pydub


## 📬 Contact

For any queries, reach out to:
📧 Email: [a.kumar01c@gmail.com]
🔗 GitHub: [https://github.com/Ajay1812]

Happy Coding! 🎉
