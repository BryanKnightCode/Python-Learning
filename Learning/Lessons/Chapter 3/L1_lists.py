# In Python, square brackets ([]) indicate a list, and individual elements
# in the list are separated by commas. Here’s a simple example of a list that
# contains a few kinds of bicycles:
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Lists are ordered collections, so you can access any element in a list by
# telling Python the position, or index, of the item desired. To access an element
# in a list, write the name of the list followed by the index of the item
# enclosed in square brackets.
print(bicycles[0])

# This is the result you want your users to see—clean, neatly formatted output.
print(bicycles[0].title())

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1])
print(bicycles[3])

# Python has a special syntax for accessing the last element in a list. By asking
# for the item at index -1, Python always returns the last item in the list:
print(bicycles[-1])

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)