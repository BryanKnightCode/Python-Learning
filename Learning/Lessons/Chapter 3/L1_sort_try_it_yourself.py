# Store the locations in a list. Make sure the list is not in alphabetical order.
# Print your list in its original order. Don’t worry about printing the list neatly,
# just print it as a raw Python list.

locations = ['disney', 'australia', 'houston', 'tampa', 'vegas']
print("\nOriginal order")
print(locations)

# Use sorted() to print your list in alphabetical order without modifying the
# actual list.
print("\nAlphabetical")
print(sorted(locations))


# Show that your list is still in its original order by printing it.
print("\nOriginal order")
print(locations)

# Use sorted() to print your list in reverse alphabetical order without changing
# the order of the original list.
print("\nReversed order")
print(sorted(locations, reverse=True))

# Show that your list is still in its original order by printing it again.
print("\nOriginal order")
print(locations)

# Use reverse() to change the order of your list. Print the list to show that its
# order has changed.
print("\nReversed")
locations.reverse()
print(locations)

# Use reverse() to change the order of your list again. Print the list to show
# it’s back to its original order.
print("\nOriginal order")
locations.reverse()
print(locations)

print("\nAlphabetical")
locations.sort()
print(locations)

print("\nReverse Alphabetical")
locations.sort(reverse=True)
print(locations)