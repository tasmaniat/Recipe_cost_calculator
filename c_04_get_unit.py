def get_unit(question):
    units = ["", "g", "gram", "grams", "kg", "kilogram",
             "kilograms", "mg", "milligram", "milligrams",
             "l", "liter", "liters"]  # Allowed units

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


# Main Routine goes here...

# Loop for testing purposes
user_choice = ""
while user_choice != "xxx":
    # ASk user for choice and check it's valid
    user_choice = get_unit("Unit? ( g, kg, mg, L, "
                           "or leave blank): ")

    # print out choice for comparison purposes
    print("You chose {}".format(user_choice))
    print()
