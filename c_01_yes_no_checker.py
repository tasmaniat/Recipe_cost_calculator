# Function go here...
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


# Main Routine goes here ...
# loop for testing purposes
user_choice = ""
while user_choice != "xxx":
    # Main Routine goes here ...
    show_instructions = yes_no("Do you want to see instructions? ")
    print("you chose {}".format(show_instructions))

    # Determine what to do based on the response
    if show_instructions == "yes":
        print("Program continues.")
        print()
    else:
        print("display instructions")
        print()
