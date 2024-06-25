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
            number = float(response)
            if number <= 0:
                print("Please enter a number more than 0")
                print()
                continue
            return f"{number}.0"

        for unit in units:
            if response.endswith(unit):
                number_str = response[:-len(unit)].strip()
                try:
                    number = float(number_str)
                    if number <= 0:
                        continue
                    return f"{number} {unit}"
                except ValueError:
                    pass
        print("Please enter valid unit 'g,kg,mg,l'")
        print()


# main routine goes here

while True:
    user_input = get_number_and_unit("Amount of ingredient: ")
    if user_input == "xxx":
        break
    print("amount:", user_input)
    print()
