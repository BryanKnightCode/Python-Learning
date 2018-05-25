# Store a person’s name in a variable, and print a message
# to that person. Your message should be simple, such as, “Hello Eric,
# would you like to learn some Python today?”
message = "Hello Eric, would you like to learn some Python today?"
print(message)


# Store a person’s name in a variable, and then print that person’s
# name in lowercase, uppercase, and titlecase.
albert_einstein = "Albert Einstein"
print(albert_einstein.title(), albert_einstein.upper(), albert_einstein.lower())

# Find a quote from a famous person you admire. Print the
# quote and the name of its author. Your output should look something like the
# following, including the quotation marks:
quote = 'Albert Einstein once said, "A person who never made a mistake never tried anything new"'
print(quote)

# Repeat Exercise 2-5, but this time store the famous person’s
# name in a variable called famous_person. Then compose your message
# and store it in a new variable called message. Print your message

famous_person = 'Albert Einstein once said, "A person who never made a mistake never tried anything new"'
message = famous_person
print(message)

# Store a person’s name, and include some whitespace
# characters at the beginning and end of the name. Make sure you use each
# character combination, "\t" and "\n", at least once.
name = "  \n\tAlbert Einstien   "
print(name)

print(name.rstrip())
print(name.lstrip())
print(name.strip())
