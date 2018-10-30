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
    newFruit = input("Add a new fruit: ")
    fruit.append(newFruit)
    print(fruit)

    again = input("Add another fruit (Y/N)? ")
    if again.capitalize() != 'Y':
        more = False


# Loop through each array element
# and print the letters
for arr in range(0,len(fruit)):
    printLetters(fruit[arr])

# End







