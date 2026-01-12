# JARVIS - Voice Assistant Web App

A **JARVIS-themed Voice Assistant** web application with Iron Man Mark VII HUD styling. Hold-to-speak interface that works on mobile (iOS/Android) via ngrok tunneling.

## Architecture

```
[iPhone/Browser] --audio--> [Flask Server] ---> [OpenAI Whisper] (STT)
                                           ---> [xAI Grok] (LLM)
                                           ---> [OpenAI TTS] (Voice)
                 <--JSON+audio-------------
```

## Tech Stack

| Component | Technology |
|-----------|------------|
| Backend | Python (Flask) |
| Speech-to-Text | OpenAI Whisper API |
| LLM | xAI Grok (`grok-4-latest`) |
| Text-to-Speech | OpenAI TTS (`tts-1`, voice: `onyx`) |
| Frontend | HTML5, CSS3, JavaScript (MediaRecorder API) |
| Mobile Access | Ngrok tunneling |

## Directory Structure

```
Jarvis/
├── .env                  # API keys (not committed)
├── .gitignore
├── requirements.txt
├── app.py                # Flask server
├── JARVIS_Spec.md
└── templates/
    └── index.html        # HUD interface
```

## Setup

1. Create virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. Create `.env` file with your API keys:
   ```
   OPENAI_API_KEY=sk-your-openai-key
   XAI_API_KEY=xai-your-xai-key
   ```

3. Run the server:
   ```bash
   python app.py
   ```

4. For mobile access, use ngrok:
   ```bash
   ngrok http 5000
   ```

## Usage

- Open the ngrok URL on your phone
- Hold the arc reactor button to speak
- Release to send audio
- JARVIS will respond with text and voice