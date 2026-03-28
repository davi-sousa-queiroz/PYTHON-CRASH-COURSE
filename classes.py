# Object-Oriented-Programming (Classes)

class User:

    def __init__(self, first_name, middle_name, last_name, date_of_birth, profession, net_worth):

        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.profession = profession
        self.net_worth = net_worth
        self.login_attempts = 0

    def greet(self):
        print(f"\nHello {self.first_name} {self.last_name}, Welcome to your profile!")

    def name_info(self):
        print(f"\nFirst name: {self.first_name}")
        print(f"Middle name: {self.middle_name}")
        print(f"Last name: {self.last_name}")

    def birthday(self):
        print(f"\nYour date of birth:\t{self.date_of_birth}")

    def work(self):
        print(f"\nYour profession: {self.profession}")
        print(f"Your net worth: {self.net_worth}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def show_login_attempts(self):
        print(self.login_attempts)

my_info = User("Davi",
               "Sousa",
               "Queiroz",
               "June 28th, 2009",
               "Machine-Learning Engineer",
               "5,000,000.00 USD$")
my_info.greet()
my_info.name_info()
my_info.birthday()
my_info.work()

user_info = User("John",
                 "Don",
                 "Lee",
                 "March 13th, 2021",
                 "Student",
                 "0.00 USD$")
user_info.greet()
user_info.name_info()
user_info.birthday()
user_info.work()

new_user = User(", ", ", ", ", ", "", ", ", "")
new_user.show_login_attempts()

new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.increment_login_attempts()

new_user.show_login_attempts()

general_info = User("Guest", "", "", "N/A", "", "")
#----------------------------------------------------------------------------------------------------------------------
class Restaurant:

    def __init__(self, restaurant_name, cuisine_type,):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_serverd = 0

    def describe_restaurant(self):
        print(f"\nWelcome to {self.restaurant_name}, home of the finest {self.cuisine_type}!")

    def open_restaurant(self):
        print(f"\n{self.restaurant_name} is now open!")

    def set_number_served(self, number):
        number = self.number_serverd

        print(number)
restaurant = Restaurant("Midnight Mozzarella", "Late-night pasta & pizza spot")

print(f"Restaurant: {restaurant.restaurant_name}")
print(f"Cuisine: {restaurant.cuisine_type}")

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant2 = Restaurant("Tapas Temptation", "Spanish Cuisine")

print(f"Restaurant: {restaurant2.restaurant_name}")
print(f"Cuisine: {restaurant2.cuisine_type}")

restaurant2.describe_restaurant()
restaurant2.open_restaurant()

restaurant3 = Restaurant("Dragon Slurp", "Ramen Shop")

print(f"Restaurant: {restaurant3.restaurant_name}")
print(f"Cuisine: {restaurant3.cuisine_type}")

restaurant3.describe_restaurant()
restaurant3.open_restaurant()

restaurant4 = Restaurant("Smoke and Sizzle", "BBQ Grill")

print(f"Restaurant: {restaurant4.restaurant_name}")
print(f"Cuisine: {restaurant4.cuisine_type}")

restaurant4.describe_restaurant()
restaurant4.open_restaurant()

restaurant.set_number_served(13)

# ---------------------------------------------------------------------------------------------------------------------

class Cat:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} sat down.")

    def meow(self):
        print(f"{self.name} meowed.")


name = input("\nEnter your cats name: ").title()
age = input("\nEnter your cats age: ")

my_cat = Cat(name, age)

name = input("\nEnter the name of your second cat: ").title()
age = input("Enter the age of your second cat: ")

my_cat2 = Cat(name, age)

print(f"\nMy cat's name is {my_cat.name},")
print(f"and it's {my_cat.age} years old.")

my_cat.sit()
my_cat.meow()

print(f"\nMy other cat's name is {my_cat2.name},")
print(f"and it's {my_cat2.age} years old.")

my_cat2.sit()
my_cat2.meow()
