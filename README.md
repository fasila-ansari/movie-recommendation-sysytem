# movie-recommendation-sysytem
A simple movie recommendation system built with Python that suggests similar movies using cosine similarity based on genre features.
## Overview
The recommendation model uses cosine similarity to measure the similarity between movies. 
Each movie is represented by genre features such as romance, action, sci-fi, and drama. 
Based on these features, the system calculates similarity scores and recommends the most similar movies.
## Technologies Used
- Python
- Pandas
- Scikit-learn
## How It Works
1. A dataset of movies and their genre features is created.
2. The system calculates similarity between movies using cosine similarity.
3. The user enters a movie name.
4. The program recommends the most similar movies from the dataset.
## Example
Input:
Enter a movie name: Interstellar
Output:
Top Recommended Movies:
The Dark Knight (similarity score: 0.82)
Inception (similarity score: 0.82)
Avengers (similarity score: 0.58)
## Purpose
This project was created to practice basic machine learning and recommendation system concepts using Python. 
It demonstrates how similarity algorithms can be used to suggest items based on shared features.

