# Teo Espero
# BS Cloud and Systems Administration
# Western Governors University

# Begin

more = True
fruit = ["banana", "apple", "pineapple", "kiwi"]
again = "Y"

# Ask for fruits
while more:
    found = False
    newFruit = input("Add a new fruit: ")

    # check if the fruit being added is already in the list
    # instead of comparing the fruit by element
    # we are using the 'in' keyword
    if newFruit.casefold() in fruit:
        # if YES say its in the list
        print("Fruit already in list!!!")
        found = True
    else:
        fruit.append(newFruit.casefold())

    # ask for more fruits
    again = input("Add another fruit (Y/N)? ")
    if again.casefold() != "y":
        more = False
print("\nFruit list")
print("----------")

count = 0
for ctr in fruit:
    print(ctr)
    count = count + 1;
print("----------")
print("Total fruits: ", count)
# End