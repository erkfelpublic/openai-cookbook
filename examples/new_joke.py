import random

jokes = [
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don't scientists trust atoms? Because they make up everything!",
    "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    "What do you call a fake noodle? An Impasta!",
]

def get_random_joke():
    return random.choice(jokes)

if __name__ == "__main__":
    print(get_random_joke())
