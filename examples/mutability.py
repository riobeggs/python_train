def hello(y):
    print(y)
    y += "bye"


x = "hi"
hello(x)
print(x)

x = ["1", "2", "3"]
hello(x)
print(x)

# # immutability\
# x = "HI"
# print(x)
# y = x # move me
# x = "bye"
# print(x)
# print(y)
# print()
# print()

# x = "hi"
# y = x
# print(x)
# x += "hi" # x = x + "hi"
# print(x)
# print(y)
# print()
# print()

# # mutability
# x = ["1", "2", "3"]
# y = x
# print(x)
# x.append("4")
# print(y)
