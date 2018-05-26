invitations = ['jim morrison', 'mr. rogers', 'sidney crosby']
print("My Invitation list includes " + invitations[0].title() + ', ' + invitations[1].title() + ', ' + invitations[2].title() + " .")
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

print("You are invited to a party! Here is the current list " + invitations[0].title() + ', ' + invitations[1].title() + ', ' + invitations [2].title() + '.')
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