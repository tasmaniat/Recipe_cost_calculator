# functions goes here

# Function to ensure the user input is not blank
def not_blank(question, error):
    valid = False
    while not valid:
        response = input(question)
        if response == "":
            print("{}. \nPlease try again \n".format(error))
            continue
        return response


# main routine goes here
while True:
    print()
    name = not_blank("Ingredient name (or 'xxx' to quit) ")
    if name == "xxx":
        break

print("We are done")
