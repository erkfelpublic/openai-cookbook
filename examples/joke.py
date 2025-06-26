import random

def tell_joke():
  """Tells a random joke."""
  jokes = [
      "Why did the scarecrow win an award? Because he was outstanding in his field!",
      "Why don't scientists trust atoms? Because they make up everything!",
      "I told my wife she was drawing her eyebrows too high. She looked surprised.",
      "What do you call a fake noodle? An impasta!",
      "Why did the bicycle fall over? Because it was two tired!",
  ]
  print(random.choice(jokes))

if __name__ == "__main__":
  tell_joke()
