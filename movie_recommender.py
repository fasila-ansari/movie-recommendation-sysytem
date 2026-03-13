import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

print("\nMovie Recommendation System")
print("--------------------------------")

data = {
    "movie": [
        "Titanic",
        "The Notebook",
        "Romeo + Juliet",
        "La La Land",
        "Avengers",
        "Iron Man",
        "Spider-Man",
        "Interstellar",
        "The Dark Knight",
        "Inception"
    ],

    "romance":[1,1,1,1,0,0,0,0,0,0],
    "action":[0,0,0,0,1,1,1,1,1,1],
    "sci_fi":[0,0,0,0,0,0,0,1,0,1],
    "drama":[1,1,1,1,0,0,0,1,1,0]
}

df = pd.DataFrame(data)

features = df[["romance","action","sci_fi","drama"]]

similarity = cosine_similarity(features)

def recommend_movies(movie_name):

    movie_name = movie_name.lower()

    df["movie_lower"] = df["movie"].str.lower()

    if movie_name not in df["movie_lower"].values:
        print("\nMovie not found in dataset.")
        return

    index = df[df["movie_lower"] == movie_name].index[0]

    scores = list(enumerate(similarity[index]))

    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print("\nTop Recommended Movies:\n")

    for i, score in scores[1:4]:
        movie_title = df.iloc[i]["movie"]
        print(f"{movie_title} (similarity score: {round(score,2)})")

movie = input("\nEnter a movie name: ")

recommend_movies(movie)