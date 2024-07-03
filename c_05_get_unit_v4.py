# Asks the user to enter a number with a unit,
# then returns the value in its base unit (g or ml)
def get_number_and_unit(question):
    # units and their conversion factors
    units = {
        "mg": 0.001, "milligram": 0.001, "milligrams": 0.001,
        "g": 1, "gram": 1, "grams": 1,
        "kg": 1000, "kilogram": 1000, "kilograms": 1000,
        "ml": 1, "milliliter": 1, "milliliters": 1,
        "l": 1000, "liter": 1000, "liters": 1000,
        "kl": 1000000, "kiloliter": 1000000, "kiloliters": 1000000,
    }
    # base units for each unit
    base_units = {"mg": "g", "g": "g", "kg": "g", "ml": "ml", "l": "ml", "kl": "ml",
                  "milligram": "g", "gram": "g", "kilogram": "g", "milliliter": "ml", "liter": "ml", "kiloliter": "ml",
                  "milligrams": "g", "grams": "g", "kilograms": "g", "milliliters": "ml", "liters": "ml",
                  "kiloliters": "ml"}

    while True:
        response = input(question).strip().lower()
        # Check if the input is a number
        if response.replace('.', '', 1).isdigit():
            number = float(response)
            if number <= 0:
                print("Please enter a number more than 0")
                print()
                continue
            return f"{number}"
        # Check if the input ends with a unit
        for unit, conversion_factor in units.items():
            if response.endswith(unit):
                number_str = response[:-len(unit)].strip()
                try:
                    number = float(number_str)
                    if number <= 0:
                        continue
                    base_unit = base_units[unit]
                    return f"{number * conversion_factor} {base_unit}"
                except ValueError:
                    pass
        print("Please enter valid unit 'g,kg,mg,l'")
        print()


# main routine here
while True:
    user_input = get_number_and_unit("Amount of ingredient: ")
    if user_input == "xxx":
        break
    print("amount:", user_input)
    print()
