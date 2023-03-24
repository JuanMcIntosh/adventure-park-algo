B_MAX_RIDES = 1
M_MAX_RIDES = 3


basic_band_numbers = range(0, 100)
moderate_band_numbers = range(100, 200)
premium_band_numbers = range(200, 249)


BAND_TYPES = ["basic", "moderate", "premium"]


band_number = int()
band_type = str("")
band_status = ""
upgrade = False
upgraded_band_type = str("")


rides = {"ATV": int(0), "Carting": int(0), "Paintballing": int(0)}


# scan to detect armband. Determine the class armband and the status.


def scan():
    global band_number
    band_number = 0
    global band_status
    band_status = "True"
    global band_type
    band_type = ""
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
                status()
                exit()
            elif band_number in moderate_band_numbers:
                band_type = str(BAND_TYPES[1])
                print(band_type)
                status()
                exit()
            else:
                if band_number in premium_band_numbers:
                    band_type = str(BAND_TYPES[-1])
                    print(band_type)
                    status()
                    exit()
        else:
            print("This is not a number. Please enter the number on you wristband.\n")
            # exit()


# if band status is valid then allow the person to enter the ride
# if not valid tell the person that have to purchase more rides


def status():
    global band_number
    global band_status
    global band_type
    if band_type == "basic":  # BAND_TYPES[0]:
        print("Basic Band!")
        if rides.get("ATV") < B_MAX_RIDES:
            rides["ATV"] = (
                rides.get("ATV", ()) + 1
            )  # upadtes the dictionary value of the item "ATV" to it's value when checked + 1
            print("Enjoy your ATV ride!")
            exit()
    else:
        if band_type == "moderate":  # BAND_TYPES[1]:
            print("Moderate Band!")
            if rides.get("ATV") < M_MAX_RIDES:
                rides["ATV"] = (
                    rides.get("ATV", ()) + 1
                )  # upadtes the dictionary value of the item "ATV" to it's value when checked + 1
            print("Enjoy your ATV ride!")
            exit()
        print(
            band_type + " Band!"
        )  # Print band type if the band is neither a basic nor moderate band. Hence assuming it is a Premuim band
        print("Enjoy your ATV ride!")
        exit()


# Upgrade the adventurer's ride accessibility with payment


def upgrade():
    global band_type
    global prev_band_type
    if band_type == "basic":
        print(
            "You have a "
            + band_type
            + "band. Would you like to upgrade to a moderate(1) or a premium(2) band? Enter the number that matches the band you wish to upgrade to."
        )
        band_upgrade_num = int(input("Enter the number."))
        if band_upgrade_num == 1:
            upgrade = True
            prev_band_type = band_type
            band_type = "moderate"
            status()
        elif band_upgrade_num == 2:
            upgrade = True
            prev_band_type = band_type
            band_type = "premium"
            status()
        else:
            print("Enter either 1 or 2 to select your upgrade.")
            band_upgrade_num = int(input("Enter the number."))
    else:
        if band_type == "moderate":
            print(
                "You have a "
                + band_type
                + "band. Would you like to upgrade to a premium(1) band? If yes press enter the number 1."
            )
        band_upgrade_num = int(input("Enter the number."))
        if band_upgrade_num == 1:
            upgrade = True
            prev_band_type = band_type
            band_type = "premium"
            status()
        else:
            print("You can only be upgraded to a premium band.")
            exit()


def main():
    scan()


main()
