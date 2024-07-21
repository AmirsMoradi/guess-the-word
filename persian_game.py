import random

word_list = ["کامپیوتر", "برنامه", "توسعه", "مهندس", "فناوری"]


def get_valid_letter():
    while True:
        letter = input("یک حرف وارد کنید: ")
        if len(letter) == 1 and 'ا' <= letter <= 'ی':
            return letter
        else:
            print("لطفاً یک حرف معتبر وارد کنید.")


def display_word(word, guessed_letters):
    displayed = "".join([letter if letter in guessed_letters else "_" for letter in word])
    print("کلمه: ", displayed)
    return displayed


def play_game():
    word = random.choice(word_list)
    guessed_letters = set()
    attempts = 5

    print("بازی حدس کلمه را شروع کنید!")
    display_word(word, guessed_letters)

    while attempts > 0:
        letter = get_valid_letter()

        if letter in word:
            guessed_letters.add(letter)
            print("حرف درست بود!")
        else:
            attempts -= 1
            print("حرف اشتباه بود!")

        displayed_word = display_word(word, guessed_letters)

        if "_" not in displayed_word:
            print("تبریک! شما کلمه را حدس زدید.")
            break

        print(f"تعداد حدس‌های باقی‌مانده: {attempts}")

    if attempts == 0:
        print(f"بازی تمام شد! کلمه مورد نظر '{word}' بود.")


play_game()