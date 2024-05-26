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


# main routine goes here
# Loop for testing purposes
user_choice = ""
while user_choice != "xxx":
    get_int = num_check("Amount of ingredient: ",
                        "Please enter an amount more than 0 \n",
                        int)
    get_cost = num_check("Cost of ingredient:$",
                         "Please enter an amount more than 0 \n",
                         float)
    # print results
    print("You need: {}".format(get_int))
    print("It costs: {}".format(get_cost))
    print()
