# Python’s sort() method makes it relatively easy to sort a list. Imagine we
# have a list of cars and want to change the order of the list to store them
# alphabetically. To keep the task simple, let’s assume that all the values in
# the list are lowercase.
cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)

# You can also sort this list in reverse alphabetical order by passing the
# argument reverse=True to the sort() method. The following example sorts
# the list of cars in reverse alphabetical order:
cars = ['bmw','audi','toyota','subaru']
cars.sort(reverse=True)
print(cars)


# To maintain the original order of a list but present it in a sorted order, you
# can use the sorted() function. The sorted() function lets you display your list
# in a particular order but doesn’t affect the actual order of the list.
cars = ['bmw','audi','toyota','subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

cars = ['bmw','audi','toyota','subaru']
print(len(cars))
