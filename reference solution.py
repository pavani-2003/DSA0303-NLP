import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

def perform_coreference_resolution(text):
    # Process the input text using spaCy
    doc = nlp(text)

    # Iterate through the identified coreferent clusters
    for cluster in doc._.coref_clusters:
        main_reference = cluster.main
        references = [mention for mention in cluster.mentions if mention != main_reference]
        print(f"Main Reference: {main_reference.text}")
        print(f"References: {[mention.text for mention in references]}\n")

if __name__ == '__main__':
    text = input("Enter a text for coreference resolution: ")
    perform_coreference_resolution(text)
