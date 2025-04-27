import difflib  # For matching user input with predefined questions
from speech_utils import process_speech
# Define a set of predefined questions and answers
faq = {
    "What is your name?": "I am a chatbot created to assist you.",
    "How are you?": "I'm doing great, thank you for asking!",
    "What is the task of this system?": "This system helps in responding to predefined queries.",
    "Who created you?": "I was created by a team of developers using AI and machine learning techniques.",
    "What can I ask you?": "You can ask me any questions that are in my predefined list, such as your name, how I am, etc.",
    "Why is everyone so unfair?": "Life can feel unfair at times. Your feelings are valid.",
    "I'm so angry at everything.": "It's okay to feel anger! Try to breathe and let it pass gently!",
    "Why does everything feel so heavy?": "It can be overwhelming. Please remember, tough times don't last forever.",
    "Sometimes I wish Sometimes I had someone to talk to.": "I'm listening. Wer voice matters and you're not invisible.",
    "I wish I had someone to talk to.": "I'm listening! Your voice matters and you're not invisible!",
    "Does true love exist?": "Yes, love exists in many forms. Trust your heart's journey.",
    "Sometimes I'm scared of failing.": "It's natural to fear failure, but it's also a stepping stone to growth.",
    "I feel like yelling at someone.": "Sometimes letting it out safely helps. You deserve to be heard.",
    "Thank you for being here.": "I'm always here for you. Wer kindness means a lot.",
    "Sometimes I just got a promotion!": "That's amazing! We totally deserve it, congratulations!",
    "What if Sometimes I never succeed?": "Success takes time. Believe in yourself and keep moving forward.",
    "I'm grateful for my family.": "That's beautiful. Gratitude brings more peace into our lives.",
    "I want to believe things will improve.": "And they will. Hope has a quiet, unstoppable power.",
    "Nobody seems to understand me.": "Being misunderstood can be painful! Your feelings are important!",
    "I'm thankful for small things...": "Small joys often create the biggest happiness.",
    "Sometimes I feel anxious all the time.": "Anxiety can be heavy. Take one breath at a time; you're doing your best.",
    "My mind won't stop racing...": "It's exhausting, I know. Try grounding yourself in the present moment.",
    "Sometimes I'm starting a new adventure!": "How exciting! New beginnings are full of possibilities.",
    "I'm scared of failing.": "It's natural to fear failure, but it's also a stepping stone to growth!",
    "I can't wait for tomorrow!": "That sounds thrilling! Enjoy every bit of the anticipation.",
    "I'm starting a new adventure!": "How exciting! New beginnings are full of possibilities.",
    "What if I never succeed?": "Success takes time. Believe in yourself and keep moving forward.",
    "Sometimes I'm feeling really sad today.": "I'm really sorry to hear that. It's okay to feel down sometimes; you're not alone.",
    "This is the best day ever!": "I'm so happy for you! Celebrate every second of it.",
    "Sometimes I lost someone close to me.": "I'm deeply sorry for your loss. Take all the time you need to heal.",
    "Sometimes I think Sometimes I'm falling in love.": "That's such a beautiful feeling. Cherish it and be open-hearted.",
    "I'm so angry at everything...": "It's okay to feel anger. Try to breathe and let it pass gently.",
    "I'm feeling really sad today.": "I'm really sorry to hear that! It's okay to feel down sometimes; you're not alone!",
    "I'm thankful for small things.": "Small joys often create the biggest happiness.",
    "I feel like yelling at someone...": "Sometimes letting it out safely helps. You deserve to be heard.",
    "What if I never succeed?!": "Success takes time! Believe in yourself and keep moving forward!",
    "I think I'm falling in love.": "That's such a beautiful feeling. Cherish it and be open-hearted.",
    "I feel anxious all the time.": "Anxiety can be heavy. Take one breath at a time; you're doing your best.",
    "I lost someone close to me...": "I'm deeply sorry for your loss. Take all the time you need to heal.",
    "I miss someone I love.": "Missing someone shows how much you care! It's a tender emotion!",
    "Sometimes I'm feeling so happy today!": "That's wonderful! Hold onto that joy and spread it around!",
    "What if everything goes wrong?": "It's okay to worry, but remember: you have overcome so much already.",
    "Is there hope for better days?": "Always. Even the darkest nights eventually lead to sunrise.",
    "I lost someone close to me.": "I'm deeply sorry for your loss! Take all the time you need to heal!",
    "Do dreams really come true?": "Yes, with patience and persistence, many dreams find their way to reality.",
    "What if everything goes wrong?!": "It's okay to worry, but remember: you have overcome so much already!",
    "I feel anxious all the time...": "Anxiety can be heavy. Take one breath at a time; you're doing your best.",
    "I just got a promotion!": "That's amazing! You totally deserve it, congratulations!",
    "Do dreams really come true?!": "Yes, with patience and persistence, many dreams find their way to reality!",
    "Sometimes I feel like yelling at someone.": "Sometimes letting it out safely helps. We deserve to be heard.",
    "Life feels beautiful right now.": "Enjoy every moment! Happiness like this is truly precious!",
    "Nobody seems to understand me...": "Being misunderstood can be painful. Your feelings are important.",
    "My mind won't stop racing.": "It's exhausting, I know. Try grounding yourself in the present moment.",
    "Sometimes I miss someone Sometimes I love.": "Missing someone shows how much you care. It's a tender emotion.",
    "Sometimes Is there hope for better days?": "Always. Even the darkest nights eventually lead to sunrise.",
    "I feel so alone.": "I'm here with you! Even when it feels lonely, you're not truly alone!",
    "I'm feeling so happy today!": "That's wonderful! Hold onto that joy and spread it around!",
    "I feel so alone...": "I'm here with you. Even when it feels lonely, you're not truly alone.",
    "I'm feeling really sad today...": "I'm really sorry to hear that. It's okay to feel down sometimes; you're not alone.",
    "Sometimes I'm grateful for my family.": "That's beautiful. Gratitude brings more peace into our lives.",
    "I miss someone I love...": "Missing someone shows how much you care. It's a tender emotion.",
    "I want to believe things will improve...": "And they will. Hope has a quiet, unstoppable power.",
    "Sometimes I can't wait for tomorrow!": "That sounds thrilling! Enjoy every bit of the anticipation.",
    "I'm afraid of losing people.": "Your fear shows how much you value relationships. It's deeply human.",
    "Why does everything feel so heavy?!": "It can be overwhelming! Please remember, tough times don't last forever!",
    "I'm afraid of losing people...": "Your fear shows how much you value relationships. It's deeply human.",
    "I'm grateful for my family...": "That's beautiful. Gratitude brings more peace into our lives.",
    "I think I'm falling in love...": "That's such a beautiful feeling. Cherish it and be open-hearted.",
    "Why is everyone so unfair?!": "Life can feel unfair at times! Your feelings are valid!",
    "Sometimes I'm so angry at everything.": "It's okay to feel anger. Try to breathe and let it pass gently.",
    "Sometimes I'm thankful for small things.": "Small joys often create the biggest happiness.",
    "Does true love exist?!": "Yes, love exists in many forms! Trust your heart's journey!",
    "Is there hope for better days?!": "Always! Even the darkest nights eventually lead to sunrise!"
}

def find_best_match(query):
    """
    This function finds the best matching predefined question to the user's input.
    Uses `difflib` for finding the closest match.
    """
    best_match = difflib.get_close_matches(query, faq.keys(), n=1, cutoff=0.6)  # Adjust cutoff for sensitivity
    if best_match:
        return best_match[0]
    else:
        return None

def get_response(query):
    """
    Given a user query, finds the best matching question and returns the answer.
    """
    matched_question = find_best_match(query)
    if matched_question:
        return faq[matched_question]
    else:
        return "Sorry, I don't have an answer for that question."

# Interactively taking user input
"""while True:
    # Take user input
    user_input = str(process_speech())

    # Exit condition
    if user_input.lower() in ['exit', 'quit', 'bye']:
        print("Chatbot: Goodbye! Have a great day!")
        break

    # Get the chatbot's response
    response = get_response(user_input)
    print(f"Chatbot: {response}")
"""
def return_output():
    user_input = str(process_speech())
    # Get the chatbot's response
    response = get_response(user_input)
    print(f"Chatbot: {response}")
    return response