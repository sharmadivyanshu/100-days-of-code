import requests
import random

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
WORDS = [word.decode("utf-8").lower() for word in response.content.splitlines()]


def start_game(word: str):
    print(word)
    spaces = len(word)
    guessed_letters = ["_" for _ in range(spaces)]
    guessed_letter_count = 0
    lives_left = 5
    won = False
    while lives_left > 0:
        choice = input("Please enter a letter: ").lower()
        if choice not in word or len(choice) > 1:
            lives_left -= 1
            print("Not matched")
            print(f"{lives_left} lives left")
            print(lives_left*"♥️")
            if lives_left == 0:
                break
        elif choice in guessed_letters:
            print(f"Please enter a different letter \x1b[1;31m{choice}\x1b[0m is already matched")
        else:
            for index, letter in enumerate(word):
                if choice == letter:
                    guessed_letters[index] = letter
                    guessed_letter_count += 1
        if guessed_letter_count == spaces:
            won = True
            break
        print("".join(guessed_letters))
    if won:
        print("\n\x1b[1;31mCongratulations! You are a true winner!\x1b[0m")
    else:
        print(f"\nYou lost correct word is \x1b[1;31m{word}\x1b[0m")


if __name__ == "__main__":
    start = input("Start Game? ")
    if start.lower() in ["yes", "y"]:
        play_again = True
        while play_again:
            random_word = str(random.choice(WORDS))
            start_game(random_word)
            play_again = input("\nDo you want to play again? ")
            play_again = play_again in ["yes", "y"]
