import nltk
from nltk.tag import CRFTagger
from nltk.corpus import nps_chat

# Download the nps_chat dataset
nltk.download('nps_chat')

# Load a pre-trained dialog act tagger (CRFTagger)
tagger = CRFTagger()
tagger.set_model_file(nps_chat._path + '/crf_model_file')

def recognize_dialog_acts(text):
    # Tokenize the input text into words
    words = nltk.word_tokenize(text)
    
    # Use the pre-trained dialog act tagger to label the words
    tagged_words = tagger.tag(words)
    
    # Extract dialog acts from the tagged words
    dialog_acts = [tag for word, tag in tagged_words]
    
    return dialog_acts

if __name__ == '__main__':
    conversation = input("Enter a conversation: ")
    dialog_acts = recognize_dialog_acts(conversation)
    
    print("Recognized Dialog Acts:")
    for act in dialog_acts:
        print(act)
