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
    # units allowed
    units = ["g", "gram", "grams",
             "kg", "kilogram", "kilograms",
             "mg", "milligram", "milligrams",
             "l", "litre", "litres"]

    while True:
        response = input(question).strip().lower()

        # checks if user enter a digit ( with no unit)
        if response.isdigit():
            return f"{response}.0"

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


# Gets user ingredient details and returns data in a dataframe
def get_ingredients():
    item_list = []
    amount_list = []
    purchased_list = []
    cost_list = []

    ingredient_name = ""
    while ingredient_name.lower() != "xxx":
        print()
        ingredient_name = not_blank("Ingredient name: ",
                                    "The ingredient name can't be blank.")

        if ingredient_name.lower() == "xxx":
            break
        amount = get_number_and_unit("Amount needed for recipe: ")
        purchased = get_number_and_unit("Purchased Amount: ")
        cost = num_check("Cost for ingredient:$",
                         "The cost must be a number more than 0", float)

        item_list.append(ingredient_name)
        amount_list.append(amount)
        purchased_list.append(purchased)
        cost_list.append(cost)

    ingredient_dict = {
        "Ingredient": item_list,
        "Amount": amount_list,
        "Purchased": purchased_list,
        "Cost": cost_list
    }
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
