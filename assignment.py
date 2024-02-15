student = {
    "name": "Nathan Galindo",
    "age": 22,
    "major": "MIS",
    "hobbies": [
        "Playing guitar",
        "Going to the gym"
    ]
}

student["state"] = "Texas"
student["age"] = student["age"] + 1
print(student)
for key in student:
    print(f"Student's {key}: {student[key]}")

movie_ratings = {
    "Finding Nemo": 10,
    "Pulp Fiction": 10,
    "The Shining": 10,
    "Scary Movie": 5,
    "White Chicks": 3
}

movie_title = input("Enter a movie title: ")


def recommend_movie(movie_ratings, movie_title):
    for movie in movie_ratings:
        if movie_title == movie and movie_ratings[movie] >= 8:
            print(f"Recommended movie: {movie}")
        elif movie_title != movie and movie_ratings[movie] >= 8:
            print(f"Recommended movie: {movie}")

recommend_movie(movie_ratings, movie_title)