import pandas


# checks users enter an integer to a given question
def num_check(question, error, num_type):
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


# checks that user response is not blank
def not_blank(question, error):
    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print("{}. \nPlease try again \n".format(error))
            continue

        return response


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# Gets expenses, returns list which has
# the data frame and sub_total
def get_expenses(var_fixed):
    #  set up dictionaries and lists

    item_list = []
    quantity_list = []
    price_list = []

    variable_dict = {
        "List ingredient": item_list,
        "Amount of ingredient": quantity_list,
        "Cost of ingredient": price_list
    }

    # loop to get component, quantity adn price
    item_name = ""
    while item_name.lower() != "xxx":

        print()
        # get name, quantity and item
        item_name = not_blank("list ingredient:  ",
                              "Can't be blank")

        if item_name.lower() == "xxx":
            break

        quantity = num_check("The amount of ingredient: ",
                             "The amount must be a whole number"
                             "more than zero",
                             int)

        price = num_check("Cost of ingredient: ",
                          "The price must be a number <more "
                          "than 0>", float)

        # add item, quantity and price to lists
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)

    expense_frame = pandas.DataFrame(variable_dict)
    expense_frame = expense_frame.set_index('Ingredient')

    # Calculate cost of each component
    expense_frame['Cost'] = expense_frame['Quantity'] * expense_frame['Price']

    # Find sub_total
    sub_total = expense_frame['Cost'].sum()

    # Currency Formatting (uses currency function)
    add_dollars = ['Price', 'Cost']
    for item in add_dollars:
        expense_frame[item] = expense_frame[item].apply(currency)

    return [expense_frame, sub_total]


# ******* main routine goes here *******

# Get user data
unit_list = ["g", "kg", "mg", "L", ""]

product_name = not_blank("Recipe name: ", "The Recipe name can't be blank. ")

variable_expenses = get_expenses("variable")
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]

# ***** Printing Area *****

print()
print(variable_frame)
print()

print("Fixed Costs: ${:.2f}".format(variable_sub))