MediQuery: A Medical Question-Answering Chatbot

Introduction

Access to reliable healthcare information is often limited, particularly for individuals seeking preliminary understanding of medical conditions. With the advancement of artificial intelligence in healthcare, conversational agents such as chatbots can assist in providing general medical information and promoting health awareness.

MediQuery is a medical question-answering chatbot designed to respond to user queries by retrieving relevant answers from a trusted medical question–answer dataset. The system is implemented in Python using Natural Language Processing (NLP) techniques, specifically TF-IDF vectorization and cosine similarity, to identify the most relevant response.

This project is intended strictly for educational and informational purposes and does not provide medical diagnosis or treatment recommendations.

Medical Disclaimer

This chatbot provides general medical information only.
It is not a substitute for professional medical advice, diagnosis, or treatment.
Users experiencing serious or persistent symptoms should consult a qualified healthcare professional or seek emergency medical care.

Dataset Description

The chatbot uses a medical question–answer dataset consisting of pairs of commonly asked medical questions and their corresponding informational answers.

Dataset Characteristics

Format: CSV (Comma-Separated Values)

Columns:

question – Medical-related user questions

answer – Informational responses

Nature of Data:

Publicly available

Non-clinical

Contains no personal or patient-identifiable information

The dataset acts as a knowledge base from which relevant responses are retrieved.

Text Preprocessing

To ensure accurate matching between user input and stored questions, text preprocessing is applied.

Preprocessing Steps

Conversion of text to lowercase

Removal of punctuation

Normalization for consistency

Purpose

Text preprocessing reduces noise and ensures uniform representation, thereby improving similarity matching accuracy.

Question-Answering Methodology

MediQuery employs a retrieval-based approach rather than a generative model.

Techniques Used

TF-IDF (Term Frequency–Inverse Document Frequency):
Converts textual questions into numerical vectors that represent word importance.

Cosine Similarity:
Measures similarity between the user query vector and stored question vectors.

Workflow

Dataset questions are vectorized using TF-IDF.

User input is preprocessed and vectorized.

Cosine similarity is computed.

The answer corresponding to the most similar question is returned.

This approach is efficient, transparent, and explainable, making it suitable for medical information systems.

Safety Layer

To ensure ethical and safe usage, the chatbot incorporates a safety mechanism.

Safety Features

Detection of emergency-related keywords (e.g., chest pain, difficulty breathing)

Automatic redirection advising users to seek immediate medical attention

This layer prevents the chatbot from responding in potentially life-threatening situations.

Chatbot Execution

The chatbot runs in an interactive loop that allows users to:

Enter medical-related questions

Receive relevant informational responses

Exit the system by typing bye

The chatbot is text-based and can be executed in Google Colab, local environments, or cloud platforms.

Results and Observations

The chatbot successfully retrieves relevant answers for common medical queries.

TF-IDF-based similarity provides accurate matching for well-phrased questions.

The safety layer appropriately handles emergency-related inputs.

Overall, the system demonstrates effective performance for basic medical question answering.

Conclusion

This focused on:

Structuring the project clearly

Implementing safe and ethical chatbot behavior

Ensuring the codebase and documentation are readable, organized, and evaluation-ready

At the completion of this phase, MediQuery is a functional and well-documented medical chatbot suitable for academic demonstration and future enhancement.