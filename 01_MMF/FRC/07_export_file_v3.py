import pandas

# Frames and content for exports

variable_dict = {
    "Item": ["Muge", "Printing", "Packaging"],
    "Quantity": [300, 300, 50],
    "Price": [1, .5, .75]
}

fixed_dict = {
    "Item": ["Rent", "Artwork", "Advertising"],
    "Price": [25, 35, 10]
}

variable_frame = pandas.DataFrame(variable_dict)
fixed_frame = pandas.DataFrame(fixed_dict)


# Change frmaes to strings
variable_txt = pandas.DataFrame.to_string(variable_frame)
fixed_txt = pandas.DataFrame.to_string(fixed_frame)

product_name = "Custom Mugs"
profit_target = "$100.00"
required_sales = "$200.00"
recommended_price = "The recommended price is $5.00"


# list holding stuff to print / write to file
to_write = [product_name, variable_txt, fixed_txt, profit_target, required_sales, recommended_price]


# write to file...
# create file to hold data (add .txt extension)
file_name = "{}.txt".format(product_name)
text_file = open(file_name, "w+")

# Heading
for item in to_write:
    text_file.write(item)
    text_file.write("\n\n")

# text_file.write(variable_txt)

#

# close file
text_file.close()

# print stuff
for item in to_write:
    print(item)
    print()