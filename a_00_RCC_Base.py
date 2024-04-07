import pandas


def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("please answer yes / no")


# Function to check if the user input is an integer or a float, as required
def num_check(question, error, num_type):
    valid = False
    while not valid:
        try:
            response = num_type(input(question))
            if response <= 0:
                print(error)
            else:
                return response
        except ValueError:
            print(error)


# Function to ensure the user input is not blank
def not_blank(question, error):
    valid = False
    while not valid:
        response = input(question)
        if response == "":
            print("{}. \nPlease try again \n".format(error))
            continue
        return response


# Function to format numbers as currency
def currency(x):
    return "${:.2f}".format(x)


# Function to get measurement unit from the user
def get_unit(question):
    units = ["", "g", "gram", "grams", "kg", "kilogram",
             "kilograms", "mg", "milligram", "milligrams",
             "l", "liter", "liters"]  # Allowed units
    unit_num = {
        "g": 1,
        "kg": 1000,
        "mg": 0,
        "l": 1
    }
    valid = False
    while not valid:
        unit = input(question).lower()
        if unit in units:
            return unit

        # check for exit code...
        elif unit == "xxx":
            return unit

        else:

            print("\nPlease enter either: (g,kg,mg,l)"
                  "\ngram, kilogram, milligram, Liter")
            print()
