# 4-3
numbers = list(range(1,21))

for number in numbers:
    print(number)

# 4-5
numbers = list(range(1,1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# 4-6
numbers = list(range(1,20,2))
for number in numbers:
    print(number)
    
# 4-7
numbers = list(range(3,30,3))
for number in numbers:
    print(number)    

# 4-8
cubes = []
for number in range(1, 11):
    cube = number**3
    cubes.append(cube)
for cube in cubes:
    print(cube)

# 4-9
cubes = [number**3 for number in range(1,11)]

for cube in cubes:
    print(cube)