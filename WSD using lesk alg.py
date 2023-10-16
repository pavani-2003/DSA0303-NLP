import nltk
from nltk.corpus import wordnet
from nltk.wsd import lesk

# Sample sentence with an ambiguous word
sentence = "He saw the bat fly over the baseball field."

# Tokenize the sentence
words = nltk.word_tokenize(sentence)

# Define the target word and its part of speech
target_word = "bat"
pos = "n"  # "n" for noun; you can adjust this for other parts of speech

# Use the Lesk algorithm to disambiguate the target word
synset = lesk(words, target_word, pos)

if synset:
    # Print the most likely sense and its definition
    print(f"Word: {target_word}")
    print(f"Sense: {synset.name()}")
    print(f"Definition: {synset.definition()}")

else:
    print(f"No suitable sense found for '{target_word}' in this context.")
