"""
hi sam, ive created functions for all of the different parts of the code.
my problem is that the variables i have created arent defined within other functions for example 
in my users_name function i have defined the variable name but in the greet_user function it is not defined.
the same problem occurs in other variables i have made too. Is there a way around this?
I havent started working on the bug for the quiz loop yet and i'm not sure if ive structured or
done this correctly since i havent really worked with functions before.
"""

import random
import time

# Capture the users name
def users_name() -> str:
    print("\n")
    name = input("Name: ")
    print("\n")

    return name


# greets user and asks for the amount of equations they wish to answer
def greet_user(name: str) -> None:
    print("\n")
    print("Hello, " + str(name) + ".\n\nThis is a multiplication test.")
    print("Complete the 20 equations as fast as you can.")
    print("Your time will be displayed at the completion of this test.\n")


# starts the timer
def timer_start() -> float:
    input("Press Enter to start\n")
    start_time = time.time()
    return start_time


# Quizzing loop
def quiz() -> None:
    for i in range(20):
        if i % 1 == 0:
            num1 = random.randint(0, 9)
            num2 = random.randint(0, 9)
        while True:
            print(num1, "x", num2, "=")
            answer = input("")
            # Find a way to prevent this from crashing if I dont enter a number
            if int(answer) == num1 * num2:
                print("Correct\n")
                break
            elif int(answer) != num1 * num2:
                print("Incorrect\n")


# stops the timer
def timer_end() -> float:
    # You should consider stopping the timer before displaying this message.
    # They have completed the test, but the timer does not stop until they
    # say they done.
    input("Press Enter to stop\n")
    end_time = time.time()
    return end_time


# displays time taken to finish the quiz
def time_convert(sec: int) -> None:
    # This method has a bug. This is an odd calculation.
    # % acts like a remainder.
    # example:
    # 0 % 2 = 0 (remainder)
    # 1 % 2 = 1 (remainder)
    # 2 % 2 = 0 (remainder)
    # 3 % 2 = 1 (remainder)
    # ...
    sec = sec % 60
    print(int(sec), "seconds\n")


# calculates the time
def time_display(start_time: float, end_time: float) -> float:
    timer = end_time - start_time
    return timer


# Displays the time taken to answer the chosen amount of equations
def result_display(name: str, timer: float) -> None:
    print("Well done " + str(name) + "!")
    print("Your time was:")
    time_convert(timer)


def main():
    # You need to pass variables around to use them in other methods
    name = users_name()
    greet_user(name=name)
    start_time = timer_start()
    quiz()
    finish_time = timer_end()
    # time_display and time_convert seemed to be inverted
    timer = time_display(start_time=start_time, end_time=finish_time)
    time_convert(timer)
    result_display(name=name, timer=timer)


if __name__ == "__main__":
    main()
