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
Fixed_frame = pandas.DataFrame(fixed_dict)

product_name = "Custom Mugs"
profit_target = "$100"
required_sales = "$200"
recommended_price = "$5.00"

print(variable_frame)

# Change dataframe to string (so it can written to a txt file)
variable_txt = pandas.DataFrame.to_string(variable_frame)

# write to file...
# create file to hold data (add .txt extension)
file_name = "{}.txt".format(product_name)
text_file = open(file_name, "w+")

# Heading
text_file.write("**** Fund Raising - {} ****\n\n".format(product_name))

text_file.write(variable_txt)

#

# close file
text_file.close()