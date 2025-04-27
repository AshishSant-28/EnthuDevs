import io
import base64
from flask import Flask, render_template, jsonify
from chat_utils import return_output
from tts_utils import translate_text_to_language
from gtts import gTTS

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_speech', methods=['GET'])
def process_speech_api():
    # 1. Get the chatbot’s English reply
    reply = return_output()             # e.g. "I'm doing great, thank you!"
    
    # 2. Translate that reply into Hindi text
    hindi_text = translate_text_to_language(reply, target_language='hi')
    
    # 3. Generate MP3 into an in-memory buffer
    tts = gTTS(text=hindi_text, lang='hi', slow=False)
    buf = io.BytesIO()
    tts.write_to_fp(buf)
    buf.seek(0)

    # 4. Base64-encode and send back
    b64 = base64.b64encode(buf.read()).decode('utf-8')
    return jsonify({
        'en': reply,
        'hi': hindi_text,
        'audio_data': b64
    })

if __name__ == '__main__':
    app.run(debug=True)
