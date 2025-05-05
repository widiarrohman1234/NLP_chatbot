import json
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load intents
with open("dataset/intents_health_eye.json") as file:
    data = json.load(file)

# Siapkan data training dari pola
all_patterns = []
tags = []
for intent in data["intents"]:
    for pattern in intent["patterns"]:
        all_patterns.append(pattern)
        tags.append(intent["tag"])

# TF-IDF vectorizer untuk input dan pola
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(all_patterns)

# Fungsi utama chatbot
def get_response(user_input):
    user_vec = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vec, X)
    idx = similarity.argmax()
    score = similarity[0][idx]

    if score < 0.3:
        tag = "fallback"
    else:
        tag = tags[idx]

    for intent in data["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])
