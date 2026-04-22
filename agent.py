def classify_input(text):
    text = text.lower()

    # Emotion detection
    if any(word in text for word in ["happy", "good", "great", "excited"]):
        emotion = "positive"
    else:
        emotion = "negative"

    # Intensity detection
    if any(word in text for word in ["very", "extremely", "too much", "highly"]):
        intensity = "high"
    else:
        intensity = "medium_low"

    # Cause detection
    if "work" in text or "job" in text:
        cause = "work"
    elif "family" in text or "friend" in text or "relationship" in text:
        cause = "relationship"
    elif "health" in text or "sick" in text:
        cause = "health"
    else:
        cause = "general"

    # Control detection
    if any(word in text for word in ["can", "will", "fix", "solve"]):
        control = "controllable"
    else:
        control = "uncontrollable"

    return emotion, intensity, cause, control


def decision_tree(emotion, intensity, cause, control):
    if emotion == "positive":
        if intensity == "high":
            return "Practice gratitude journaling"
        else:
            return "Reflect on what went well today"

    if emotion == "negative":
        if intensity == "high":
            if control == "controllable":
                return "Create an action plan to improve the situation"
            else:
                return "Practice acceptance and deep breathing"
        else:
            if cause == "work":
                return "Break your tasks into smaller steps and prioritize"
            elif cause == "relationship":
                return "Communicate openly and express your thoughts"
            elif cause == "health":
                return "Take rest and focus on self-care"
            else:
                return "Reflect calmly and reset your mindset"

    return "I'm not sure. Try reflecting calmly."


def agent():
    print("Daily Reflection Agent (type 'exit' to quit)\n")

    while True:
        user_input = input("Enter your reflection: ")

        if user_input.lower() == "exit":
            break

        emotion, intensity, cause, control = classify_input(user_input)
        response = decision_tree(emotion, intensity, cause, control)

        print("\nResponse:", response, "\n")


if __name__ == "__main__":
    agent()