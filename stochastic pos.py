import nltk

# Download the Penn Treebank POS corpus (if not already downloaded)
nltk.download('treebank')

# Sample text for POS tagging
text = "This is a simple example of a POS tagging algorithm."

# Tokenize the text into words
tokens = nltk.word_tokenize(text)

# Load the Penn Treebank corpus
corpus = nltk.corpus.treebank

# Train a unigram POS tagger
unigram_tagger = nltk.UnigramTagger(corpus.tagged_sents())

# Perform POS tagging
pos_tags = unigram_tagger.tag(tokens)

# Print the tagged words
for word, pos_tag in pos_tags:
    print(f'{word}: {pos_tag}')
