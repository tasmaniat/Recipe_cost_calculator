# checks that input is either a float or an
# integer that is more than zero. Takes in custom error message
def num_check(question, error, num_type=float):
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


def get_unit(question):
    # Allowed units list
    units = ["", "g", "gram", "grams", "kg", "kilogram",
             "kilograms", "mg", "milligram", "milligrams",
             "l", "liter", "liters"]

    valid = False
    while not valid:
        unit = input(question).lower()
        # checks if unit is in the list of allowed units
        if unit in units:
            return unit

        # check for exit code...
        elif unit == "xxx":
            return unit
        else:
            # If unit is not valid, prints an error message
            print("\nPlease enter either: (g,kg,mg,l)"
                  "\ngram, kilogram, milligram, Liter")
            print()


# Main Routine goes here...
# Loop for testing purposes
user_choice = ""
while user_choice != "xxx":
    print()
    get_cost = num_check("how much? ", "please enter an whole number", float)

    # ASk user for choice and check it's valid

    what_unit = get_unit("Unit? (or leave blank): ")

    # print out choice for comparison purposes
    print("You chose ", get_cost, what_unit)


