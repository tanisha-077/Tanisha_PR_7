import math


def compound_interest(principal, rate, time):
    amount = principal * (1 + rate / 100) ** time
    return amount


def circle_area(radius):
    return math.pi * radius * radius


def rectangle_area(length, width):
    return length * width


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


if __name__ == "__main__":
    print("Math Utilities Module")