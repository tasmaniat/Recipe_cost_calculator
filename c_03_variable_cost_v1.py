import pandas


# Function to check if the user input is an integer or a float, as required
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


# Function to gather the recipe ingredients and calculate the total cost and cost per serving
def get_ingredients():
    item_list = []
    quantity_list = []
    cost_list = []

    ingredient_name = ""
    while True:
        print()
        ingredient_name = not_blank("Ingredient name : ",
                                    "The ingredient name can't be blank.")
        if ingredient_name.lower() == "xxx":
            break

        amount_needed = num_check("Amount needed : ",
                                  "The amount must be a number more than zero")

        cost = num_check("Cost for the specified amount ($): ",
                         "The cost must be a number more than 0")

        item_list.append(ingredient_name)
        quantity_list.append(amount_needed)
        cost_list.append(cost)

    ingredient_dict = {
        "Ingredient": item_list,
        "Amount needed": quantity_list,
        "Cost": cost_list
    }

    ingredient_frame = pandas.DataFrame(ingredient_dict)
    ingredient_frame = ingredient_frame.set_index('Ingredient')

    # Calculate total cost
    total_cost = ingredient_frame['Cost'].sum()

    return [ingredient_frame, total_cost]


# Main routine
# recipe_name = not_blank("Recipe name: ", "The recipe name can't be blank.")
# serving_size = num_check("Serving size: ", "The serving size must be an integer more than zero", int)

ingredient_expenses = get_ingredients()
ingredient_frame = ingredient_expenses[0]
total_cost = ingredient_expenses[1]
# cost_per_serving = total_cost / serving_size

# Printing the results
print()
# print(f"Recipe: {recipe_name}")
print(ingredient_frame)
print()
print(f"Total cost: {currency(total_cost)}")
# print(f"Cost per serving (for {serving_size} servings): {currency(cost_per_serving)}")
