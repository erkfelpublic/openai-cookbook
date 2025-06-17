import random

def get_random_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't skeletons fight each other? They don't have the guts.",
        "What do you call a fake noodle? An Impasta!",
        "Why did the bicycle fall over? Because it was two tired!"
    ]
    return random.choice(jokes)

if __name__ == "__main__":
    print(get_random_joke())
