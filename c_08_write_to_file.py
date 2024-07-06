import pandas

# Frames and content for export
ingredient_dict = {
    "Ingredient": ["Buns", "Chicken", "Lettuce", "Mayo"],
    "Amount": ["6.0", "25.0 g", "2.0", "15.0 g"],
    "Purchased": ["6.0", "300.0g", "12.0", "3570.0g"],
    "Cost": [12.00, 15.0, 3.3, 6.2]
}
# Convert the dictionary to a pandas DataFrame
ingredient_frame = pandas.DataFrame(ingredient_dict)

# change frame to string
ingredient_txt = pandas.DataFrame.to_string(ingredient_frame)

# define name of product and total cost
product_name = "Chicken Sub"
tally_cost = "Total cost: $36.50"

# list holding stuff to print / write to file
to_write = [product_name, ingredient_txt, tally_cost]


# write to file...
# create file to hold data (add .txt extension)
file_name = "{}.txt".format(product_name)
text_file = open(file_name, "w+")

# heading
for item in to_write:
    text_file.write(item)
    text_file.write("\n")

# close file
text_file.close()

# Print Stuff
for item in to_write:
    print(item)
    print()
