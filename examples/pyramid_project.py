# converts an input to an integer and returns it
def convert_to_int(input):
    converted = None
    try:
        converted = int(input)
    except:
        pass

    return converted


# gets the users input for the height of the pyramid and returns it
# loops until input is an integer bigger than 0
# f2 to mass rename a variable
def get_pyramid_height():
    while True:
        height = input("\nPyramid height: ")
        converted_height = convert_to_int(height)
        if converted_height == None:
            print("Please enter a number")
            continue

        if converted_height <= 0:
            print("Please enter a positive number")
            continue

        return converted_height


# prints the structure of the pyramid for the given height
def pyramid_structure(chosen_height):
    print("\n")
    for i in range(1, chosen_height + 1):
        spaces = " " * (chosen_height - i)
        astericies = "*" * ((2 * i) - 1)
        print(spaces + astericies)

    print("\n")


# calls functions
def main():
    chosen_height = get_pyramid_height()
    pyramid_structure(chosen_height)


# excecutes main()
if __name__ == "__main__":
    main()
