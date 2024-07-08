import pandas
from datetime import date


# displays # a simple statement to welcome
# the user into the program and tells a little about it
def generate_welcome_statement():
    print()
    print(" -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
    print(" ★  WELCOME TO RECIPE COST CALCULATOR  ★")
    print(" -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
    print("This program will calculate the costs for the recipe")
    print()


# function to display instructions
def show_instructions():
    print('''
*--*--*--*--*--*--* INSTRUCTIONS *--*--*--*--*--*--*
    1. enter recipe name & serving size.
    
    2. For each ingredient, enter...
     - Ingredient (required, cannot be blank)
     - Quantity needed for recipe (e.g. 15g)
     - Quantity of purchased ingredient (e.g. 1kg)
     - Cost of the ingredient 
     
        Allowed units: g, kg, mg, ml, l, kl 
        (or leave blank if not applicable)
 
    A data table will be displayed and its costs
    This information will be saved to a text file 
     
     3. enter new serving size (optional)
     4. calculate for another recipe (optional)
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
   ''')


# Checks that user has entered yes / no to a question
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("please answer yes / no")


# checks if input is either a float or an
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


def expense_string(heading, frame, subtotal):
    expense_heading = "**** Recipe: {} ****".format(heading)
    expense_frame_txt = pandas.DataFrame.to_string(frame)
    expense_sub_txt = "{} Costs: ${:.2f}".format(heading, subtotal)

    return expense_heading, expense_frame_txt, expense_sub_txt


# Gets user to enter a number with a unit,
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
        # checks if the input is a number without unit
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
                # takes the number part of the input
                number_str = response[:-len(unit)].strip()
                try:
                    number = float(number_str)
                    if number <= 0:
                        continue
                    # gets base unit for the input unit
                    base_unit = base_units[unit]
                    return f"{number * conversion_factor} {base_unit}"
                except ValueError:
                    pass
        print("Please enter valid amount /unit 'g,kg,mg,ml,kl,l'")
        print()


# Gets user ingredient details and returns data in a dataframe
def get_ingredients():
    # stores ingredient data
    item_list = []
    amount_list = []
    purchased_list = []
    cost_list = []
    cost_to_make_list = []

    # Loop until user enters "xxx" to stop
    ingredient_name = ""
    while ingredient_name.lower() != "xxx":
        print()
        # ensures it not blank
        ingredient_name = not_blank("Ingredient name: ",
                                    "The ingredient name can't be blank.")

        if ingredient_name.lower() == "xxx":
            break
        # Get amount needed, purchased amount, and cost
        amount = get_number_and_unit("Amount needed for recipe: ")
        purchased = get_number_and_unit("Purchased Amount: ")
        cost = num_check("Cost for ingredient:$",
                         "The cost must be a number more than 0", float)

        # extracts the number out of the amount and purchased string
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

    # Calculate total cost and total cost to make
    total_sum = dataframe['Cost'].sum()
    total_cost_to_make = dataframe['Cost to Make'].sum()

    # Currency Formatting (uses currency function)
    add_dollars = ['Cost to Make', 'Cost']
    for item in add_dollars:
        dataframe[item] = dataframe[item].apply(currency)

    return [dataframe, total_sum, total_cost_to_make]


# calculate the cost per serving based
# on the total cost and serving size.
def cost_per_serving(cost, serving_size):
    if serving_size <= 0:
        return "Please enter a valid number"
    else:
        cost_per_serve = cost / serving_size
        return cost_per_serve


# ******* main routine goes here *******
# a simple statement to welcome the user into the program
generate_welcome_statement()

# asks user if used before
played_before = yes_no("Have you used this program before? ")

# no then show instructions
if played_before == "no":
    show_instructions()

while True:
    print()
    # gets users recipe name and serving size
    print("***** Program Launched! *****")
    recipe_name = not_blank("Recipe name: ", "The recipe name can't be blank")
    serving_size = num_check("Serving size: ", "The serving size must be an integer more than zero", int)

    print()
    print("Please enter your recipe information below...")
    print("Enter 'xxx' for the item name when done.")

    # variable cost / get ingredients details
    ingredient_expenses = get_ingredients()
    frame_data = ingredient_expenses[0]
    sum_total = ingredient_expenses[1]
    total_cost_to_make = ingredient_expenses[2]

    # Calculate the cost per serving
    total_cps = cost_per_serving(sum_total, serving_size)

    # Calculate total cost
    total_cost = sum_total

    # **** Get current date for heading and filename ****
    # get today's date
    today = date.today()

    # Get day, month and year as individual strings
    day = today.strftime("%d")
    month = today.strftime("%m")
    year = today.strftime("%Y")

    # ***** Printing Area *****
    print()
    heading = "***** Ingredient Data ({}/{}/{}) *****\n".format(day, month, year)
    filename = "Ingredient_{}_{}_{}".format(year, month, day)

    # Change frame to string so that we can export it to file
    ingredient_string = pandas.DataFrame.to_string(frame_data)

    ingredient_strings = expense_string(recipe_name, frame_data, sum_total)
    ingredient_heading = ingredient_strings[0]
    ingredient_frame_txt = ingredient_strings[1]

    total_heading = "\n****** Total Costs ******"
    total_cost_txt = f"{recipe_name} Costs: ${sum_total:.2f}"
    total_make_txt = f"Total cost to make: ${total_cost_to_make:.2f}"

    serve_heading = "\n===== Serving Costs ====="
    serve_per_cost_txt = f"Cost Per serve: ${total_cps:.2f}"
    serve_total_txt = f"Total cost per serve {total_cost_to_make / serving_size:.2f}"

    to_write = [heading, ingredient_heading, ingredient_frame_txt,
                total_heading, total_cost_txt, total_make_txt,
                serve_heading, serve_per_cost_txt, serve_total_txt]

    # write to file...
    # create file to hold data (add.txt extension)
    file_name = "{}.txt".format(filename)
    text_file = open(file_name, "w+")

    # heading
    for item in to_write:
        text_file.write(item)
        text_file.write("\n")

    # close file
    text_file.close()

    # Print Stuff
    for item in to_write:
        print(item)
        print()

    # ask user if they want to calculate cost per serving for different serving size
    recalculate_cps = yes_no("Do you want to recalculate for different serving size?  ")
    if recalculate_cps == "yes":
        new_serving_size = num_check("Enter the new serving size: ",
                                     "The serving size must be an integer more than zero", int)
        new_total_cps = cost_per_serving(sum_total, new_serving_size)
        print()
        print(f"Cost per serving for {new_serving_size} servings: ${new_total_cps:.2f}")
        print()

    # ask user if they want to calculate another recipe
    calculate_another = yes_no("Do you want to calculate another recipe? ")
    print()

    if calculate_another == "no":
        print("Thank you for using this program")
        break
