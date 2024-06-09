

# checks if the user input is valid and returns the number and unit
def get_number_and_unit(question):
    units = ["g", "gram", "grams",
             "kg", "kilogram", "kilograms",
             "mg", "milligram", "milligrams",
             "l", "litre", "litres"]

    while True:
        response = input(question).strip().lower()
        for unit in units:
            if response.endswith(unit):
                number_str = response[:-len(unit)].strip()
                try:
                    number = float(number_str)
                    if number > 0:
                        return number, unit
                    else:
                        print("\nPlease enter a positive number")
                except ValueError:
                    pass
        print("\nPlease enter valid unit 'g,kg,mg,l'")


while True:
    user_input = get_number_and_unit("Amount of ingredient: ")
    print("amount:", user_input)
    print()
