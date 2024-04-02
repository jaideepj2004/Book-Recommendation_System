import logging
from flask import Flask, render_template, request
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle as pkl 

# Initialize Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load the model data
model_path = "book_recommendation_model.pkl"
try:
    # file_path = 'book_recommendation_model.pkl'

    # with open(file_path , 'rb') as f:
    #      model_data = pkl.load(f)
    model_data = joblib.load(model_path)
    kmeans_model = model_data['kmeans_model']
    cluster_books = model_data['cluster_books']
except Exception as e:
    logging.error(f"Error loading model data: {e}")

# Load the filtered dataset
filtered_df = pd.read_csv(r"C:\Users\jaide\OneDrive\Desktop\Data Science\Internship\pwskills book recomendation system\project1\filtered_books.csv")

# Create TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(filtered_df['genres'])

# Define function for book recommendation
def get_recommendations(genre, n_recommendations=5):
    try:
        genre_vector = tfidf_vectorizer.transform([genre])
        cluster = kmeans_model.predict(genre_vector)[0]
        cluster_books_titles = cluster_books[cluster]
        recommendations = filtered_df[filtered_df['title'].isin(cluster_books_titles)].sample(n=n_recommendations)['title'].tolist()
        return recommendations
    except Exception as e:
        logging.error(f"Error getting recommendations: {e}")
        return []

# Define routes
@app.route('/')
def home():
    genres = sorted(filtered_df['genres'].unique())
    return render_template('index.html', genres=genres)

@app.route('/recommendation', methods=['POST'])
def recommendation():
    if request.method == 'POST':
        try:
            genre = request.form['genre']
            recommendations = get_recommendations(genre)
            return render_template('recommendation.html', genre=genre, recommendations=recommendations)
        except Exception as e:
            logging.error(f"Error processing recommendation request: {e}")
            return render_template('error.html')
    else:
        return render_template('index.html', genres=genres)  

if __name__ == '__main__':
    app.run(debug=True)
