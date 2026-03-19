import time
vacations = {}

polling = True
while polling:
    name = input("\nWhat is your name?\n>> ").title()
    time.sleep(1)
    print(f"Hello {name}!")
    time.sleep(1)
    place = input("Where is your dream vacation?\n>> ").title()
    print(f"\n{place} is a great vacation spot!")
    time.sleep(1)
    vacations[name] = place
    poll_again = input("\nWould you like to continue the poll? (y/n) \n>> ").lower()
    if poll_again == "y":
        continue
    else:
        print("\nThank you for your time!")
        time.sleep(1)
        print("\nRESULTS")

        for name, place in vacations.items():
            time.sleep(1)
            print(f"\n{name} wants to go to {place}.")
            time.sleep(1)


sandwich_orders = ['pastrami',
                   'bacon',
                   'pastrami',
                   'ham',
                   'pastrami',
                   'cheese',
                   'pastrami',
                   'chicken']

finished_sandwiches = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    print("\npastrami removed.")
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)
    print(f"\n{sandwich} complete!")

print("\nSandwiches made:")
for sandwich in finished_sandwiches:
    print(f"\n\t{sandwich}")

print("\nBon Apitite!")

rental_car = "What car would you like to purchase?"
rental_car += "\n>> "
choice = input(rental_car)
print(f"\n I'll see if i can find you a {choice} in our garage.")
print(f"\n We found a {choice} in our stock!\n\n")

#=======================================================================================================================

print("Welcome to our restaurant!\n")
print("A table for how many today?\n")
customers = input("\t>> ")
customers = int(customers)
if customers < 8:
    print(f"\n{customers} people? Sounds good.")
    print(f"We have a table for {customers} right over there!")
else:
    print(f"\n{customers} people?! That's a lot!")
    print(f"You'll have to make a reserve if your dinner is for {customers}.\n")

print("Enter a number: ")
number = input("\n>> ")
number = int(number)
if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")

running = True
while running:
    print("\nEnter a topping to add to your pizza (q to quit): ")
    topping = input("\t\n>> ")
    if topping == "q":
        print("\nThank you for your time!")
        running = False
    else:
        print(f"\nI'll add {topping} to your pizza.")

running = True
while running:
    print("\nWelcome to the movies!")
    print("\nWhat is your age?")
    age = int(input("\n\t>> "))
    if age < 3:
        print(f"\n{age} year olds get a movie ticket for free!")
    elif age >= 3 and age < 12:
        print(f"\n{age} year olds get a movie ticket for 12$!")
    elif age >= 12:
        print(f"\n{age} year olds get a movie ticket for 15$!")



