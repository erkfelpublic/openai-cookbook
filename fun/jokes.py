"""This file contains a collection of jokes."""
import random

def get_random_joke():
  """Returns a random joke from a predefined list."""
  jokes = [
      "Why don't scientists trust atoms? Because they make up everything!",
      "What do you call a fake noodle? An Impasta!",
      "Why did the scarecrow win an award? Because he was outstanding in his field!",
      "I'm reading a book on anti-gravity. It's impossible to put down!",
      "What do you call a lazy kangaroo? Pouch potato!",
  ]
  return random.choice(jokes)
