from transformers import MarianMTModel, MarianTokenizer

# Load the pre-trained model and tokenizer for English to French translation
model_name = "Helsinki-NLP/opus-mt-en-fr"
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)

def translate_english_to_french(text):
    # Tokenize and translate the input text
    inputs = tokenizer.encode(">>en<<" + text, return_tensors="pt", max_length=512, truncation=True)
    translation = model.generate(inputs, max_length=150, num_return_sequences=1, num_beams=4)

    # Decode and return the translated text
    translated_text = tokenizer.decode(translation[0], skip_special_tokens=True)
    return translated_text

if __name__ == "__main__":
    english_text = input("Enter English text to translate to French: ")
    french_translation = translate_english_to_french(english_text)

    print("French Translation:")
    print(french_translation)
