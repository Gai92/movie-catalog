import unittest
from movie_catalog import MovieCatalog

class TestMovieCatalog(unittest.TestCase):
    #setUp
    def setUp(self):
        self.catalog = MovieCatalog()
        self.catalog.add_movie("Matrix", "sci-fi")
        self.catalog.add_movie("Titanic", "drama")

    #add movie testing
    def test_add_valid_movie(self):
        movie = self.catalog.add_movie("She", "drama")
        self.assertEqual(movie["title"], "She")
        self.assertEqual(movie["genre"], "drama")

    #get all movies
    def test_get_all_movies(self):
        movies = self.catalog.get_all_movies()
        self.assertEqual(len(movies), 2)

if __name__ == "__main__":
    unittest.main()