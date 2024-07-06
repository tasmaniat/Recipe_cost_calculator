import pandas
from datetime import date

# dictionary to hold ingredient details
ingredient_dict = {
    "Ingredient": ["Buns", "Chicken", "Lettuce", "Mayo"],
    "Amount": ["6.0", "25.0 g", "2.0", "15.0 g"],
    "Purchased": ["6.0", "300.0g", "12.0", "3570.0g"],
    "Cost": [12.00, 15.0, 3.3, 6.2]

}
# Convert the dictionary to a pandas DataFrame
ingredient_frame = pandas.DataFrame(ingredient_dict)

# Calculate the cost per serving
sum_total = 36.50
serving_size = 6
total_cps = sum_total / serving_size

# Calculate total cost
total_cost = sum_total

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

# prints out data with heading
heading = "---- Ingredient Data ({}/{}/{}) ----\n".format(day, month, year)
filename = "Ingredient_{}_{}_{}".format(year, month, day)

# Change frame to string so that we can export it to file
ingredient_string = pandas.DataFrame.to_string(ingredient_frame)

total_heading = "\n****** Total Costs ******"
total_cost_txt = "CHICKEN SUB Costs: ${:.2f}".format(sum_total)
total_make_txt = "Total cost to make: ${:.2f}".format(total_cost_to_make)

serve_heading = "\n===== Serving Costs ====="
serve_per_cost_txt = "Cost Per serve: ${:.2f}".format(total_cps)
serve_total_txt = "Total cost per serve: ${:.2f}".format(total_cost_to_make / serving_size)

# create string for printing...
# total_cost_string = "\nPrice Total: ${}".format(total_cost)
# total_cost_to_make_string = "Total cost to make: ${}".format(total_cost_to_make)

# list holding content to print / write to file
to_write = [heading, ingredient_string, total_heading,
            total_cost_txt, total_make_txt, serve_heading,
            serve_per_cost_txt, serve_total_txt]

# print output
for item in to_write:
    print(item)
    print()

# write output to file
# create file to hold data (add.txt extension)
write_to = "{}.txt".format(filename)
text_file = open(write_to, "w+")

# heading
for item in to_write:
    text_file.write(item)
    text_file.write("\n")

# close file
text_file.close()
