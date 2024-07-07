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


# Function to get measurement unit from the user
def get_unit(question):
    # Allowed units
    units = ["", "g", "gram", "grams", "kg", "kilogram",
             "kilograms", "mg", "milligram", "milligrams",
             "l", "liter", "liters"]

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


# Function to gather the recipe ingredients, amounts, units, and costs
def get_ingredients():
    # stores ingredient data
    item_list = []
    amount_list = []
    unit_list = []
    purchased_list = []
    purchased_unit_list = []
    cost_list = []

    # Loop until user enters "xxx" to stop
    ingredient_name = ""
    while ingredient_name.lower() != "xxx":
        print()
        # enter ingredient name , ensures that it is not blank
        ingredient_name = not_blank("Ingredient name: ",
                                    "The ingredient name can't be blank.")
        if ingredient_name.lower() == "xxx":
            break

        # enter amount of ingredient, check if more than 0
        amount = num_check("Amount (without unit): ",
                           "Please enter the 'number only' greater than 0")

        unit = get_unit("Amount unit (blank for none): ")

        # enter purchased amount of ingredient, check if more than 0
        purchased = num_check("Purchased Amount: ",
                              "Please enter the 'number only' greater than 0",)

        purchased_unit = get_unit("Purchased Unit (blank for none): ")

        # enter cost of ingredient
        cost = num_check("Cost for ingredient:$ ",
                         "Please enter a number more than 0", float)

        # Add data to lists
        item_list.append(ingredient_name)
        amount_list.append(amount)
        unit_list.append(unit)
        purchased_list.append(purchased)
        purchased_unit_list.append(purchased_unit)
        cost_list.append(cost)

    # Create a dictionary from the lists
    ingredient_dict = {
        "Ingredient": item_list,
        "Amount": amount_list,
        "Unit": unit_list,
        "Purchased": purchased_list,
        "Purchased unit": purchased_unit_list,
        "Cost": cost_list
    }

    # Convert dictionary to a pandas DataFrame
    dataframe = pandas.DataFrame(ingredient_dict)
    dataframe = dataframe.set_index('Ingredient')

    # Calculate total cost
    total_sum = dataframe['Cost'].sum()

    return [dataframe, total_sum]


# Main routine

ingredient_expenses = get_ingredients()
frame_data = ingredient_expenses[0]
sum_total = ingredient_expenses[1]

# Printing the results
print()
print(frame_data)
print()
print(f"Total cost: {currency(sum_total)}")
