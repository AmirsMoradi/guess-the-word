import random

word_list = ["computer", "program", "development", "engineer", "technology"]


def get_valid_letter():
    while True:
        letter = input("Enter a letter: ").lower()
        if len(letter) == 1 and letter.isalpha():
            return letter
        else:
            print("Please enter a valid letter.")


def display_word(word, guessed_letters):
    displayed = "".join([letter if letter in guessed_letters else "_" for letter in word])
    print("Word: ", displayed)
    return displayed


def play_game():
    word = random.choice(word_list)
    guessed_letters = set()
    attempts = 5

    print("Let's start the word guessing game!")
    display_word(word, guessed_letters)

    while attempts > 0:
        letter = get_valid_letter()

        if letter in word:
            guessed_letters.add(letter)
            print("Correct letter!")
        else:
            attempts -= 1
            print("Incorrect letter!")

        displayed_word = display_word(word, guessed_letters)

        if "_" not in displayed_word:
            print("Congratulations! You've guessed the word.")
            break

        print(f"Remaining attempts: {attempts}")

    if attempts == 0:
        print(f"Game over! The word was '{word}'.")


play_game()