import random
import time

# Capture the users name
def users_name():
    print("\n")
    name = str(input("Name: "))
    return name


# greets user and asks for the amount of equations they wish to answer
def greet_user(name):
    print("\n")
    print("Hello, " + (name.capitalize()) + "! \n\nThis is a multiplication test.")
    print("How many equations would you like to answer?\n")


# captures the amount of equations the user wishes to answer
def user_equations():
    while True:
        user_input = input("Equations: ")
        equations = convert_to_int(user_input)
        if equations == None or equations <= 0:
            continue
        elif equations == int(equations):
            return equations


# lets the user know how many questions they will be answering and how the score is recorded
def amount_of_equations(equations):
    print("\nComplete the", equations, "equations as fast as you can.")
    print("Your time will be displayed at the completion of this test.\n")


# starts the timer
def timer_start():
    input("Press Enter to start")
    print("\n")
    start_time = int(time.time())
    return start_time


# converts the users input to an integer
def convert_to_int(input):
    converted = None
    try:
        converted = int(input)
        return converted
    except:
        pass


# (havent used this function yet)
def printer(x: str) -> None:
    x = x.upper()
    print(x)
    return x


# Quizzing loop
def quiz(equations):
    for i in range(equations):
        if i % 1 == 0:
            num1 = random.randint(0, 9)
            num2 = random.randint(0, 9)
        while True:
            print(num1, "x", num2, "=")
            user_answer = input("")
            answer = convert_to_int(user_answer)
            if type(answer) == None:
                print("Incorrect\n")
            elif answer != num1 * num2:
                print("Incorrect\n")
            else:
                print("Correct\n")
                break


# stops the timer
def timer_end():
    input("Press Enter to stop\n")
    end_time = int(time.time())
    return end_time


# displays and calculates the time taken to finish the quiz
def result_display(name, end_time, start_time):
    timer = end_time - start_time
    print("Well done " + (name.capitalize()) + "!")
    print("Your time was:\n")
    print(timer, "seconds\n")


def main():
    name = users_name()
    greet_user(name)
    equations = user_equations()
    amount_of_equations(equations)
    start_time = timer_start()
    quiz(equations)
    end_time = timer_end()
    result_display(
        name, end_time, start_time,
    )


if __name__ == "__main__":
    main()
