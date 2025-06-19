# for Loops

fruits = ["Apple", "Banana", "Cherry"]

for fruit in fruits:
    print(fruit)
    
    
    
numbers = [1, 2, 4, 5]

for number in numbers:
    print(number)
    
    
    
# While loop

#using while loop to count from 0 to 5
count = 0 

while count <= 5:
     print(count)
     count += 1 # increment by 1
     
     
     
# loop control statement

fruit = ["Apple", "banana", "cherry", "date"]

for fruits in fruit:
    if fruits == "cherry":
        break # Exit the loop if cherry is found
    print(fruits)
    
print()# print blank space

for fruits  in fruit:
    if fruits == "cherry":
        continue # skip cherry and move to date
    print(fruits) 
    
print()

for fruits in fruit:
    if fruits == "cherry":
        pass # placeholder no action is needed for cherry
    print(fruits)

print()
    
counter = 0 

while counter <= 5:
     print(counter)
     counter += 1 # increment by 1
     if counter == 3:
         break # exits loop when 3 is reached