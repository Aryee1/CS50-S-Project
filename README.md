# English–Twi Translator Chatbot

🎥 **Video Demo:** https://youtu.be/BkHLnRFHXmc  

---

## 📝 Description

The **English–Twi Translator Chatbot** is a web-based NLP application that translates text from English into Twi. It is built with **Flask**, **HTML/CSS**, and a pretrained multilingual model from **Hugging Face Transformers**.

The project explores how language technologies can support low-resource African languages like Twi. English–Twi translation is an important step toward improving digital accessibility for native speakers and highlighting the potential of AI language tools for underrepresented linguistic communities. It reflects a broader interest in **Natural Language Processing (NLP)**, **machine translation**, and computational tools for low-resource languages.

The app integrates both machine learning and web development concepts. It demonstrates:

- Flask backend integration  
- Frontend design with HTML templates and CSS  
- Basic NLP workflows such as tokenization, text preprocessing, and translation  

It combines a simple web interface with a language model to create an interactive system that translates user input and displays the result in real time.

Because few open-source English–Twi translation models currently exist, the app uses an **English–French** model from Hugging Face as a working prototype. This serves as a placeholder that simulates translation logic while maintaining the project’s structure and educational value. To provide real English–Twi functionality, a **JSON dictionary** performs basic word-level translations offline. This hybrid setup combines a pretrained translation model with a custom-built dictionary to show how a future fine-tuned model could be integrated seamlessly.

The system follows a hybrid translation approach:

1. When the user submits English text, the app first checks for matches in the local Twi dictionary.  
2. If no match is found, it uses the pretrained multilingual model to generate a translation.  

This design demonstrates a realistic development path for low-resource NLP systems. The model handles translation through Hugging Face’s `pipeline` API, while the Flask backend connects the translation logic to the web interface.

The user interface is simple and intuitive. Users type an English sentence, click **Translate**, and see the translation instantly. The layout focuses on clarity and minimalism using HTML, CSS, and Flask templates. The web app runs locally but can be deployed on cloud platforms such as **Render**, **Vercel**, or **Hugging Face Spaces**.

The project was built as the final project for **Harvard’s CS50x** course. Beyond fulfilling course requirements, it reflects a growing commitment to applied NLP research and a long-term goal of improving computational resources for African languages. Planned future improvements include fine-tuning a model specifically trained on Twi datasets to improve translation accuracy, support idiomatic expressions, and broaden vocabulary coverage.

---

## ⚙️ Features

- English text input with real-time translation output  
- Flask-based backend for model and dictionary integration  
- Simple, responsive web interface using HTML, CSS, and Flask templates  
- Offline English–Twi word lookup through a JSON dictionary  
- Scalable structure that supports future fine-tuned Twi translation models  
- Expandable design for additional features such as sentiment analysis or speech input/output  

---

## 📁 Project Structure

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
