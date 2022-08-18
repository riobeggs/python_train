# Create some code to randomly select a number under 10
# The user must try to guess this number in 3 or less guesses
# If the users guess is too low, tell them
# If the users guess is too high, tell them
# There is a strategy to this game which will allow you to always win. Figure out that strategy


import random


# computer chooses a random number and returns it
def random_number():
    answer = random.randint(1, 9)
    return answer


# introduces the user to the objective of the game
def intro():
    print("\n\nI am thinking of a number between 1 and 9 inclusive.")
    print("You have 3 attempts to guess my number.")


# converts the users input to an integer and returns it
def convert_to_int(input):
    converted = None
    try:
        converted = int(input)
    except:
        pass
    # if the input can not be converted to an integer then it converts it to a None and returns it
    return converted


# lets the user know how many guesses they have left
def guesses_left(i):
    if 3 - i != 1:
        print("\n")
        print(3 - i, "guesses remaining")

    if 3 - i == 1:
        print("\n")
        print("1 guess remaining")


# gets the input for the users guess at the computers chosen number and returns it
def get_users_guess():
    guess = input("guess: ")
    return convert_to_int(guess)


# checks if the users guess is valid/ is an integer and returns it
def valid_guess(i):
    # if the users guess is not valid/ is a None, then:
    is_valid = False
    while is_valid == False:
        # it does not take away from the amount of guesses they have
        guesses_left(i)
        # it asks the user for their input/ guess again
        guess = get_users_guess()
        if guess != None:
            is_valid = True
    return guess


# hints the user to whether their guess was higher or lower than the computers number
def hinter(guess, answer):
    if guess < answer:
        print("Your guess is too low")

    if guess > answer:
        print("Your guess is too high")


# displays whether the user won or lost and tells them what the computers number was
def results(guess, answer):
    if guess == answer:
        print("\nYou win!")
        print("The number was:", answer, "\n\n")
    else:
        print("\nYou lose!")
        print("The number was:", answer, "\n\n")


# function for running the game
def run_game():
    answer = random_number()

    intro()

    for i in range(3):
        guess = valid_guess(i)
        hinter(guess, answer)
        if guess == answer:
            break

    results(guess, answer)


# excecutes game
run_game()
