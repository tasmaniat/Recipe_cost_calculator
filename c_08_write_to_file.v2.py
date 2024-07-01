import pandas
from datetime import date

# holds the ingredients data
ingredient_dict = {
    "Ingredient": ["Buns", "Chicken", "Lettuce", "Mayo"],
    "Amount": ["6.0", "25.0 g", "2.0", "15.0 g"],
    "Purchased": ["6.0", "300.0g", "12.0", "3570.0g"],
    "Cost": [12.00, 15.0, 3.3, 6.2]

}
ingredient_frame = pandas.DataFrame(ingredient_dict)

# Calculate the Price total
total_cost = ingredient_frame['Cost'].sum()

# Calculate cost to make
ingredient_frame['Cost to Make'] = (ingredient_frame['Cost'] / ingredient_frame['Purchased'].str.replace('g', '').astype(float)
                                    * ingredient_frame['Amount'].str.replace('g', '').astype(float)).round(2)

# Calculate the total cost to make
total_cost_to_make = ingredient_frame['Cost to Make'].sum()

# set index at end (before printing)
ingredient_frame = ingredient_frame.set_index('Ingredient')

# **** Get current date for heading and filename ****
# get today's date
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

heading = "---- Ingredient Data ({}/{}/{}) ----\n".format(day, month, year)
filename = "Ingredient_{}_{}_{}".format(year, month, day)

# Change frame to string so that we can export it to file
ingredient_string = pandas.DataFrame.to_string(ingredient_frame)

# create string for printing...
total_cost_string = "\nPrice Total: ${}".format(total_cost)
total_cost_to_make_string = "Total cost to make: ${}".format(total_cost_to_make)

# list holding content to print / write to file
to_write = [heading, ingredient_string, total_cost_string, total_cost_to_make_string]

# print output
for item in to_write:
    print(item)
    print()

# write output to file
# create file to hold data (add.txt extension)
write_to = "{}.txt".format(filename)
text_file = open(write_to, "w+")

for item in to_write:
    text_file.write(item)
    text_file.write("\n")

# close file
text_file.close()
