from flask import Flask, request, jsonify, render_template
from machinetranslation import english_to_french, french_to_english

app = Flask(__name__)

@app.route('/')
def home():
    """
    Endpoint that renders the index.html template
    """
    return render_template('index.html')

@app.route('/eng_fr', methods=['POST'])
def english_to_french_endpoint():
    """
    Endpoint that translates English to French using the english_to_french function from the machinetranslation package
    """
    text = request.json['text']
    translation = english_to_french(text)
    return jsonify({'translation': translation})

@app.route('/fr_eng', methods=['POST'])
def french_to_english_endpoint():
    """
    Endpoint that translates French to English using the french_to_english function from the machinetranslation package
    """
    text = request.json['text']
    translation = french_to_english(text)
    return jsonify({'translation': translation})
    
if __name__ == '__main__':
    app.run()
