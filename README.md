# English–Twi Translator Chatbot

#### 🎥 Video demo: [https://youtu.be/BkHLnRFHXmc](https://youtu.be/BkHLnRFHXmc)

---

## Description

The **English–Twi Translator Chatbot** is a small web-based prototype that explores how to connect a neural translation model with a simple English–Twi dictionary inside a Flask application.

Because there are very few open English–Twi machine translation models, the current version uses:

- a pretrained **English–French translation model** from Hugging Face’s Transformers library as a stand-in neural component  
- a **local JSON dictionary** for basic English–Twi word and phrase lookup  

The goal is to show the end-to-end architecture of a translation chatbot, while keeping the Twi side honest about its current limitations.

This project was built as my **final project for Harvard’s CS50x** and reflects my interest in **NLP for low-resource African languages**, especially Twi.

---

## Features

- Web interface for entering English text and viewing translation output  
- Flask backend that combines a neural translation model with a JSON dictionary  
- Simple HTML/CSS frontend using Flask templates  
- Local English–Twi word translations stored in `data/dictionary.json`  
- Project structure that can later be extended with a real English–Twi model

---

## Limitations

This is a prototype, not a full English–Twi machine translation system.

- The neural model currently handles **English → French**, not English → Twi  
- Twi support is limited to **dictionary lookups** for individual words and short phrases  
- There is **no large Twi parallel corpus** or Twi-specific model in this version  

The idea is to have the infrastructure in place so that a future English–Twi model or Twi-trained checkpoint can be dropped in when suitable data becomes available.

---

## Setup and usage

### 1. Clone the repository

```bash
git clone https://github.com/USERNAME/english-twi-chatbot.git
cd english-twi-chatbot
````

Replace `USERNAME` with your GitHub username if needed.

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv .venv

# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1

# macOS / Linux
# source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

This installs Flask, transformers, and any other Python libraries used by the app.

### 4. Run the Flask app

```bash
python app.py
```

By default Flask will run on `http://127.0.0.1:5000`. Open that address in your browser to use the chatbot.

---

## How it works (high level)

1. The user enters an English sentence in the web interface.
2. The Flask backend splits the text and:

   * looks up known words and short phrases in the **English–Twi JSON dictionary**, and
   * uses a pretrained **English–French translation model** to demonstrate how a neural model is integrated.
3. The response is rendered back into the chat interface.

The current behaviour is deliberately simple. The main focus is the **architecture**: routing messages between the browser, Flask, the model wrapper, and the dictionary.

---

## Project structure

```text
english-twi-chatbot/
│
├── app.py                  # Main Flask application
├── requirements.txt        # Project dependencies
│
├── data/
│   └── dictionary.json     # Local English–Twi word dictionary
│
├── static/
│   └── style.css           # CSS styling for the web interface
│
└── templates/
    └── index.html          # Frontend HTML layout
```

---

## Design choices

* **Flask** was chosen because it is easy to connect HTTP endpoints to Python functions and external models without a lot of boilerplate.
* A **pretrained English–French model** is used as a proxy to show how a neural translation model can be wired into a chatbot, even though it is not trained on Twi.
* The **JSON dictionary** keeps the Twi side grounded. It shows how local resources can provide basic English–Twi translations even in the absence of a large Twi model or internet access.
* The code and folder structure are kept simple so that a future English–Twi model or Twi-trained checkpoint can replace the current proxy with minimal changes.

---

## Future work

Planned or possible extensions include:

* Replacing the English–French model with:

  * a multilingual model that supports Twi more directly, or
  * a custom model fine-tuned on English–Twi data when such a corpus is available
* Expanding `data/dictionary.json` with more comprehensive Twi vocabulary and phrases
* Adding basic evaluation on held-out Twi examples once a proper dataset exists
* Improving the chat interface (history, clearer separation of dictionary vs model outputs)

For now, this repository should be read as a **working prototype** that shows how web development, neural translation models, and low-resource language resources can be combined in a single project.
