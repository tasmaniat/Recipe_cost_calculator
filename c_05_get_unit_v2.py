# Input for recipe ingredient amount
# Checks user input is valid & returns
# full unit name /  error message
def get_unit(input_str):
    # units allowed (shorthand & full names)
    units = {
        'g': 'grams', 'gram': 'grams', 'grams': 'grams',
        'kg': 'kilograms', 'kilogram': 'kilograms', 'kilograms': 'kilograms',
        'mg': 'milligrams', 'milligram': 'milligrams', 'milligrams': 'milligrams',
        'l': 'litres', 'liter': 'litres', 'liters': 'litres',
        'ml': 'millilitres', 'millilitre': 'millilitres', 'millilitres': 'millilitres'
    }
    i = 0
    while i < len(input_str) and (input_str[i].isdigit() or input_str[i] == '.'):
        i += 1
    # checks if user enters both amount and unit
    amount_str = input_str[:i]
    unit_str = input_str[i:].strip().lower()

    if not amount_str or not unit_str:
        return "Please enter the amount and unit"

    # Turns to float and check if is more than 0
    try:
        amount = float(amount_str)
        if amount <= 0:
            return "Please enter a number more than 0"
    except ValueError:
        return "Please enter a number"

    # Checks if unit is valid
    if unit_str in units:
        return f"{amount} {units[unit_str]}"
    else:
        return "Please enter one of the following\n" \
               "units: g, kg, mg, l, ml"


# Main routine (loop for testing purposes)

while True:
    print()
    # asks user for amount for recipe (xxx to quit)
    user_input = input("Amount needed for recipe: ").strip()
    if user_input.lower() == 'xxx':

        break
    print(get_unit(user_input))


