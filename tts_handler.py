from gtts import gTTS
from pydub import AudioSegment, silence
from pydub.playback import play
import io
import threading
import queue
import time

## Shared queue for TTS text messages
tts_queue = queue.Queue()

def tts_worker():
    while True:
        text = tts_queue.get()
        if text is None:
            break  

        try:
            # Generate speech to a memory stream
            mp3_fp = io.BytesIO()
            tts = gTTS(text=text, lang='en')
            tts.write_to_fp(mp3_fp)
            mp3_fp.seek(0)

            # Load and play using pydub
            audio = AudioSegment.from_file(mp3_fp, format="mp3")
            audio = audio.fade_out(200) 
            play(audio)

            time.sleep(5)
        except Exception as e:
            print("❌ TTS Error:", e)
        finally:
            tts_queue.task_done()

def start_tts_worker():
    threading.Thread(target=tts_worker, daemon=True).start()

def enqueue_tts(text):
    tts_queue.put(text)
