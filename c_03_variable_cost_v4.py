import pandas


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


# checks if user enters a number more than 0
# with unit, then returns it as a string
def get_number_and_unit(question):
    # units and their conversion factors
    units = {
        "mg": 0.001, "milligrams": 0.001,
        "g": 1, "grams": 1,
        "kg": 1000, "kilograms": 1000,
        "ml": 1, "milliliters": 1,
        "l": 1000, "liters": 1000,
        "kl": 1000000, "kiloliters": 1000000,
    }
    # base units for each unit
    base_units = {"mg": "g", "g": "g", "kg": "g", "ml": "ml", "l": "ml", "kl": "ml",
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


# Gets user ingredient details and returns data in a dataframe
def get_ingredients():
    item_list = []
    amount_list = []
    purchased_list = []
    cost_list = []
    cost_to_make_list = []

    # Loop until user enters "xxx" to stop
    ingredient_name = ""
    while ingredient_name.lower() != "xxx":
        print()
        ingredient_name = not_blank("Ingredient name: ",
                                    "The ingredient name can't be blank.")

        if ingredient_name.lower() == "xxx":
            break
        # Get amount needed, purchased amount, and cost
        amount = get_number_and_unit("Amount needed for recipe: ")
        purchased = get_number_and_unit("Purchased Amount: ")
        cost = num_check("Cost for ingredient:$",
                         "The cost must be a number more than 0", float)

        amount_value = float(amount.split()[0])
        purchased_value = float(purchased.split()[0])

        # Calculate cost to make ingredient
        cost_to_make = round((amount_value / purchased_value) * cost, 2)

        # Add data to lists
        item_list.append(ingredient_name)
        amount_list.append(amount)
        purchased_list.append(purchased)
        cost_list.append(cost)
        cost_to_make_list.append(cost_to_make)

    # Create a dictionary from the lists
    ingredient_dict = {
        "Ingredient": item_list,
        "Amount": amount_list,
        "Purchased": purchased_list,
        "Cost": cost_list,
        "Cost to Make": cost_to_make_list
    }
    # Convert dictionary to a pandas DataFrame
    dataframe = pandas.DataFrame(ingredient_dict)
    dataframe = dataframe.set_index('Ingredient')

    # Calculate total cost
    total_sum = dataframe['Cost'].sum()
    total_cost_to_make = dataframe['Cost to Make'].sum()

    return [dataframe, total_sum, total_cost_to_make]


# Main routine

ingredient_expenses = get_ingredients()
frame_data = ingredient_expenses[0]
sum_total = ingredient_expenses[1]
sum_cost_to_make = ingredient_expenses[2]

# Printing the results
print()
print(frame_data)
print()
print(f"Total cost: {currency(sum_total)}")
print(f"Total: {currency(sum_cost_to_make)}")
