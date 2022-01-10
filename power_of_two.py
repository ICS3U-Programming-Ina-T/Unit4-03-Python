#!/usr/bin/env python3

# Created by: Ina Tolo
# Created on: Jan. 10, 2022
# This program asks the user to enter a whole number.
# It then uses a for loop to determine the calculate
# the power of two from zero until the entered number.

def main():
    # initialize the loop counter and power of two
    loop_counter = 0
    power_of_two = 0

    # get the user number as a string
    user_number_string = input("Enter a whole number: ")
    print("")

    try:
        # converts user input to integer
        user_number_int = int(user_number_string)

        if user_number_int >= 0:
            # calculate the power of two from 0 to user number
            for loop_counter in range(user_number_int + 1):
                power_of_two = loop_counter**2
                print("{}^2 = {}".format(loop_counter, power_of_two))
        else:
            print("Please enter a whole number!")
    except Exception:
        print("{} is not a number.". format(user_number_string))


if __name__ == "__main__":
    main()
