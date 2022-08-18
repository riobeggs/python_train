import random

# introduces and starts the game
def intro():
    print("\nGuess the 4 letter word in 20 attempts to win!\n")
    input("Press Enter to start")
    print("\n")


# computer chooses random word from list
def chosen_word():
    wordchoice = [
        "Bake",
        "Word",
        "List",
        "Four",
        "Five",
        "Nine",
        "Good",
        "Best",
        "Cute",
        "Zero",
        "Huge",
        "Cool",
        "Tree",
        "Race",
        "Rice",
        "Keep",
        "Lace",
        "Beam",
        "Game",
        "Mars",
        "Tide",
        "Ride",
        "Hide",
        "Exit",
        "Hope",
        "Cold",
        "From",
        "Need",
        "Stay",
        "Come",
    ]
    word = random.choice(wordchoice).lower()
    return word


# asks the user to guess the chosen word.
# if they guess correctly within 10 guesses they win.
# if they guess incorrectly or run out of guesses they lose.
def users_guess(word):
    for i in range(20):
        if 20 - i == 1:
            print("This is your last guess!")
            answer(word)
            break
        else:
            print("You have", 20 - i, "guesses left.")
        guess = input("Guess: ").lower()
        if len(guess) != 4:
            print("Incorrect\nYou must guess 4 letter words only.\n")
            continue
        if len(guess) == 4 and guess != word:
            correct_letters = []
            for letter in guess:
                if letter in word:
                    correct_letters.append(letter)
            if correct_letters:
                print(f"The following letters were correct: {correct_letters}\n")
            else:
                print("Incorrect\n")
            continue
        elif guess == word:
            print("\nYou win!\nThe word was:", word, "\n")
            break


# lets user know if they won or lost and tells them the answer
def answer(word):
    guess = input("Guess: ").lower()
    if guess == word:
        print("\nYou win!\nThe word was:", word, "\n")
    else:
        print("\nYou lose.\nThe word was:", word, "\n")


def main():
    intro()
    word = chosen_word()
    users_guess(word)


if __name__ == "__main__":
    main()
