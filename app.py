from flask import Flask, render_template, request
import json
from transformers import pipeline

app = Flask(__name__)

# Load bilingual dictionary
with open("data/dictionary.json", "r", encoding="utf-8") as f:
    dictionary = json.load(f)

# Load small translation model 
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fr")

def translate_to_twi(text):
    text = text.lower().strip()
    
    # Try dictionary first
    if text in dictionary:
        return dictionary[text]
    
    # Otherwise use the transformer model
    try:
        result = translator(text, max_length=100)
        translation = result[0]['translation_text']
        return f"(AI-based) {translation}"
    except Exception as e:
        return f"Error: {e}"

@app.route("/", methods=["GET", "POST"])
def index():
    translation = None
    if request.method == "POST":
        text = request.form["text"]
        translation = translate_to_twi(text)
    return render_template("index.html", translation=translation)

if __name__ == "__main__":
    app.run(debug=True)