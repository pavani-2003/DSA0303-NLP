import spacy
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Load the English language model
nlp = spacy.load("en_core_web_sm")

def sentence_embedding(sentence, model):
    tokens = model(sentence)
    return np.mean([token.vector for token in tokens], axis=0)

def compute_coherence(text):
    sentences = [sent.text for sent in nlp(text).sents]
    embeddings = [sentence_embedding(sent, nlp) for sent in sentences]

    coherence_matrix = cosine_similarity(embeddings)
    np.fill_diagonal(coherence_matrix, 0)  # Set diagonal values to 0

    average_coherence = coherence_matrix.mean()
    return average_coherence

if __name__ == '__main__':
    text = input("Enter the text to evaluate coherence: ")
    coherence_score = compute_coherence(text)
    
    print(f"Text Coherence Score: {coherence_score:.2f}")
