#MediQuery: A Medical Question-Answering Chatbot
#Overview

MediQuery is a Python-based medical question-answering chatbot designed to provide general health information using a retrieval-based Natural Language Processing (NLP) approach. The system identifies the most relevant answer from a medical question–answer dataset using TF-IDF vectorization and cosine similarity.

This project is intended for educational and informational purposes only and does not provide medical diagnosis or treatment.

#Medical Disclaimer

This chatbot provides general medical information only and is not a substitute for professional medical advice. Users experiencing serious symptoms should consult a qualified healthcare professional.

#Key Features

Retrieval-based medical question answering

TF-IDF and cosine similarity for relevance matching

Text preprocessing for improved accuracy

Built-in safety layer for emergency keyword detection

Runs in Google Colab, local systems, and cloud environments

#Dataset

Format: CSV

Columns: question, answer

Public, non-clinical, and de-identified data

#Methodology

Preprocess dataset questions and user input

Convert text to TF-IDF vectors

Compute cosine similarity

Return the most relevant answer

Redirect emergency cases to medical professionals

#Results

The chatbot demonstrates effective performance for answering common medical questions while maintaining safety and ethical constraints.
