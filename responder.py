from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class MedicalResponder:
    def __init__(self, questions, answers):
        self.answers = answers
        self.vectorizer = TfidfVectorizer()
        self.question_vectors = self.vectorizer.fit_transform(questions)

    def get_answer(self, user_input):
        user_vector = self.vectorizer.transform([user_input])
        similarity = cosine_similarity(user_vector, self.question_vectors)
        index = similarity.argmax()
        return self.answers.iloc[index]
