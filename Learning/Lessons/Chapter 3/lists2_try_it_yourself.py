invitations = ['jim morrison', 'mr. rogers', 'sidney crosby']
print("My Invitation list includes " + invitations[0].title() + ', ' + invitations[1].title() + ', ' + invitations[2].title() + ".")
print("I like your music " + invitations[0].title() + '.')
print("Thanks for all that you have done "+ invitations[1].title() + '!')
print("Do you think you're the best Hockey player in the world " + invitations[2] + '?')

print(invitations)
cancelled = 'jim morrison'
invitations.remove(cancelled)
print(invitations)
print("\nThe guest " + cancelled.title() + " can no longer make it and has cancelled.")

invitations.insert(0, 'ghandi')
print(invitations)

print("You are invited to a party! Here is the current list- " + invitations[0].title() + ', ' + invitations[1].title() + ', ' + invitations [2].title() + '.')
print( "I have found a bigger table, We will be inviting more people. Who should I invite? ")

invitations.insert(0, 'john doe')
invitations.insert(2, 'binx bah')
invitations.insert(5, 'salem bah')
invitations.append('maigy moo')
print(invitations)

invite = "You've been invited! "
print(invite + invitations[0])
print(invite + invitations[1])
print(invite + invitations[2])
print(invite + invitations[3])
print(invite + invitations[4])
print(invite + invitations[5])
print(invite + invitations[6])

print("The new dinner table will not be arriving. I will only be able to invite two people. ")

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

print(invitations)
print("You are still invited to the party " + invitations[0] + ", " + invitations[1] + ".")

del invitations[0]
print(invitations)
del invitations[0]
print(invitations)