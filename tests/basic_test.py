import unittest
from os.path import dirname
import sys
sys.path.append(dirname(__file__) + '/..')
from media import movie

class TestBasicFeatures(unittest.TestCase):
    def setUp(self):
        self.sample = movie.Movie("test_title", "test_image", "test_url")

    def test_movie_has_a_title(self):
        self.assertEqual(self.sample.title, 'test_title')

    def test_movie_has_a_image_url(self):
        self.assertEqual(self.sample.poster_image_url, 'test_image')

    def test_movie_has_a_trailer_url(self):
        self.assertEqual(self.sample.trailer_youtube_url, 'test_url')

if __name__ == '__main__':
    unittest.main()
