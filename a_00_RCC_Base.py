import pandas


# Checks that user has entered yes / no to question
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("please answer yes / no")


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


# Asks the user to enter a number with a unit,
# then returns the value in its base unit (g or ml)
def get_number_and_unit(question):
    units = {
        "mg": 0.001, "milligrams": 0.001,
        "g": 1, "grams": 1,
        "kg": 1000, "kilograms": 1000,
        "ml": 1, "milliliters": 1,
        "l": 1000, "liters": 1000,
        "kl": 1000000, "kiloliters": 1000000,
    }

    base_units = {"mg": "g", "g": "g", "kg": "g", "ml": "ml", "l": "ml", "kl": "ml",
                  "milligrams": "g", "grams": "g", "kilograms": "g", "milliliters": "ml", "liters": "ml",
                  "kiloliters": "ml"}

    while True:
        response = input(question).strip().lower()

        if response.replace('.', '', 1).isdigit():
            number = float(response)
            if number <= 0:
                print("Please enter a number more than 0")
                print()
                continue
            return f"{number}"

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


# Display instructions
def show_instructions():
    print('''
    *-*-*-*-*-*-* INSTRUCTIONS *-*-*-*-*-*-*
          - enter the recipe name 
          - enter the serving size
    
            There will be a series of            
          question's for each ingredient         
    
     enter the ingredient name (can't be blank)
     enter the amount & unit for ingredient
     enter the amount & unit for purchased packet
      - - - - -(the units can be blank)- - - - - 
           enter the cost for ingredient 
    
      When you have entered all the ingredients  
         to the recipe, press 'xxx' to quit.     
    
     A datatable will then be printed with all the 
     recipe details like the total cost, cost per 
      serve and will calculate the cost to make 
    
    This information will also be automatically written to
    a text file.
    *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*''')


def expense_string(heading, frame, subtotal):
    expense_heading = "**** {} Costs ****".format(heading)
    expense_frame_txt = pandas.DataFrame.to_string(frame)
    expense_sub_txt = "\n{} Costs: ${:.2f}".format(heading, subtotal)

    return expense_heading, expense_frame_txt, expense_sub_txt


# calculate the cost per serving based on the total cost and serving size.
def cost_per_serving(cost, serving_size):
    if serving_size <= 0:
        return "Please enter a valid number"
    else:
        cost_per_serve = cost / serving_size
        return cost_per_serve


# ******* main routine goes here *******
print()
played_before = yes_no("Have you used this program before? ")

if played_before == "no":
    show_instructions()
print("***** Program Launched! *****")

# get users recipe name and serving size
recipe_name = not_blank("Recipe name: ", "The recipe name can't be blank")
serving_size = num_check("Serving size: ", "The serving size must be an integer more than zero")

# variable cost / get ingredients
ingredient_expenses = get_ingredients()
frame_data = ingredient_expenses[0]
sum_total = ingredient_expenses[1]

# calculate total cost per serving
total_cps = cost_per_serving(sum_total, serving_size)

# ***** Printing Area *****

ingredient_strings = expense_string("Ingredient", frame_data, sum_total)
ingredient_heading = ingredient_strings[0]
ingredient_frame_txt = ingredient_strings[1]
ingredient_sub_txt = ingredient_strings[2]

print(ingredient_heading)
print(ingredient_frame_txt)
print()
print("Total: ${:.2f}".format(sum_total))
print("Cost per serving: ${:.2f} ".format(total_cps))
