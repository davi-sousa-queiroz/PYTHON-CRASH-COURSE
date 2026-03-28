import time
def display_message():
    print("\nI'm learning about functions!")

display_message()

def favorite_book(book):
    print(f"\n{book} is my favorite book!")

favorite_book("PYTHON CRASH COURSE")

def make_shirt(size, message):
    print(f"\nThe size of your shirt is {size}, and the message '{message}' will be printed on it.")

make_shirt('G', "Jesus loves you")

make_shirt(message = 'I love Jesus', size = 'S')

def make_shirt(size = 'large', message = 'I love Python'):
    print(f"\nThe size of your shirt is {size}, and the message '{message}' will be printed on it.")

make_shirt()

make_shirt(size = 'medium')

make_shirt(size = 'Extra Large', message = 'I like coding')

#def city_country():
#    while True:
#        city = input("\nEnter a city:\n>> ").title()
#        country = input("\nEnter a country:\n>> ").title()
#        place = {'city': city, 'country': country}
#        return place

#full_place = city_country()
#print(full_place)

def make_album(artist, album, songs=None):

    album_dict = {"artist": artist, "album": album}

    if songs is not None:
        album_dict["songs"] = songs

    return album_dict

print(make_album("Me", "One of my albums", 633))

msgs = ["Hi, how are U?", "Good, and U?", "im good 2"]

def show_msgs():
    for msg in msgs:
        print(msg)

show_msgs()



while True:
        artist = input("Enter artist name: ")
        album = input("Enter album name: ")
        songs = input("Enter number of songs (optional): ")

        if songs != '':
            print(make_album(artist, album, songs))
        elif songs == "":
            print(make_album(artist, album))
        else:
            print("Enter a valid number of songs")