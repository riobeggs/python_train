import operator
import sys


# constants
OPERATIONS = {
    "+": operator.add,
    "-": operator.sub,
    "x": operator.mul,
    "*": operator.mul,
    "/": operator.truediv,
}


class Calculator:
    def __init__(self, num1, operator, num2):
        self.num1 = num1
        self.operator = operator
        self.num2 = num2

    def instructions():
        print("\n\nYou may use this calculator as many times as you like.")
        print("To exit the calculator, type 'quit', then press enter.")
        print()
        print("Add using the '+' key.")
        print("Subtract using the '-' key.")
        print("Multiply using the 'x' or '*' key.")
        print("Divide using the '/' key.")
        print()

    def calculate_answer(self):
        print()
        print(
            self.num1,
            self.operator,
            self.num2,
            "=",
            OPERATIONS[self.operator](self.num1, self.num2),
        )
        print()


class Get_equation:
    def __init__(
        self,
        question_prefix=None,
        number=None,
        converted_number=None,
        operator=None,
    ):
        self.question_prefix = question_prefix
        self.number = number
        self.converted_number = converted_number
        self.operator = operator

    def get_number(self):
        while True:
            self.number = input(f"{self.question_prefix} number: ")

            if Get_equation(number=self.number).quit() == True:
                print("\nQuitting...\n\n")
                sys.exit()
            # if self.number.lower().strip() == "quit":
            #     print("Quitting...")
            #     sys.exit(0)

            self.converted_number = Get_equation(number=self.number).convert_to_float()

            if self.converted_number == None:
                continue

            return self.converted_number

    def convert_to_float(self):
        converted = None
        try:
            converted = float(self.number)
        except:
            print(self.number, "is not a number")

        return converted

    def get_operator(self):
        while True:
            self.operator = input("Operator: ")

            if Get_equation(operator=self.operator).quit() == True:
                print("\nQuitting...\n\n")
                sys.exit()

            if self.operator not in OPERATIONS:
                print(self.operator, "is not an operator")
                continue

            return self.operator

    def quit(self):
        try:
            if self.number.lower().strip() == "quit":
                return True
        except:
            pass

        try:
            if self.operator.lower().strip() == "quit":
                return True
        except:
            pass


Calculator.instructions()
while True:
    num1 = Get_equation(question_prefix="First").get_number()
    operator = Get_equation().get_operator()
    num2 = Get_equation(question_prefix="Second").get_number()
    Calculator(num1=num1, operator=operator, num2=num2).calculate_answer()

    # Define a function which gives instruction how to use the calculator

    # Create multiply func
    # Create devide func
    # Create add func
    # Create subtract func


# Once you have created a calculator class capable of performing calculations
# Create project 4 again, but this time use the calculator.
# You must use my_calculator.Add(5, 6) for adding for instance

# I really dont expect you to be able to do this.
# Super added you dont need me points, Construct a quizzer, which asks questions.
# It should use the Calculator.
