import unittest
from joke import get_random_joke, jokes

class TestJoke(unittest.TestCase):

    def test_get_random_joke(self):
        joke = get_random_joke()
        self.assertIn(joke, jokes)

if __name__ == '__main__':
    unittest.main()
