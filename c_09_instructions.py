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


# Display instructions
def show_instructions():
    print('''\n
   *--*--*--*--*--*--* INSTRUCTIONS *--*--*--*--*--*--*
        This calculates the cost of the recipe 
      based on the ingredient and their quantities
         
         To get started, follow these steps:
          
      1. Enter the recipe name & serving size.
      2. For each ingredient, enter the following..
       - Ingredient name (required, cannot be blank)
       - Quantity needed for recipe (e.g. 15g)
       - Quantity of purchased ingredient (e.g. 1kg)
       - Cost of the ingredient 
        
   Units can be blank if not applicable (e.g. 1, 2, etc)
             
       The calculator will display a table with 
    the recipe details, including the total cost, cost 
       per serving, and cost to make the recipe. 
         
   This information will also be saved to a text file 
   *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*''')


# Main Routine goes here...
played_before = yes_no("Have you used this program before? ")

if played_before == "no":
    show_instructions()
print()
print("Please press <enter> to begin...")