class MovieCatalog:
    VALID_GENRES = ["drama", "comedy", "sci-fi", "action", "horror"]
    def __init__(self):
        self.movies = []

    def get_movies_by_genre(self, genre):
        genre = genre.strip().lower()
        return [movie for movie in self.movies if movie["genre"] == genre]

def main():
    catalog = MovieCatalog()

    # Temporary demo data
    catalog.movies = [
        {"title": "Inception", "genre": "sci-fi"},
        {"title": "The Notebook", "genre": "drama"},
        {"title": "Interstellar", "genre": "sci-fi"}
    ]

    # Show available genres before asking
    print("Available genres:", ", ".join(MovieCatalog.VALID_GENRES))

    genre = input("Enter a genre to filter by: ").strip()
    filtered = catalog.get_movies_by_genre(genre)

    if not filtered:
        print(f"No movies found for genre '{genre}'.")
    else:
        print(f"\n Movies in genre '{genre}':")
        for movie in filtered:
            print(f"{movie['title']} ({movie['genre']})")


if __name__ == "__main__":
    main()