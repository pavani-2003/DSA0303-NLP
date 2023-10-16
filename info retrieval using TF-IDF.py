from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Sample documents
documents = [
    "The quick brown fox jumps over the lazy dog",
    "A lazy dog is resting in the sun",
    "A quick brown dog chases the fox",
    "The sun is shining brightly",
]

# Query
query = "lazy dog"

# Step 1: Initialize the TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer()

# Step 2: Fit and transform the documents
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

# Step 3: Transform the query
query_tfidf = tfidf_vectorizer.transform([query])

# Step 4: Calculate the cosine similarity between the query and documents
cosine_similarities = linear_kernel(query_tfidf, tfidf_matrix)

# Step 5: Sort documents by their similarity score
document_scores = list(enumerate(cosine_similarities[0]))
sorted_documents = sorted(document_scores, key=lambda x: x[1], reverse=True)

# Print the ranked documents
print("Ranking of documents for the query:", query)
for i, score in sorted_documents:
    print(f"Document {i + 1}: Similarity Score = {score:.4f}\n{documents[i]}\n")
