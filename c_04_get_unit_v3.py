

# checks if the user input is valid and returns the number and unit
def get_number_and_unit(question):
    # units allowed
    units = ["g", "gram", "grams",
             "kg", "kilogram", "kilograms",
             "mg", "milligram", "milligrams",
             "l", "litre", "litres"]

    while True:
        response = input(question).strip().lower()

        # checks if user enter a digit ( with no unit)
        if response.isdigit():
            return float(response), ""

        for unit in units:
            if response.endswith(unit):
                number_str = response[:-len(unit)].strip()
                try:
                    number = float(number_str)
                    if number > 0:
                        return f"{number} {unit}"
                    else:
                        print("\nPlease enter a positive number")
                except ValueError:
                    pass
        print("\nPlease enter valid unit 'g,kg,mg,l'")


# main routine goes here

while True:
    user_input = get_number_and_unit("Amount of ingredient: ")
    if user_input == "xxx":
        break
    print("amount:", user_input)
    print()
