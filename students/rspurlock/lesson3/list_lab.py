#!/usr/bin/env python3

# Series 1
print('Series 1')

# Build the starting fruit list
fruit1 = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruit1)

# Request user to enter another fruit and add it to the list
anotherFruit = input("Please enter another fruit: ")
fruit1.append(anotherFruit)
print(fruit1)

# Request user to enter a fruit number and then display that fruit (1-based)
fruitIndex = input("Please enter a fruit number: ")
print('Fruit number', end=' ')
print(fruitIndex, end = ' ')
print('is', end = ' ')
print(fruit1[int(fruitIndex) - 1])

# Add grapes to the list of fruits (At the front of the list)
fruit1 = ['Grapes'] + fruit1
print(fruit1)

# Insert pineapples into the list of fruits at index 2
fruit1.insert(2, 'Pineapples')
print(fruit1)

# Loop and display all the fruits that begin with 'P'
print('Fruits that begin with the letter "P"')
for fruit in fruit1:
    if fruit[0] == 'P':
        print(fruit)

print()

# Series 2
print('Series 2')

# Create the initial list from the series 1 list
fruit2 = list(fruit1)
print(fruit2)

# Remove the last fruit from the list
fruit2 = fruit2[:-1]
print(fruit2)

# Ask the user to enter a fruit to delete
fruit = input("Please enter a fruit to delete: ")
fruit2.remove(fruit)
print(fruit2)

# Double the fruit list and ask until matching fruit found, then delete all occurrences
fruit = ''
fruit2 *= 2
print(fruit2)
while fruit not in fruit2:
    fruit = input("Please enter another fruit to delete: ")
while fruit in fruit2:
    fruit2.remove(fruit)
print(fruit2)

print()

# Series 3
print('Series 3')

# Create the initial list from the series 1 list
fruit3 = list(fruit1)
print(fruit3)

# Ask user if they like each fruit in the list, remove those they don't
valid = ['yes', 'no']
fruits = list(fruit3)
for fruit in fruits:
    answer = input("Do you like " + fruit + "? ")
    while answer not in valid:
        answer = input("Please answer yes or no!: ")
    if (answer == 'no'):
        fruit3.remove(fruit)
print(fruit3)

print()

# Series 4
print('Series 4')

# Create the initial list from the series 1 list
fruit4 = list(fruit1)
print(fruit4)

# Reverse the letters of each fruit in the list
newFruits = []
for fruit in fruit4:
    newFruits.append(fruit[::-1])

# Delete the last item of the original list
fruit4 = fruit4[:-1]

# Print the updated lists
print(fruit4)
print(newFruits)
