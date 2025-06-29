
fruits = ["apple", "banana", "cherry",]

# Print apple
print(fruits[0])

# Replace banana with blueberry
fruits[1] = "blueberry"
print(fruits)

# Add to list
fruits.append("kiwi")
print(fruits)

# add to list at a postion 1
fruits.insert(1, "orange")
print(fruits)

# Remove item from list
fruits.remove("kiwi")
print(fruits)

# sorting list in alphabetical order
fruits.sort()
print(fruits)

# sorting list in reverse order
fruits.sort(reverse=True)
print(fruits)