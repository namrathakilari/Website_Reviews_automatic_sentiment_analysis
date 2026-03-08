#  Aurène — Jewelry Reviews Sentiment Analysis

A full-stack web application that automatically classifies customer reviews as **Positive**, **Negative**, or **Neutral** in real time using a machine learning model trained from scratch.

##  Live Demo
- **Website:** https://heroic-granita-2101bb.netlify.app
- **API:** https://jewelry-reviews-sentiment-analysis.onrender.com

##  Tech Stack
- **ML Model:** Logistic Regression + TF-IDF Vectorizer (scikit-learn)
- **Training:** Google Colab — 50,000 IMDB reviews dataset
- **Backend:** Python Flask REST API
- **Frontend:** HTML, CSS, JavaScript
- **Deployment:** Render (API) + Netlify (Frontend)

##  How It Works
1. User clicks a product on the homepage and navigates to the product page
2. User writes and submits a review
3. The review is sent to the Flask API
4. The ML model classifies it as Positive, Negative, or Neutral with a confidence score
5. The result is instantly displayed and the sentiment counter updates live

##  Model Details
- Trained on 50,000 real IMDB reviews using the Hugging Face datasets library
- Neutral class identified using hedging language detection
- Dataset balanced across all three classes before training
- Achieves 85%+ accuracy on the test set
- Exported as a `.pkl` file and served via Flask

## Project Structure
```
jewelry-app/
├── app.py                 # Flask API
├── sentiment_model.pkl    # Trained ML model
├── requirements.txt       # Python dependencies
├── Procfile               # Render deployment config
└── index.html             # Frontend website
```

##  Run Locally
1. Clone the repository
```bash
git clone https://github.com/namrathakilari/Website_Reviews_automatic_sentiment_analysis.git
cd Website_Reviews_automatic_sentiment_analysis
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Start the Flask server
```bash
python app.py
```
4. Open `index.html` in your browser

##  Future Improvements
- Add a database (Firebase) to persist reviews across sessions
- Retrain model on jewelry-specific reviews for higher accuracy
- Add star ratings alongside sentiment
- Deploy as a full React application
