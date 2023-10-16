import nltk
from nltk.corpus import wordnet

# Download WordNet data (if not already downloaded)
nltk.download("wordnet")

# Define a word to explore its meanings
word = "example"

# Get synsets for the word
synsets = wordnet.synsets(word)

if synsets:
    # Display the word and its meanings (synsets)
    print(f"Word: {word}")
    print("Meanings (Synsets):")

    for synset in synsets:
        print(f"Synset: {synset.name()}")
        print(f"Definition: {synset.definition()}")

        # Get hypernyms (more general terms)
        hypernyms = synset.hypernyms()
        if hypernyms:
            print("Hypernyms:")
            for hypernym in hypernyms:
                print(f"- {hypernym.name()}")

        # Get hyponyms (more specific terms)
        hyponyms = synset.hyponyms()
        if hyponyms:
            print("Hyponyms:")
            for hyponym in hyponyms:
                print(f"- {hyponym.name()}")

        # Get synonyms
        synonyms = synset.lemmas()
        if synonyms:
            print("Synonyms:")
            for synonym in synonyms:
                print(f"- {synonym.name()}")

        # Get antonyms
        antonyms = synset.lemmas()[0].antonyms()
        if antonyms:
            print("Antonyms:")
            for antonym in antonyms:
                print(f"- {antonym.name()}")

        print()

else:
    print(f"No synsets found for the word: {word}")
