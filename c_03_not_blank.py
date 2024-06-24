# functions goes here

# checks that user response is not blank
def not_blank(question):
    while True:
        response = input(question)

        if response == "":
            print("Sorry this can't be black. Please try again")
        else:
            return response


# main routine goes here
while True:
    print()
    name = not_blank("Ingredient name (or 'xxx' to quit) ")
    if name == "xxx":
        break

print("We are done")
