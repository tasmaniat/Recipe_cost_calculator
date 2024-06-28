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


# calculate the cost per serving based on the total cost and serving size.
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
