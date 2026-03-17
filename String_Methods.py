# FORMATING PRINT STATEMENTS

#print("Whitespace")
#print("\tWhitespace")
#print("Python\nWhiteSpace")
#print("Python\n\tWhiteSpace")

# REMOVING SPACES

#language = 'python '
#language = language.strip()
#print(language)

#language = 'python '
#language = language.rstrip()
#print(language)

#language = 'python '
#language = language.lstrip()
#print(language)


#favorite_language = input("Enter favorite programing language: ")
#favorite_language = favorite_language.strip()
#favorite_language = favorite_language.title()
#print(favorite_language)

# REMOVING PREFIXES

#link = "https://github.com/davi-sousa-queiroz"

#print(link.removeprefix("https://github.com/"))

#link = input("Enter your GitHub profile link: ")
#print(f"Hello {link.removeprefix('https://github.com/')}! 😊")