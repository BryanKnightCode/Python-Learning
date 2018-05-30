# Although this code looks like it should print the numbers from 1 to 5, it
# doesn’t print the number 5:
for value in range(1,5):
    print(value)

print("\n")

# To print the numbers from 1 to 5, you would use range(1,6):
for value in range(1,6):
    print(value)

numbers = list(range(1,6))
print(numbers)

# list the even numbers between 1 and 10:
even_numbers = list(range(2,11,2))
print(even_numbers)

squares = [] # 1. We start with an empty list called squares at line 19

# 2. we tell Python to loop through each value from 1 to 10 using the range() function. Inside
# the loop, the current value is raised to the second power and stored in the variable space in 3.
for value in range(1,11): 
    squares.append(value**2) # each new value of square is appended to the list squares.
    
print(squares)

