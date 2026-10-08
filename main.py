import datetime
import time
import math
import random
import string
import uuid

from utilities.file_operations import (
    create_file,
    write_file,
    read_file,
    append_file
)

from utilities.math_utils import (
    compound_interest,
    circle_area,
    rectangle_area,
    celsius_to_fahrenheit
)

def datetime_menu():

    while True:
        print("\nDatetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates")
        print("3. Format date")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            now = datetime.datetime.now()
            print("Current Date and Time:", now.strftime("%Y-%m-%d %H:%M:%S"))

        elif choice == "2":
            date1 = input("Enter first date (YYYY-MM-DD): ")
            date2 = input("Enter second date (YYYY-MM-DD): ")

            d1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
            d2 = datetime.datetime.strptime(date2, "%Y-%m-%d")

            difference = abs((d2 - d1).days)

            print("Difference:", difference, "days")

        elif choice == "3":
            date = datetime.datetime.now()
            print("Formatted Date:", date.strftime("%d-%m-%Y %H:%M:%S"))

        elif choice == "4":
            input("Press Enter to start stopwatch...")
            start = time.time()

            input("Press Enter to stop stopwatch...")
            end = time.time()

            print("Time:", round(end - start, 2), "seconds")

        elif choice == "5":
            seconds = int(input("Enter countdown seconds: "))

            while seconds > 0:
                print("Remaining:", seconds)
                time.sleep(1)
                seconds -= 1

            print("Time's up!")

        elif choice == "6":
            break

        else:
            print("Invalid choice!")

def math_menu():

    while True:
        print("\nMathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculation")
        print("4. Area of Geometric Shapes")
        print("5. Logarithm")
        print("6. Unit Conversion")
        print("7. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            number = int(input("Enter a number: "))
            print("Factorial:", math.factorial(number))

        elif choice == "2":
            principal = float(input("Enter principal amount: "))
            rate = float(input("Enter rate of interest (%): "))
            years = float(input("Enter time (years): "))

            amount = compound_interest(principal, rate, years)

            print("Compound Amount:", round(amount, 2))

        elif choice == "3":
            angle = float(input("Enter angle in degrees: "))

            radians = math.radians(angle)

            print("Sin:", math.sin(radians))
            print("Cos:", math.cos(radians))
            print("Tan:", math.tan(radians))

        elif choice == "4":
            print("\n1. Circle")
            print("2. Rectangle")

            shape = input("Choose shape: ")

            if shape == "1":
                radius = float(input("Enter radius: "))
                print("Area:", circle_area(radius))

            elif shape == "2":
                length = float(input("Enter length: "))
                width = float(input("Enter width: "))

                print("Area:", rectangle_area(length, width))

            else:
                print("Invalid choice!")

        elif choice == "5":
            number = float(input("Enter number: "))
            print("Log:", math.log(number))

        elif choice == "6":
            celsius = float(input("Enter temperature in Celsius: "))

            print(
                "Fahrenheit:",
                celsius_to_fahrenheit(celsius)
            )

        elif choice == "7":
            break

        else:
            print("Invalid choice!")

def random_menu():

    while True:
        print("\nRandom Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Random Sampling")
        print("6. Coin Toss Game")
        print("7. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":

            number = random.randint(1, 100)

            print("Random Number:", number)

        elif choice == "2":

            numbers = []

            for i in range(5):
                numbers.append(random.randint(1, 100))

            print("Random List:", numbers)

        elif choice == "3":

            length = int(input("Enter password length: "))

            characters = string.ascii_letters + string.digits + "!@#$"

            password = ""

            for i in range(length):
                password += random.choice(characters)

            print("Generated Password:", password)

        elif choice == "4":

            otp = random.randint(100000, 999999)

            print("Generated OTP:", otp)

        elif choice == "5":

            data = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

            sample = random.sample(data, 3)

            print("Random Sample:", sample)

        elif choice == "6":

            result = random.choice(["Head", "Tail"])

            print("Coin Toss Result:", result)

        elif choice == "7":
            break

        else:
            print("Invalid choice!")

def uuid_menu():

    print("\nGenerate Unique Identifier:")

    unique_id = uuid.uuid4()

    print("Generated UUID:", unique_id)

def file_menu():

    while True:

        print("\nFile Operations:")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":

            filename = input("Enter file name: ")

            create_file(filename)

        elif choice == "2":

            filename = input("Enter file name: ")
            data = input("Enter data to write: ")

            write_file(filename, data)

        elif choice == "3":

            filename = input("Enter file name: ")

            read_file(filename)

        elif choice == "4":

            filename = input("Enter file name: ")
            data = input("Enter data to append: ")

            append_file(filename, "\n" + data)

        elif choice == "5":
            break

        else:
            print("Invalid choice!")

def explore_module():

    module_name = input(
        "\nEnter module name to explore "
        "(math/random/datetime/time/uuid): "
    )

    if module_name == "math":
        print(dir(math))

    elif module_name == "random":
        print(dir(random))

    elif module_name == "datetime":
        print(dir(datetime))

    elif module_name == "time":
        print(dir(time))

    elif module_name == "uuid":
        print(dir(uuid))

    else:
        print("Module not available!")

def main():

    while True:

        print("\nWelcome to Multi-Utility Toolkit")

        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifier (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            datetime_menu()

        elif choice == "2":
            math_menu()

        elif choice == "3":
            random_menu()

        elif choice == "4":
            uuid_menu()

        elif choice == "5":
            file_menu()

        elif choice == "6":
            explore_module()

        elif choice == "7":
            print("Thank you for using the Multi-Utility Toolkit!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()