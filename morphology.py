import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

# Sample text for analysis
text = "The quick brown foxes are jumping over the lazy dogs"

# Tokenize the text into words
words = word_tokenize(text)

# Initialize the Porter Stemmer and WordNet Lemmatizer
porter = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# Perform stemming and lemmatization
stemmed_words = [porter.stem(word) for word in words]
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]

# Print the original, stemmed, and lemmatized words
print("Original words:", words)
print("Stemmed words:", stemmed_words)
print("Lemmatized words:", lemmatized_words)
