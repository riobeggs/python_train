import operator
from typing import Any, Union


# constants
available_operators = ["+", "-", "x", "*", "/"]


def instructions():
    """Prints the instructions for usage."""
    print("\n\nYou may use this calculator as many times as you like.")
    print("To exit the calculator, type 'quit', then press enter.")
    print()
    print("Add using the '+' key.")
    print("Subtract using the '-' key.")
    print("Multiply using the 'x' key.")
    print("Divide using the '/' key.")
    print()


class Calculator:
    """A calculator capable of :gasp: calculating."""

    def _add(self, equation: "Equation") -> float:
        if equation.can_calculate() and equation.get_operator() is operator.add:
            result = equation.number_one + equation.number_two
            equation.result = result
            return result

    def _subtract(self, equation: "Equation") -> float:
        if equation.can_calculate() and equation.get_operator() is operator.sub:
            result = equation.number_one - equation.number_two
            equation.result = result
            return result

    def _divide(self, equation: "Equation") -> float:
        if equation.can_calculate() and equation.get_operator() is operator.truediv:
            result = equation.number_one / equation.number_two
            equation.result = result
            return result

    def _multiply(self, equation: "Equation") -> float:
        if equation.can_calculate() and equation.get_operator() is operator.mul:
            result = equation.number_one * equation.number_two
            equation.result = result
            return result

    def calculate(self, equation: "Equation") -> Union[float, None]:
        """Calculate a result from an equation."""
        if equation.can_calculate():
            if equation.get_operator() is operator.add:
                return self._add(equation)
            elif equation.get_operator() is operator.sub:
                return self._subtract(equation)
            elif equation.get_operator() is operator.mul:
                return self._multiply(equation)
            elif equation.get_operator() is operator.truediv:
                return self._divide(equation)


class Equation:
    """An equation object holding details for and calculating."""

    OPERATIONS = {
        "+": operator.add,
        "-": operator.sub,
        "x": operator.mul,
        "*": operator.mul,
        "/": operator.truediv,
    }

    def __init__(self):
        self.number_one: float = None
        self.number_two: float = None
        self.operator: operator = None
        self.result: float = None
        self.calculator: Calculator = Calculator()

    def __str__(self):
        if self.result:
            return (
                f"{self.number_one} {self.operator} {self.number_two} = {self.result}"
            )

        return f"Equation({self.number_one}, {self.number_two}, {self.operator})"

    def get_operator(self) -> operator:
        """Convert the value in self.operator to an 'cls:operator'."""
        return self.OPERATIONS[self.operator]

    def set_number_one(self) -> "Equation":
        """Sets number one of our equation.
        
        Self is a fun thing to return."""
        while True:
            number_one = input("First number: ")
            self.number_one = self._convert_to_float(number_one)

            if not self.number_one:
                continue

            return self

    def set_number_two(self) -> "Equation":
        """Sets number two of our equation.
        
        Self is a fun thing to return."""
        while True:
            number_two = input("Second number: ")
            self.number_two = self._convert_to_float(number_two)

            if not self.number_two:
                continue

            return self

    def _convert_to_float(self, number: Any) -> Union[float, None]:
        """As this class is never called externally, we prefix it with an "_". 
        
        Attempts to convert a number to a float.

        Returns None if no conversion. 
        Returns float if conversion is successful.
        """
        converted = None
        try:
            converted = float(number)
        except:
            print("Could not convert", number, "to a float")

        return converted

    def set_operator(self) -> "Equation":
        """Sets the operator of our equation."""
        while True:
            self.operator = input("Operator: ")
            if self.operator not in self.OPERATIONS:
                continue

            return self

    def _is_valid(self) -> bool:
        """
        We underscore the start when we only intend a function to be used internally.

        Reports if the equation is valid and calculate can be used.
        """
        return self.number_one and self.number_two and self.operator

    def can_calculate(self) -> bool:
        """Determines if a calculation can be made."""
        if not self._is_valid():
            missing_attriute = []
            attributes = [self.number_one, self.number_two, self.operator, self.result]
            for attribute in attributes:
                if not attribute:
                    missing_attriute.append(attribute)

            print(f"ERROR: The following attributes were missing: {missing_attriute}")
            return False

        return True

    def calculate(self):
        """Calculates the sum of an equation."""
        if self.can_calculate():
            self.calculator.calculate(self)
        return self

    def reset(self) -> None:
        """Reset the equation."""
        self.__init__()

    def print_result(self) -> None:
        """Prints the result if one exists."""
        if self.result:
            print()
            print(self)
            print()

            return

        print("Error: Equation has no result.")


def main():
    """Some dumb comment."""
    instructions()
    equation = Equation()

    while True:
        equation.set_number_one().set_number_two().set_operator().calculate().print_result()
        equation.reset()


if __name__ == "__main__":
    main()

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
