languages = ['spanish', 'russian', 'french', 'english', 'italian']
print("\nOriginal order")
print(languages)

print("\nAlphabetical")
print(sorted(languages))

print("\nReversed Alphabetical")
print(sorted(languages, reverse=True))

print("\nAlphabetical")
languages.sort()
print(languages)

print("\nNumber of languages in this list?")
print(len(languages))