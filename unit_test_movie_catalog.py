import unittest
from movie_catalog import MovieCatalog

class TestMovieCatalog(unittest.TestCase):

    def setUp(self):
        self.catalog = MovieCatalog()
        self.catalog.add_movie("Matrix", "sci-fi")
        self.catalog.add_movie("Titanic", "drama")

    def test_add_valid_movie(self):
        movie = self.catalog.add_movie("She", "drama")
        self.assertEqual(movie["title"], "She")
        self.assertEqual(movie["genre"], "drama")

if __name__ == "__main__":
    unittest.main()