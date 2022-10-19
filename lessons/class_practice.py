# print(__file__)
import os

x = os.path.dirname(__file__)
# print(x)
# print(os.path.join(x, "assets.txt"))

# Python 3 code to demonstrate the
# working of MD5 (byte - byte)


def print_human(name, age, height):
    print(name, age, height)

print_human("rioo", 18, 164)
print_human("sam", 34, 164)
print_human(15, "hello", "world")


def print_human4(human: dict):
    print(human["name"], human["age"], human["height"])

rio = {"name": "rio", "age": 18, "height": 164}
rio2 = {"name": "rio", "age": 18}
print_human4(rio)
# print_human4(rio2)



def print_human5(**kwargs):
    print(kwargs["name"], kwargs["age"], kwargs["height"])

print_human5(name = "rio", age = 18, height = 164)



def print_human2(name, age, height):
    assert isinstance(name, str)
    assert isinstance(age, int)
    assert isinstance(height, int)
    print(name, age, height)

# print_human2(15, "hello", "world")



from dataclasses import dataclass
@dataclass
class HumanClass:
    # def __init__(self, name, age, height):
    #     self.name = name
    #     self.age = age
    #     self.height = height
    name:str
    age:int
    height:int

    def __post_init__(self):
        assert isinstance(self.name, str)
        assert isinstance(self.age, int)
        assert isinstance(self.height, int)

    # def __str__(self) -> str:
    #     return f"{self.__class__.__name__}({self.name}, {self.age}, {self.height})"

    # def __repr__(self) -> str:
    #     return f"{self.__class__.__name__}({self.name}, {self.age}, {self.height})"


# rio = HumanClass()
# rio = HumanClass(15, "hello", "world")
rio = HumanClass("rio", 18, 164)
print(rio)
print([rio])
sam = HumanClass("sam", 34, 164)
# test = HumanClass()

def print_human3(human: HumanClass):
    assert isinstance(human, HumanClass)
    print(human.name, human.age, human.height)

print_human3(rio)
print_human3(sam)

