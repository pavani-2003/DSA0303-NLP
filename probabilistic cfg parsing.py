import nltk
from nltk import PCFG
from nltk.parse import ViterbiParser

# Define a probabilistic context-free grammar
pcfg_grammar = PCFG.fromstring("""
    S -> NP VP [1.0]
    NP -> Det N [0.7] | N [0.3]
    VP -> V NP [0.4] | V [0.6]
    Det -> 'the' [0.6] | 'a' [0.4]
    N -> 'dog' [0.5] | 'cat' [0.5]
    V -> 'chases' [0.3] | 'meows' [0.7]
""")

# Create a PCFG parser
parser = ViterbiParser(pcfg_grammar)

# Input sentence
sentence = "the dog chases a cat"

# Tokenize the sentence
tokens = nltk.word_tokenize(sentence)

# Parse the sentence using PCFG
for tree in parser.parse(tokens):
    tree.pretty_print()

# Display the most probable parse tree
print("Most probable parse tree:")
most_probable_tree = parser.parse(tokens).__next__()
most_probable_tree.pretty_print()
