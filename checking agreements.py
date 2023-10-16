import nltk
from nltk import CFG
from nltk.parse import ChartParser
from nltk.tree import Tree

# Define a context-free grammar for subject-verb agreement
grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N
    VP -> V
    Det -> 'the' | 'a'
    N -> 'dog' | 'cat' | 'dogs' | 'cats'
    V -> 'chases' | 'chase'
""")

# Create a parser based on the defined grammar
parser = ChartParser(grammar)

def check_agreement(sentence):
    tokens = nltk.word_tokenize(sentence)
    for tree in parser.parse(tokens):
        return check_tree_agreement(tree, None)

def check_tree_agreement(tree, subject=None):
    if isinstance(tree, Tree):
        if tree.label() == 'NP':
            # Check for noun phrase
            subject = tree[1].leaves()[0]
        elif tree.label() == 'VP':
            # Check for verb phrase
            verb = tree[0].leaves()[0]
            if subject:
                if verb == 'chases' and subject.endswith('s'):
                    return "Agreement error: Subject and verb do not agree."
                if verb == 'chase' and not subject.endswith('s'):
                    return "Agreement error: Subject and verb do not agree."
        for subtree in tree:
            result = check_tree_agreement(subtree, subject)
            if result:
                return result

    return None

# Usage
sentence = "the dog chases a cat"
result = check_agreement(sentence)
if result:
    print(result)
else:
    print("No agreement errors found in the sentence.")
