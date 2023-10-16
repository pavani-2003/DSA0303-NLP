import random

# Sample input text
input_text = "This is a simple example of a bigram text generator. It generates text based on bigram model."

# Tokenize the text
tokens = input_text.split()

# Build the bigram model
bigram_model = {}
for i in range(len(tokens) - 1):
    current_word = tokens[i]
    next_word = tokens[i + 1]
    if current_word in bigram_model:
        bigram_model[current_word].append(next_word)
    else:
        bigram_model[current_word] = [next_word]

# Generate text using the bigram model
generated_text = []
current_word = random.choice(tokens)  # Start with a random word
generated_text.append(current_word)

while current_word in bigram_model:
    next_word = random.choice(bigram_model[current_word])
    generated_text.append(next_word)
    current_word = next_word

# Combine the generated words into a sentence
generated_sentence = ' '.join(generated_text)

print(generated_sentence)
