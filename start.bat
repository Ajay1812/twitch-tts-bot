@echo off
echo 🚀 Starting Twitch TTS Bot...

REM If using a virtual environment, activate it (uncomment if needed)
cd .venv\Scripts
call activate.bat
cd ..\..

REM
python bot.py

pause
