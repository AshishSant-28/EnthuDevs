from speech_utils import process_speech as capture_speech
from emotions_utils import detect_emotion as classify_emotion
from chat_utils import get_response as generate_response_ml
from tts_utils import text_to_speech as synthesize_speech


def main():
    # Loop to keep the conversation going
    while True:
        # 1. Capture user speech and convert to text
        user_text = capture_speech()
        if not user_text:
            continue

        # Check for exit commands
        if user_text.lower() in ['exit', 'quit', 'bye']:
            farewell = "Goodbye! Have a great day!"
            print(f"🤖 MindfulMate: {farewell}")
            synthesize_speech(farewell)
            break

        # Display user input
        print(f"📝 You: {user_text}")

        # 2. Classify emotion (optional theming/logging)
        label, score = classify_emotion(user_text)
        print(f"🔍 Emotion: {label} ({score:.2f})")

        # 3. Generate chatbot response
        bot_reply = generate_response_ml(user_text)
        print(f"🤖 MindfulMate: {bot_reply}")

        # 4. Speak the chatbot response
        synthesize_speech(bot_reply)


if __name__ == "__main__":
    main()
