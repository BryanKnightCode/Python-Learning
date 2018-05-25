# *******The remove() method deletes only the first occurrence of the value you specify. If there’s
# a possibility the value appears more than once in the list, you’ll need to use a loop to
# determine if all occurrences of the value have been removed. You’ll learn how to do
# this in Chapter 7.*********

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("The last motorcycle I woned was a " + last_owned.title() + ".")

first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

# If you’re unsure whether to use the del statement or the pop() method,
# here’s a simple way to decide: when you want to delete an item from a list
# and not use that item in any way, use the del statement; if you want to use an
# item as you remove it, use the pop() method

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

# You can also use the remove() method to work with a value that’s being
# removed from a list. Let’s remove the value 'ducati' and print a reason for
# removing it from the list:

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me")

Test commit
