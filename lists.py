#car_makes = ["BMW", "Honda", "Nissan", "Ford", "Mercedes"]

#print("The first 3 items in the list are: ")
#for car_make in car_makes[:3]:
#    print(car_make)

#print("Three items from the middle of the list are: ")
#for car in car_makes[1:4]:
#    print(car)

#print(car_makes[0])
#print(car_makes[1])
#print(car_makes[-1])

#print(f"My favorite car make is: {car_makes[-3]}")

#dinner_guests = []

#letters = []

#print("Let's Plan Dinner!")
#guest1 = input("Who will you invite first?: ")
#guest2 = input("Who else?: ")
#guest3 = input("Last guest!: ")
#dinner_guests.append(guest1)
#dinner_guests.append(guest2)
#dinner_guests.append(guest3)
#letter1 = input(f"Write a short invitation letter for {guest1}!:  ")
#letters.append(letter1)
#letter2 = input(f"Now write a short invitation letter for {guest2}!:  ")
#letters.append(letter2)
#letter3 = input(f"Lastly, write a short invitation letter for {guest3}!:  ")
#letters.append(letter3)
#print("")
#print(f"Invitation for {guest1}: \n{letters[0]}")
#print()
#print(f"Invitation for {guest2}: \n{letters[1]}")
#print()
#print(f"Invitation for {guest3}: \n{letters[2]}")
#print("")
#send = input("Ready to mail? (y/n): ")
#if send == "y":
    #print("Mail sent!")
    #print("")
    #print(f"Well done! Dinner with {guest1}, {guest2}, and {guest3} is official.")
#else:
    #print("Mail not sent!")

#garage = []
#
#while True:
#
#    print("1. Add Car To Garage\n2. View Cars\n3. Remove Car From Garage\n4. Exit")
#    choice = input("Enter your choice: ")
#    if choice == "1":
#        car_selection = input ("Enter the name of your new car: ").lower()
#        garage.append(car_selection)
#        print(f"{car_selection} was added to your garage.")
#    elif choice == "2":
#        if garage:
#            for car in garage:
#                print(car)
#        else:
#            print("No cars in your garage.")
#    elif choice == "3":
#        for car in garage:
#            print(car)
#            remove_car = input("Enter the name of the car to be removed").lower()
#            if remove_car in garage:
#                garage.remove(remove_car)
#                print(f"{remove_car} was removed from your garage.")
#            else:
#                print("Car is not in the garage.")
#    elif choice == "4":
#        print("Until next time.")
#        break#





