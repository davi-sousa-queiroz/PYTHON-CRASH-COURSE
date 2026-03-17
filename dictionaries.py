alien_0 = {"color": "green",
           "points": 5}

print(alien_0["color"])
print(alien_0["points"])
me = {
        "Name" : "Davi",
        "Age" : 16,
        "Country" : "Brazil",
        "State" : "MG",
        "Sex" : "male"
    }

for key, value in me.items():
    print(f"{key} : {value}")
    print("")


people = {
        "Chris" : 10,
        "Davi" : 13,
        "Nathan" : 7,
        "John" : 5,
        "Samantha" : 4,
        "Alice" : 77
    }

print(f"Chris's favorite number is {people["Chris"]}!")
print(f"Davi's favorite number is {people["Davi"]}!")
print(f"Nathan's favorite number is {people["Nathan"]}!")
print(f"John's favorite number is {people["John"]}!")
print(f"Alice's favorite number is {people["Alice"]}!")

for key, value in people.items():
    print(f"{key}'s favorite number is {value}!\n")

for value in people.values():
    print(value)
    print("")

rivers = {
    "Nile" : "Egypt",
    "Amazon" : "Brazil",
    "Mississippi" : "USA"
    }

for key, value in rivers.items():
    print(f"The {key} runs through {value}.\n")

for key in rivers:
    print(f"{key}\n")

for country in rivers.values():
    print(f"{country}\n")

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'rust',
    'phil' : 'python'
}

potential_pollers = {
    'sarah' : 'c',
    'edward' : 'rust',
    'phil' : 'python',
    'jonathan' : 'python',
    'blake' : 'javaSkript'
}

for key, value in potential_pollers.items():
    if key in favorite_languages:
        print(f"Thank you for taking the poll {key}!\n")
    else:
        print(f"Please take the poll {key}!\n")




people = [

    {"Name" : "Davi", "Age" : 16, "Country" : "Brazil", "State" : "MG", "Sex" : "male"},
    {"Name" : "Clarisse", "Age" : 18, "Country" : "Brazil", "State" : "MG", "Sex" : "Female"},
    {"Name" : "Jack", "Age" : 17, "Country" : "USA", "State" : "CT", "Sex" : "male"}

          ]

for dictionary in people:
    for key, value in dictionary.items():
       print(f"{key} : {value}\n")

pet_1 = {"animal" : "dog", "owner" : "fern"}

pet_2 = {"animal" : "cat", "owner" : "jack"}

pet_3 = {"animal" : "hamster", "owner" : "lily"}

pet_4 = {"animal" : "spider", "owner" : "ben"}

pet_5 = {"animal" : "parrot", "owner" : "harold"}

pets = [pet_1, pet_2, pet_3, pet_4, pet_5]
for pet in pets:
    for key, value in pet.items():
        print(f"{key} : {value}\n")


favorite_places = {"davi" : ['home', 'restaurants', 'libraries'],
                   "clarisse" : ['venice', 'shibuya', 'cancún'],
                   "jack" : ['france', 'spain', 'china']}

for key, values in favorite_places.items():
    print(f"{key}'s favorite places are: {', '.join(values)}!\n")

people = {
        "Chris" : [10, 7, 9, 11],
        "Davi" : [13, 5, 84, 6],
        "Nathan" : [7, 8, 4, 99],
        "John" : [5, 1, 11, 88],
        "Samantha" : [4, 7, 8, 9],
        "Alice" : [77, 87, 44, 100]
    }

for key, values in people.items():
    print(f"{key}'s favorite numbers are: {values}")

