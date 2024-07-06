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


# calculate the cost per serving based
# on the total cost and serving size.
def cost_per_serving(cost, serving_size):
    if serving_size <= 0:
        return "Please enter a valid number"
    else:
        cost_per_serve = cost / serving_size
        return cost_per_serve


# main routine goes here
# Loop for testing purposes
user_choice = ""
while True:
    print()
    user_choice = num_check("cost of ingredient: $", "please enter a number more than 0", float)
    serving_size = num_check("the serving size: ", "Please enter a valid number", int)

    total_cps = cost_per_serving(user_choice, serving_size)
    print(f"Cost per serving: ${total_cps:.2f}")

    # ask user if they want to calculate cost per serving for different serving size
    print()
    recalculate_cps = yes_no("Do you want to recalculate for different serving size?  ")

    if recalculate_cps == "yes":
        new_serving_size = num_check("Enter the new serving size: ",
                                     "The serving size must be an integer more than zero", int)
        new_total_cps = cost_per_serving(user_choice, new_serving_size)
        print()
        print(f"Cost per serving for {new_serving_size} servings: ${new_total_cps:.2f}")
        print()