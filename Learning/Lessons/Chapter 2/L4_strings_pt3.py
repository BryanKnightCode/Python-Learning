# Assigning variables to strings
# Concatenating two strings. (to combine strings). the " " adds a space.
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

print(full_name)

# Trying concatenation a different way using the titlename method. I needed to add quotes around ! to ensure it was still a string.
print("Hello, " + full_name.title() + "!")

# The preferred method of concatenation. Stroing the message in a variable is preferred. 
message = "Hello, " + full_name.title() + "!"
print(message)

