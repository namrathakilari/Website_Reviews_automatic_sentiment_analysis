from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import re
import nltk
nltk.download('stopwords', quiet=True)
from nltk.corpus import stopwords

app = Flask(__name__)
CORS(app)  # allows your website to talk to this server

# Load your trained model
with open('sentiment_model.pkl', 'rb') as f:
    model = pickle.load(f)

def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[^a-z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    stop_words = set(stopwords.words('english'))
    text = ' '.join([w for w in text.split() if w not in stop_words])
    return text

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    review = data.get('review', '')
    cleaned = clean_text(review)
    prediction = model.predict([cleaned])[0]
    probabilities = model.predict_proba([cleaned])[0]
    confidence = round(float(max(probabilities)) * 100, 1)
    return jsonify({
        'sentiment': prediction,
        'confidence': confidence
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
