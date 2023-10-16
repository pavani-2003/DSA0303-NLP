import re

def rule_based_pos_tagger(word):
    if re.match(r'\d+$', word):
        return 'NUM'
    elif re.match(r'.*ly$', word):
        return 'ADV'
    elif re.match(r'.*ing$', word):
        return 'VERB'
    elif re.match(r'^[A-Z][a-z]*$', word):
        return 'NOUN'
    elif re.match(r'^[A-Z]*$', word):
        return 'NOUN'
    elif re.match(r'^[A-Z]*[a-z]*ed$', word):
        return 'VERB'
    elif re.match(r'^[A-Z]*[a-z]*es$', word):
        return 'VERB'
    elif re.match(r'^[A-Z]*[a-z]*ing$', word):
        return 'VERB'
    else:
        return 'UNKNOWN'

# Sample text for tagging
text = "The quick brown fox is jumping over 123 dogs."

# Tokenize the text into words
words = text.split()

# Perform POS tagging using the rule-based tagger
pos_tags = [rule_based_pos_tagger(word) for word in words]

# Print the tagged words
for word, pos_tag in zip(words, pos_tags):
    print(f'{word}: {pos_tag}')
