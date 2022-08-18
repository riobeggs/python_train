def example1():
    class Person:
        def __init__(self):
            print("person.init")
            self.name = "rio"
            self.age = 18

    bob = Person()
    print(bob.name)
    bob.name = "name"
    alice = Person()
    print(bob.name)
    print(alice.name)


def example2():
    class Person:
        def __init__(self, age=None, name=None):
            print("person.init")
            if name == None:
                name = "default"
            self.name = name
            self.age = age

    rio = Person(name="rio", age=18)
    print(rio.name)
    print(rio.age)

    bob = Person(20)
    print(bob.name)
    print(bob.age)

    carl = Person()
    print(carl.name)
    print(carl.age)


def example3():
    class Person:
        def __init__(self, age=None, name=None):
            print("person.init")
            if name == None:
                name = "default"
            self.name = name
            self.age = age
            # init is called when Person is instantiated
            # defaults creation (constructs) arguments
            # creates and assigns attributes

        def __str__(self):
            print("person.str")

            return f"Person({self.name}, {self.age})"
            # str is called when string representation of a person object is requested
            # offers up string representation of a Person object

        def greet(self):
            return "Person.greet"
            #

    alice = Person(name="alice", age=30)

    print(str(alice))
    print(alice)
    print(alice.__str__())

    print(alice.greet())

    carl = Person()
    print(carl)


example3()
