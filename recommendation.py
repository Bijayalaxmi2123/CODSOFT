movies = {
    "action": ["Avengers", "Batman", "John Wick"],
    "comedy": ["3 Idiots", "Golmaal", "Dhamaal"],
    "romance": ["Titanic", "The Notebook", "A Walk to Remember"],
    "sci-fi": ["Interstellar", "Inception", "The Matrix"]
}

print("Movie Recommendation System")
print("Genres: action, comedy, romance, sci-fi")

genre = input("Enter your favorite genre: ").lower()

if genre in movies:
    print("\nRecommended Movies:")
    for movie in movies[genre]:
        print("-", movie)
else:
    print("Genre not available.")