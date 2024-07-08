# Function go here...
# check user answers yes / no to a question
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("please answer yes / no")


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


# Main Routine goes here...
played_before = yes_no("Have you used this program before? ")

if played_before == "no":
    show_instructions()
print()
print("Please press <enter> to begin...")