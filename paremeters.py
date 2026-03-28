def greet(name, age):
    print(f"\nHello {name}, you are {age} years old!")

while True:
    name = input("\nEnter your name: ").title()
    age = input("\nEnter your age: ")

    greet(name, age)

