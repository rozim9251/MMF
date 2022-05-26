import pandas


def num_check(question, error, num_type):

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


def not_blank(question, error):

    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print("{}. \nPlease try again.\n".format(error))

        return response


# Currency formating function
def currency (x):
    return "${:.2f}".format(x)

# *** Main routine starts here ***

# Set up dictionaries and lists

item_list = []
quantity_list = []
price_list = []  

variable_dict = {
    "item": item_list,
    "Quantity": quantity_list,
    "price": price_list
}

# Get user data
product_name = not_blank("product name: ", "The product name can't be blank.")


# Loop to get component, quantity and price
item_name = ""
while item_name.lower() != "xxx":

    print()
    # get name, quantity and item
    item_name = not_blank("Item name:", "The component name can't be blank.")

    if item_name.lower() == "xxx":
        break


    quantity = num_check("Quantity:", "The amount must be a whole number more than zero", int)
    price = num_check("How much for a single item? $", "The price must be a number<more than 0>", float)

    # add item , quantity and price lists
    item_list.append(item_name)
    quantity_list.append(quantity)
    price_list.append(price)


variable_frame = pandas.DataFrame(variable_dict)
variable_frame = variable_frame.set_index('Item')


# Calculate cost of each component
variable_frame['cost'] = variable_frame['Quantity']\
    * variable_frame['price']


# Find sub total
variable_sub = variable_frame['cost'].sum()

# Currency Formating (use currrency function)
add_dollars = ['Price', 'Cost']
for item in add_dollars:
    variable_frame[item] = variable_frame[item].apply(currency)


# *** Printing Area ***

print(variable_frame)

print()

print("Variable Costs: ${:.2f}".format(variable_sub))