import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.model_selection import GridSearchCV
import joblib
import mlflow
from mlflow.tracking import MlflowClient

# Load the dataset
df = pd.read_csv(r"C:\Users\jaide\OneDrive\Desktop\Data Science\Internship\pwskills book recomendation system\project1\books_cleaned.csv")

# Filter the dataset based on your criteria
filtered_df = df[(df['average_rating'] > 4) & (df['ratings_count'] > 200) & (df['books_count'] > 200)]

# Select relevant columns
filtered_df = filtered_df[['title', 'genres']]

# Create TF-IDF matrix
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(filtered_df['genres'])

# Define parameters for grid search
params = {
    'n_clusters': [5, 10, 15],
    'init': ['k-means++', 'random'],
    'n_init': [10, 15, 20],
    'max_iter': [300, 400, 500],
    'random_state': [42]
}

# Train the KMeans model using GridSearchCV
with mlflow.start_run():
    kmeans = KMeans()
    grid_search = GridSearchCV(kmeans, params, cv=5)
    grid_search.fit(tfidf_matrix)

    # Log parameters and best score
    for key, value in grid_search.best_params_.items():
        mlflow.log_param(key, value)
    mlflow.log_metric("best_score", grid_search.best_score_)

    # Get the best model
    best_kmeans_model = grid_search.best_estimator_

    # Assign cluster labels to the data
    filtered_df['cluster'] = best_kmeans_model.fit_predict(tfidf_matrix)

    # Group titles by cluster
    cluster_books = filtered_df.groupby('cluster')['title'].apply(list)

    # Save the trained model along with the clustered books
    model_data = {'kmeans_model': best_kmeans_model, 'cluster_books': cluster_books}
    joblib.dump(model_data, 'book_recommendation_model.pkl')

    # Log model as MLflow artifact
    mlflow.sklearn.log_model(best_kmeans_model, "model")
