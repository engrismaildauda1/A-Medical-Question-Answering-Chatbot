import pandas as pd
from chatbot.preprocess import clean_text
from chatbot.responder import MedicalResponder

EMERGENCY_KEYWORDS = [
    "chest pain", "difficulty breathing",
    "severe bleeding", "unconscious"
]

def safety_check(text):
    return any(keyword in text for keyword in EMERGENCY_KEYWORDS)

def main():
    print("MediQuery: Medical Question-Answering Chatbot")
    print("Disclaimer: General medical information only.\n")

    data = pd.read_csv("data/medical_qa.csv")
    data.columns = data.columns.str.strip().str.lower()
    data["clean_question"] = data["question"].apply(clean_text)

    responder = MedicalResponder(
        data["clean_question"],
        data["answer"]
    )

    while True:
        user_input = input("User: ")
        if user_input.lower() == "bye":
            print("Bot: Take care. Stay healthy!")
            break

        cleaned = clean_text(user_input)

        if safety_check(cleaned):
            print("Bot: Please seek immediate medical attention.")
        else:
            print("Bot:", responder.get_answer(cleaned))

if __name__ == "__main__":
    main()
