from transformers import pipeline

# Load a ready-to-use emotion detection model
emotion_classifier = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion", return_all_scores=False)

# A function to predict emotion
def detect_emotion(text):
    result = emotion_classifier(text)[0]
    emotion = result['label']
    confidence = round(result['score'], 2)  # rounding off the score
    return emotion, confidence

# Test examples
texts = [
    "I am feeling very happy today!",
    "This is so frustrating and annoying!",
    "I'm scared of what might happen.",
    "I love spending time with my family."
]

# Predict emotions
for sentence in texts:
    label, score = detect_emotion(sentence)
    print(f"Text: {sentence}")
    print(f"Detected Emotion: {label} (Confidence: {score})\n")


