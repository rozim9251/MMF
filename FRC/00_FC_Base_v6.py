import pandas
import math



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


def expense_print(heading, frame, subtotal):
    print()
    print("**** {} Costs ****".format(heading))
    print(frame)
    print()
    print("{} Costs: ${:.2f}".format(heading,subtotal))
    return ""


def profit_goal(total_costs):

    # Initialise variables and error message
    error = "Please enter a valid profit goal\n"

    valid = False
    while not valid:

        # ask for profit goal...
        response = input("What is your profit goal (eg $500 or 50%) ")

        # check if first character is $...
        if response[0] == "$":
            profit_type = "$"
            # Get amount(everything after $)
            amount = response[1:]


        # check if last character is %
        elif response [-1] == "%":
            profit_type = "%"
            # Get amount (everything before the %)
            amount = response[:-1]

        else:
            # Set response to amount for now
            profit_type = "unknown"
            amount = response

        try:
            # check amount is a number more than zero...
            amount = float(amount)
            if amount <= 0:
                print(error)
                continue
        
        except ValueError:
            print(error)
            continue


        if profit_type == "unknown" and amount  >= 100:
            dollar_type = yes_no("Do you mean ${:.2f}. ie {:.2f} dollars? , y / n".format(amount, amount))


            # Set profit type based on user answer above
            if dollar_type == "yes":
                profit_type = "$"
            else:
                profit_type = "%"

        
        elif profit_type == "unknown" and amount < 100:
            percent_type = yes_no("Do you mean {}%? , y / n".format(amount))
            if percent_type == "yes":
                profit_type = "%"
            else:
                profit_type = "$"

        # return profit goal to main routine
        if profit_type == "$":
            return amount
        else:
            goal = (amount / 100) * total_costs
            return goal


def round_up(amount, round_to):
    return int(math.ceil(amount / round_to)) * round_to


# *** Main Routine goes here ***
# Get product name
product_name = not_blank("product name: ", "The product name can't be blank.")
how_many = num_check("How many items will you be producing? ",  "The number of items must be a whole number mre than zero",int)

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
    fixed_frame = ""
    fixed_sub = 0

# work out total costs and profits target
all_costs = variable_sub + fixed_sub
profit_target = profit_goal(all_costs)

# Calculate total sales needed to reach goal
sales_needed = all_costs + profit_target

# Ask user for rounding 
round_to = num_check("Round to nearest...? $", "Please enter an integer that is more than 0", int)

# calculate recommended price
selling_price =  sales_needed / how_many
print("Selling Price (unrounded): ${:.2f}".format(selling_price))

recommended_price = round_up(selling_price, round_to)

# change content to strings for writing...

# Change frmaes to strings

product_name_txt = "***** {} ******".format(product_name)

variable_txt = pandas.DataFrame.to_string(variable_frame)

if have_fixed == "yes":
    fixed_txt = pandas.DataFrame.to_string(fixed_frame)
else:
    fixed_txt = "There are no fixed costs"

profit_target_txt = "Profit  Target: ${:.2f}".format(profit_target)
sales_needed_txt = "Sales Needed: ${:.2f}".format(sales_needed)
recommended_price_txt = "Recommended Price: ${:.2f}".format(recommended_price)

# list holding stuff to print / write to file
to_write = [product_name_txt, "\n----  Variable Costs -----", variable_txt, "\n---- Fixed Costs ----", fixed_txt, "\n---- Sales Advice / Calculations  ----", profit_target_txt, sales_needed_txt, recommended_price_txt]

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
