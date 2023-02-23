B_MAX_RIDES = 1
M_MAX_RIDES = 3


basic_band_numbers = range(0, 100)
moderate_band_numbers = range(100, 200)
premium_band_numbers = range(200, 249)


BAND_TYPES = ["basic", "moderate", "premium"]

# ride_status = 0
band_number = int()
band_type = str("")
band_status = ""


rides = {"ATV": int(0), "Carting": int(0), "Paintballing": int(0)}

# check band status funtion


def status():
    if band_type == str(BAND_TYPES[0]):
        while rides.values("ATV") < B_MAX_RIDES:
            # rides.update({"ATV":  })
            # rides.values("ATV") =
            rides.update({"ATV": rides.values("ATV" + int(1))})
            print("Enjoy your " + rides.values(("ATV")) + "ride!")
    else:
        print("oyyee!!")
    # elif band_type == BAND_TYPES[1]:


# def status():
#     for i in RIDES:
#         if ride_status < B_MAX_RIDES:
#             print("Go ahead! Enjoy your adventure!")
#         else:
#             print(
#                 "You have used up all your rides on the tier ticket you purhased. You may purchase more rides if you wish."
#             )
#         # exit()


# scan to detect armband within a certain proximity of scanner. Determine the class armband and the status.


def scan():
    while True:
        band_number = input("What is your wristband number?\n")
        if (
            band_number.isdigit()
        ):  # if band_number is a digit then store the value in the same variable as an integer
            band_number = int(band_number)
            if (
                band_number in basic_band_numbers
            ):  # if the value stored in band_number is in basic_band_numbers (a range of numbers) then assign to band_type the string stored in the constant BAND_TYPES
                band_type = str(BAND_TYPES[0])
                print(band_type)
                exit()
            elif band_number in moderate_band_numbers:
                band_type = str(BAND_TYPES[1])
                print(band_type)
                exit()
            else:
                if band_number in premium_band_numbers:
                    band_type = str(BAND_TYPES[-1])
                    print(band_type)
                    exit()
        else:
            print("This is not a number. Please enter the number on you wristband.\n")
            # exit()


# if band status is valid then allow the person to enter the ride
# if not valid tell the person that have to purchase more rides


def main():
    scan()


status()
main()
