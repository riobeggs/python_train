# Create code to print trees
def convert_to_int(input):
    converted = None
    try:
        converted = int(input)
        return converted
    except: 
        pass

def pyramid_height():
  while True:
    height = input("\nPyramid height: ") 
    chosen_height = convert_to_int(height)
    if chosen_height == None:
      print("Please enter a number")
      continue
    elif chosen_height <=0:
      print("Please enter a positive number")
      continue
    else:
      return chosen_height

def pyramid_structure(chosen_height):
  print("\n")
  for i in range(chosen_height):
    x = i+1  
    for y in range(chosen_height-x):
      print(" ", end="")
    for z in range((2*i)+1):
      print("*", end="")
    print("")
  print("\n")

def main():
  chosen_height = pyramid_height()
  pyramid_structure(chosen_height)
if __name__ == "__main__":
  main()

