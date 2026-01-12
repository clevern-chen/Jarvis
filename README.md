# JARVIS Voice Assistant

A JARVIS-themed voice assistant web app with Iron Man Mark VII HUD styling.

## Features

- Hold-to-speak interface with arc reactor button
- Speech-to-Text via OpenAI Whisper
- AI responses via xAI Grok
- Text-to-Speech via OpenAI TTS
- Mobile-friendly HUD interface

## Quick Start

1. Clone and setup:

git clone https://github.com/clevern-chen/Jarvis.git
cd Jarvis
python -m venv venv
venv\Scriptsctivate
pip install -r requirements.txt

2. Create .env with your API keys:

OPENAI_API_KEY=sk-your-key
XAI_API_KEY=xai-your-key

3. Run: python app.py

4. For mobile: ngrok http 5000

## Usage

- Open the ngrok URL on your phone
- Hold the arc reactor button to speak
- Release to send audio
- JARVIS responds with text and voice

## License

MIT
