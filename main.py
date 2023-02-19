B_MAX_RIDES = 1
M_MAX_RIDES = 3


basic_band_numbers = range(0, 99)
moderate_band_numbers = range(100, 199)
premium_band_numbers = range(200, 249)


BAND_TYPES = ["basic", "moderate", "premium"]
RIDES = ["ATV", "Carting", "Paintballing"]


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)


ride_status = 0
band_number = int()
band_type = str()
band_status = ""


# check band status funtion


def status():
    for i in RIDES:
        if ride_status < B_MAX_RIDES:
            print("You may enter the ride. Enjoy your adventure!")
        else:
            print(
                "You have used up all your rides on the tier ticket you purhased. You may purchase more rides if you wish."
            )
        # exit()


# scan to detect armband within a certain proximity of scanner. Determine the class armband and the status.


def scan():
    while True:
        band_number = input("What is your wristband number?\n")
        if band_number.isdigit():
            band_number = int(band_number)
            for band_number in basic_band_numbers:
                band_type = BAND_TYPES[0]
                status()

    print("This is not a number. Please enter the number on you wristband.")


# else:
#     print("Please enter the number on you wristband.")


# if band status is valid then allow the person to enter the ride
# if not valid tell the person that have to purchase more rides


def main():
    scan()


main()
