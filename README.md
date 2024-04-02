# Book Recommendation System

This project implements a Book Recommendation System using Flask, scikit-learn, and MLflow. The system allows users to input a genre and receive recommendations for books in that genre based on clustering of book genres.

## Introduction

The Book Recommendation System uses a KMeans clustering algorithm to group books based on their genres. After training the model and clustering the books, users can input a genre through a web interface and receive recommendations for books in that genre.

## Features

- User-friendly web interface for inputting genre preferences and receiving book recommendations.
- Recommendation based on clustering of book genres using KMeans algorithm.
- Error handling for better user experience.
- Logging of errors and information for debugging purposes.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/book-recommendation-system.git

Install dependencies:
pip install -r requirements.txt

Ensure you have Flask installed. If not, install it using:
pip install Flask

Usage
Navigate to the project directory:
cd book-recommendation-system

Run the Flask application:
python app.py

Open your web browser and go to http://localhost:5000 to access the Book Recommendation System interface.

Select a genre from the dropdown menu and click "Get Recommendations" to see book recommendations for that genre.

Project Structure
app.py: Flask application file containing routes and logic for the web interface.
book_recommendation_model.pkl: Serialized model file containing the trained KMeans model and clustered books data.
filtered_books.csv: CSV file containing filtered book data used for training the model.
static/: Directory containing static files (CSS, JavaScript).
templates/: Directory containing HTML templates for the Flask application.
Contributing
Contributions are welcome! If you'd like to contribute to this project, feel free to open a pull request
