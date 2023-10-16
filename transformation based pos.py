import nltk
nltk.data.path.append("/path/to/nltk_data")


# Sample text
text = "This is a simple example of transformation-based tagging."

# Tokenize the text into words
words = nltk.word_tokenize(text)

# Define transformation rules (example rules)
rules = [
    (r'ing$', 'VBG'),  # Gerund verbs ending in 'ing' are tagged as VBG
    (r'ed$', 'VBD'),   # Past tense verbs ending in 'ed' are tagged as VBD
    (r'^[A-Z][a-z]*$', 'NNP'),  # Proper nouns start with a capital letter
    (r'.*', 'NN')      # Default: tag as noun
]

# Apply the transformation rules to tag the words
def transform_tagging(text, rules):
    tagged_words = []
    for word in text:
        for pattern, tag in rules:
            if nltk.re.match(pattern, word):
                tagged_words.append((word, tag))
                break
        else:
            tagged_words.append((word, 'NN'))  # Default tag
    return tagged_words

tagged_words = transform_tagging(words, rules)

# Print the tagged words
for word, tag in tagged_words:
    print(f"{word}: {tag}")
