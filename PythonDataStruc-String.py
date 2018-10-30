# Teo Espero
# BS Cloud and Systems Administration
# Western Governors University

def printLetters(theFruit):
    # This function prints the letters of the fruits in our array
    fruit = theFruit
    sizeOfFruitName = len(fruit)
    for ctr in range(0, sizeOfFruitName):
        print(fruit[ctr])
    print("\n")

# Begin

more = True
fruit = ["banana", "apple", "pineapple", "kiwi"]

# Ask for fruits
while more:
    found = False
    newFruit = input("Add a new fruit: ")

    # check if the fruit being added is already in the list
    for check in range(0, len(fruit)):
        if fruit[check].casefold() == newFruit.casefold():
            print(fruit[check] + " = " + newFruit)

            # if YES say its in the list
            print("Fruit already in list!!!")
            found = True
            break

    # otherwise add it
    if found != True:
        fruit.append(newFruit.casefold())
        print(fruit)

    # ask for more fruits
    again = input("Add another fruit (Y/N)? ")
    if again.casefold() != 'Y':
        more = False


# Loop through each array element
# and print the letters
for arr in range(0,len(fruit)):
    printLetters(fruit[arr])

# End