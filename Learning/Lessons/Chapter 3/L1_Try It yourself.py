# 3-1. Names: Store the names of a few of your friends in a list called names. Print
# each person’s name by accessing each element in the list, one at a time.
names = ['cliff', 'mark', 'johnnie']
print(names[0].title())
print(names[1].title())
print(names[-1].title())


# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
# printing each person’s name, print a message to them. The text of each message
# should be the same, but each message should be personalized with the
# person’s name.
message1 = "Hello, " + names[0].title() + ", How are you?"
print(message1)

message2 = "Hi, " + names[1].title() + ", How do you do?"
print(message2)

message3 = "Yo, " + names[2].title() + " is a dork."
print(message3)

# Your Own List: Think of your favorite mode of transportation, such as a
# motorcycle or a car, and make a list that stores several examples. Use your list
# to print a series of statements about these items, such as “I would like to own a
# Honda motorcycle.”
transportation = ['harley davidson', 'ford mustang', 'boeing jet']

transmessage1 = "I would like to own a " + transportation[0].title()
print(transmessage1)

transmessage2 = "Do you own a "+ transportation[1].title() + " or a " + transportation[2].title() + "?"
print(transmessage2)

transmessage3 = "I doubt you own a " + transportation[2].title() + "."
print(transmessage3)