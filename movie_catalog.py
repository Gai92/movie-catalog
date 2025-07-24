class MovieCatalog:
    VALID_GENRES = ["drama", "comedy", "sci-fi", "action", "horror"]

    def __init__(self):
        self.movies = []

    # Return all movies
    def get_all_movies(self):
        if not self.movies:
            print("The catalog is currently empty.")
        return self.movies

def main():
    catalog = MovieCatalog()

    # Temporary demo: manually pre-fill movies
    catalog.movies = [
        {"title": "Inception", "genre": "sci-fi"},
        {"title": "The Notebook", "genre": "drama"},
        {"title": "Interstellar", "genre": "sci-fi"}
    ]
    #Print all movies
    print("\nAll Movies in Catalog:")
    movies = catalog.get_all_movies()
    for movie in movies:
        print(f" {movie['title']} ({movie['genre']})")


if __name__ == "__main__":
    main()