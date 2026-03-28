class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Welcome to {self.restaurant_name}, home of the finest {self.cuisine_type}!")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

restaurant = Restaurant("Luigi's Palace", "Italian Cuisine")

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):

        super().__init__(restaurant_name, cuisine_type)

        self.flavors = ["", "Vanilla", "Chocolate", "Strawberry", "Cookies & Cream"]

    def flavor(self):
        print(" ------------ FLAVORS ------------- ")
        for i, flavor in enumerate(self.flavors):
            if i == 0:
                continue
            print(i, flavor)

IceCreamStand = IceCreamStand("Bob's Ice Cream", "Ice Cream")

IceCreamStand.flavor()

class User:

    def __init__(self, first_name, last_name, age, net_worth):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.net_worth = net_worth

    def describe(self):
        user_info = {"\nFirst Name:": self.first_name,
                     "Last Name:" : self.last_name,
                     "Age:": self.age,
                     "Net Worth USD$:": self.net_worth}

        for item, value in user_info.items():
            print(item, value)

    def greet(self):
        print("-------------- USER INFO ---------------")
        print(f"Welcome back {self.first_name}!")

my_user = User("Davi", "Queiroz", "16", "0.00$")
my_user.greet()
my_user.describe()

class Privileges:

    def __init__(self):
        self.privileges = ["\n",
                           "Can add post",
                           "Can delete post",
                           "Can ban user",
                           "Can access app data",
                           "Can comment",
                           "Can message other admins",
                           "Can participate in meetings",
                           "Can mute",
                           "Can delete messages"]

    def show_privileges(self):
        for i, item in enumerate(self.privileges):
            if i == 0:
                continue
            print(i,"|", item)

class Admin(User):

    def __init__(self, first_name, last_name, age, net_worth, ):

        super().__init__(first_name, last_name, age, net_worth)

        self.privileges = Privileges()

    def show_privileges(self):
        for i, item in enumerate(self.privileges):
            if i == 0:
                continue
            print(i,"|", item)

my_admin = Admin("Davi", "Queiroz", 16, 0.00)
print("------------- PRIVILEGES ------------")
my_admin.privileges.show_privileges()
