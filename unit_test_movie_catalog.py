import unittest
from movie_catalog import MovieCatalog

class TestMovieCatalog(unittest.TestCase):

    def setUp(self):
        self.catalog = MovieCatalog()
        self.catalog.add_movie("Matrix", "sci-fi")
        self.catalog.add_movie("Titanic", "drama")

if __name__ == "__main__":
    unittest.main()