import nltk

nltk.download('punkt')

sentence = "Tokenization is an important step in NLP."

tokens = nltk.word_tokenize(sentence)

print(tokens)
