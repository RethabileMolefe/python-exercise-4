# Question 1
# Creating a list of fruits
fruits = ["Apples","pears", "bananas", "oranges"]

# Creating a for loop
for fruit in fruits:
  print(fruit)

# Question 2
# Creating a while loop
count = 5

while count > 0:
  print(count)
  count += -1

# Question 3
# Creating a for loop with range
for i in range(1,11):
  print(i**2)

# Question 4
# Importing random module
import random

# Creating lists
colours = ["Red","black","pink","blue","yellow","brown"]

# Creating a for loop
for i in range(3):
  print(random.choice(colours))

# Question 5
#Importing the module
import math_operations

#Creating a simple calculator
while True:
  print("Select operation:")
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")
  print("5. Exit")
  
  choice = input("Enter choice (1/2/3/4/5): ")
  if choice == '5':
    print("Exiting calculator. Bye!")
    break
  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))
  
  if choice == "1":
    print(f"{num1} + {num2} = {math_operations.add(num1, num2)}")
  elif choice == "2":
    print(f"{num1} - {num2} = {math_operations.subtract(num1, num2)}")
  elif choice == "3":
    print(f"{num1} *{num2} = {math_operations.multiply(num1, num2)}")
  elif choice == "4":
    result = math_operations.divide(num1, num2)
    print(f"{num1} / {num2} = {result}")
  else:
    print("Invalid input")


 



 
