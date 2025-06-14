import unittest
from joke_generator import get_random_joke

class TestJokeGenerator(unittest.TestCase):
  def test_get_random_joke(self):
    joke = get_random_joke()
    self.assertIsInstance(joke, str)
    self.assertGreater(len(joke), 0)

if __name__ == '__main__':
  unittest.main()
