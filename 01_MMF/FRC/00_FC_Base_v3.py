import pandas

# *** Functions go here ***

# Checks that input is either a float or an
# interger that is more than zero. Take custom error message.
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


# Checks that user has entered yes / no to question
def yes_no(question):

    to_check = ["yes", "no"]

    valid = False
    while not valid:

        response = input (question).lower()

        for var_item in to_check:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item

        print("Please enter either yes or nno...\n")


# Checks that string response is not blank
def not_blank(question, error):

    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print("{}. \nPlease try again.\n".format(error))

        return response


# currency formating functions
def currency (x):
    return "${:.2f}".format(x)


# Gets expenses, returns list which has
# Gets expenses, returns list which has
# the data frame and sub total
def get_expenses(var_fixed):
    # St up dictoinaries and lists
   
    item_list = []
    quantity_list = []
    price_list = []  

    variable_dict = {
        "Item": item_list,
        "Quantity": quantity_list,
        "Price": price_list
    }

    # Loop to get component, quantity and price
    item_name = ""
    while item_name.lower() != "xxx":
        
        print()
        # get name, quantity and item
        item_name = not_blank("Item name:", "The component name can't be blank.")

        if item_name.lower() == "xxx":
            break

        if var_fixed == "variable":
            quantity = num_check("Quantity:", "The amount must be a whole number more than zero", int)
        
        
        else:
            quantity = 1

        price = num_check("How much for a single item? $", "The price must be a number<more than 0>", float)

        # add item, quantity and price lists
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)

    expense_frame = pandas.DataFrame(variable_dict)
    expense_frame = expense_frame.set_index('Item')

    # Calculate cost of each component
    expense_frame['Cost'] = expense_frame['Quantity'] * expense_frame['Price']

    # Find sub total
    Sub_total = expense_frame['Cost'].sum()

    # Currency Formating (use currrency function)
    add_dollars = ['Price', 'Cost']
    for item in add_dollars:
        expense_frame[item] =  expense_frame[item].apply(currency)

    return [expense_frame, Sub_total]


def expence_print(heading, frame, subtotal):
    print()
    print("**** {} Costs ****".format(heading))
    print(frame)
    print()
    print("{} Costs: ${:.2f}".format(heading,subtotal))
    return ""


# *** Main Routine goes here ***
# Get product name
product_name = not_blank("product name: ", "The product name can't be blank.")


# Get variable costs
variable_expenses = get_expenses("variable")
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]

print()
have_fixed = yes_no("Do you have fixed costs (y / n)? ")

print()
print("Please enter your variable costs below...")

if have_fixed == "yes":

    fixed_expenses = get_expenses("fixed")
    fixed_frame = fixed_expenses[0]
    fixed_sub = fixed_expenses[1]

else:
    fixed_sub = 0

# Find total costs

# Ask user for profit goal 

# calculate recommended price

# write data to file

# **** Printing Area ****

print()
print("**** Fund Raising - {} ****".format(product_name))
print()
expence_print("Variable", variable_frame, variable_sub)

if have_fixed == "yes":
    expence_print("Fixed", fixed_frame[['Cost']], fixed_sub)