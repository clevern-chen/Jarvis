import os
import base64
import tempfile
from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Separate clients: OpenAI for Whisper, x.ai for Grok
openai_client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

xai_client = OpenAI(
    api_key=os.environ.get("XAI_API_KEY"),
    base_url="https://api.x.ai/v1"
)

SYSTEM_PROMPT = """You are JARVIS. Speak with a refined British accent. 
Be concise, witty, and robotic. Address the user as 'Sir'."""

@app.route("/")
def index():
    # Ensure you created the 'templates' folder!
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process_audio():
    if "audio" not in request.files:
        return jsonify({"error": "No audio file"}), 400

    audio_file = request.files["audio"]
    
    # FIXED: Use .m4a or determine extension dynamically. 
    # iOS sends mp4/m4a, Desktop sends webm. Whisper handles m4a well.
    with tempfile.NamedTemporaryFile(delete=False, suffix=".m4a") as tmp:
        audio_file.save(tmp.name)
        tmp_path = tmp.name

    try:
        # 1. EAR: Transcribe (Whisper via OpenAI)
        with open(tmp_path, "rb") as f:
            transcription = openai_client.audio.transcriptions.create(
                model="whisper-1",
                file=f
            )
        user_text = transcription.text

        # 2. BRAIN: Think (Grok via x.ai)
        response = xai_client.chat.completions.create(
            model="grok-4-latest", 
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_text}
            ],
            max_tokens=150
        )

        jarvis_reply = response.choices[0].message.content

        # 3. VOICE: Text-to-Speech (OpenAI TTS)
        speech_response = openai_client.audio.speech.create(
            model="tts-1",
            voice="onyx",  # Deep British-ish voice, good for JARVIS
            input=jarvis_reply
        )
        audio_base64 = base64.b64encode(speech_response.content).decode('utf-8')

        return jsonify({
            "transcription": user_text,
            "response": jarvis_reply,
            "audio": audio_base64
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        # Cleanup temp file
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)