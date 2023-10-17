import spacy
import nltk
from nltk.corpus import wordnet

# Download the WordNet resource
nltk.download('wordnet')

# Load the English language model (small model)
nlp = spacy.load("en_core_web_sm")

def extract_noun_phrases(sentence):
    # Process the input sentence using spaCy
    doc = nlp(sentence)

    noun_phrases = []

    for chunk in doc.noun_chunks:
        head_noun = chunk.root.text
        # Find WordNet synsets for the head noun
        synsets = wordnet.synsets(head_noun)
        if synsets:
            definition = synsets[0].definition()
            noun_phrases.append((str(chunk), definition))

    return noun_phrases

if __name__ == '__main__':
    sentence = input("Enter a sentence: ")
    noun_phrases = extract_noun_phrases(sentence)
    
    if noun_phrases:
        print("Noun Phrases and Their Meanings:")
        for noun_phrase, definition in noun_phrases:
            print(f"{noun_phrase}: {definition}")
    else:
        print("No noun phrases found in the sentence.")
