

from typing import List


class PouchableObject:
    def __init__(self, is_sharp=False) -> None:
        self.is_sharp = False


class Branch(PouchableObject):
    def __init__(self, is_sharp=False) -> None:
        print("A branch special function")
        super().__init__(is_sharp)


class Stone(PouchableObject):
    pass


class Diamond(PouchableObject):
    def __init__(self) -> None:
        self.is_sharp = True


class Animal:
    def __init__(self, name=None, age=None):
        self.has_tail = False
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def set_name(self, name: str):
        if isinstance(name, str) and len(name) > 0:
            self.name = name

        return self.name

    def talk(self):
        print(f"Hi I'm a {self.__class__.__name__}")

    def can_wag_tail(self) -> bool:
        return self.has_tail

    def wag_tail(self):
        print(f"{self.__class__.__name__} wags tail.")


class Hedgehog(Animal):
    def __init__(self):
        self.has_tail = False

    def talk(self):
        print("Hi I'm a Hedgehog")


class Dog(Animal):
    def __init__(self):
        self.has_tail = True

    def talk(self):
        print("Hi I'm a Dog")


class Kangaroo(Animal):
    def __init__(self):
        self.has_tail = True
        self.has_pouch = True
        self.pouch = []

    def talk(self):
        print("Hi I'm a Kangaroo")

    def put_something_in_pouch(self, item: "PouchableObject") -> None:
        # if there are less than 3 objects put item in the pouch
        if not isinstance(item, PouchableObject):
            print("Something went wrong.") # Worst
            print("Your item is not a PouchableObject.") # Medium
            print(f"{type(item).__name__} is not a {PouchableObject.__name__}") # True
            return

        if item.is_sharp:
            print("Ouch!")
            return
            
        if len(self.pouch) < 3:
            self.pouch.append(item)
            return
        
        print("Too many items?")
        # [stretch] if the item is sharp, we cannot put it in and exclaim ouch

    def get_pouch_contents(self) -> None:
        # list the items in the pouch
        return self.pouch


roo = Kangaroo()
pipi = Dog()
andy = Hedgehog()
nadal = Animal()


item = Diamond()

stone = Stone()
branch = Branch()
diamond = Diamond()


# print(f"Kangaroo is test: {isinstance(roo, Kangaroo)}")
# print(f"Animal is test: {isinstance(roo, Animal)}")
# print(f"str is test: {isinstance(roo, str)}")

animal_list: List[Animal] = [roo, pipi, andy, nadal]

# stone = "stone"
# branch = "branch"
# diamond = "diamond"

items = ["a bad item", stone, stone, branch, diamond, branch]

for rubbish in items:  
    roo.put_something_in_pouch(rubbish)


print(roo.get_pouch_contents())
# for animal in animal_list:
#     animal.talk()

#     if animal.can_wag_tail():
#         animal.wag_tail()

# # my_str = "hi there"
# # my_str_2 = "hi there"
# # print(f"is test: {my_str is my_str_2}")

# # my_list = [1]
# # my_second_list = [1]
# # print(f"is test: {my_list is my_second_list}")

# # my_list.append(2)
# # print(f"my_list: {my_list}")
# # print(f"my_second_list: {my_second_list}")




# nadal = Animal(name="Nadal", age=18)
# print(nadal.name) # Nadal


# nadal = Animal()
# nadal.name = "Nadal"
# print(nadal.name) # Nadal


# nadal = Animal()
# nadal.set_name(name="Nadal")
# print(nadal.name) # Nadal
