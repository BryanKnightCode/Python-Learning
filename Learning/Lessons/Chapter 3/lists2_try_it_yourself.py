# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
# would you invite? Make a list that includes at least three people you’d like to
# invite to dinner. Then use your list to print a message to each person, inviting
# them to dinner.
invitations = ['jim morrison', 'mr. rogers', 'sidney crosby']
print("My Invitation list includes " + invitations[0].title() + ', ' + invitations[1].title() + ', ' + invitations[2].title() + ".")
print("I like your music " + invitations[0].title() + '.')
print("Thanks for all that you have done "+ invitations[1].title() + '!')
print("Do you think you're the best Hockey player in the world " + invitations[2] + '?')

# 3-5. Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
print(invitations)
cancelled = 'jim morrison'
invitations.remove(cancelled)
print(invitations)
print("\nThe guest " + cancelled.title() + " can no longer make it and has cancelled.")

# Modify your list, replacing the name of the guest who can’t make it with
# the name of the new person you are inviting.
invitations.insert(0, 'ghandi')
print(invitations)

# Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
# statement to the end of your program informing people that you found a
# bigger dinner table.
print("You are invited to a party! Here is the current list- " + invitations[0].title() + ', ' + invitations[1].title() + ', ' + invitations [2].title() + '.')
print( "I have found a bigger table, We will be inviting more people. Who should I invite? ")

# Use insert() to add one new guest to the beginning of your list.
invitations.insert(0, 'john doe')
# Use insert() to add one new guest to the middle of your list.
invitations.insert(2, 'binx bah')
# Use insert() to add one new guest to the end of your list. (practice)
invitations.insert(5, 'salem bah')
# • Use append() to add one new guest to the end of your list.
invitations.append('maigy moo')
print(invitations)

# Print a new set of invitation messages, one for each person in your list.
invite = "You've been invited! "
print(invite + invitations[0])
print(invite + invitations[1])
print(invite + invitations[2])
print(invite + invitations[3])
print(invite + invitations[4])
print(invite + invitations[5])
print(invite + invitations[6])


# Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.
print("The new dinner table will not be arriving. I will only be able to invite two people. ")


# Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, print
# a message to that person letting them know you’re sorry you can’t invite
# them to dinner.
print(invitations)
john_doe_uninvite = invitations.pop(0)
print("You have been uninvited from my party due to unforseen circumstances " + john_doe_uninvite.title())

print(invitations)
ghandi_uninvite = invitations.pop(0)
print("You have been uninvited from my party due to unforseen circumstances " + ghandi_uninvite.title())

print(invitations)
binx_bah_uninvite = invitations.pop(0)
print("You have been uninvited from my party due to unforseen circumstances " + binx_bah_uninvite.title())

print(invitations)
mr_rogers_uninvite = invitations.pop(0)
print("You have been uninvited from my party due to unforseen circumstances " + mr_rogers_uninvite.title())

print(invitations)
sidney_crosby_uninvite = invitations.pop(0)
print("You have been uninvited from my party due to unforseen circumstances " + sidney_crosby_uninvite.title())

# Print a message to each of the two people still on your list, letting them
# know they’re still invited.
print(invitations)
print("You are still invited to the party " + invitations[0] + ", " + invitations[1] + ".")

# Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end
# of your program.
del invitations[0]
print(invitations)
del invitations[0]
print(invitations)