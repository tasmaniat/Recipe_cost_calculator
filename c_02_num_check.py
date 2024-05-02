# checks that input is a positive number or
# integer that is more than zero. Takes in custom error message
def num_check(question, error):
    valid = False
    while not valid:
        try:
            response = float(input(question))
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
    get_int = num_check("How many do you need? ",
                        "Please enter an amount more than 0\n",
                        )
    get_cost = num_check("how much does it cost? $",
                         "Please enter a number more than 0\n",
                         )

    print("You need: {}".format(get_int))
    print("It costs: {}".format(get_cost))
    print()
