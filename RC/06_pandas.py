# imports...
import pandas


# Functions go here

# checks that string is not blank
def not_blank(question, error_messasge):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print(error_messasge)


# Checks that input is either a float or an
# interger that is more than zero. Take custom error message.
def num_check(question, error):
    valid = False
    while not valid:

        try:
            response = float(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# checks if items are in list
def choice_checker(question, valid_list, error):
    valid = False
    while not valid:

        # Ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        # iterates through list and if response is an item
        # in the list ( or the first letter of an item), the
        # full item name is returned

        try:
            for item in valid_list:
                if response == item[0] or response == item:
                    print()
                    return item

            # output error if item is not in list
            print(error)
            print()

        except IndexError:
            return response


# ***** Main Routine starts here *****

total = 0
ingredient_list = ""
ingredient_order = []

# Initialise lists (to make a data-frame in due course)
Ingredient = []
Quantity = []
Units = []
Package_amount = []
Price = []
Cost_to_make = []
Price_per_serve = []
Serving = []

# unit list
unit_list = ["kilograms", "kg", "grams", "g", "liters", "l", "millilitres", "ml", ""]

# Data for dictionary
ingredient_data_dict = {
    'Ingredient': Ingredient,
    'Amount needed': Quantity,
    'Unit':Units,
    'Package amount': Package_amount,
    'Price': Price,
    'Cost to make':Cost_to_make,
}


# start of loop
# initiate loop so that it runs at least once
while ingredient_list != "xxx":

    # Get name (can't be blank)
    ingredient_name = not_blank("Enter Ingredient Name: ", "Sorry, this can't be blank")

    if ingredient_name == "xxx":
        break
    else:
        Ingredient.append(ingredient_name)

    # asks for the quantity, if quantity = 0 puts error message than asks question again
    quantity = num_check("How much do you need? ", "Sorry, the amount must be a number or a number more than 0")
    Quantity.append(quantity)


    # asks user for package amount
    package_amount = num_check("Enter Package amount: ", "Sorry, the amount must be a number or a number more than 0")
    Package_amount.append(package_amount)

    # asks user for the cost of ingredient
    price = num_check("Enter the price: $", "Sorry, the amount must be a number more than 0")
    Price.append(price)

    # asks for the unit, if not in list asks again
    unit = choice_checker("Enter the unit: ", unit_list, "Invalid response, try again")
    Units.append(unit)

    # calculates price over package_amount then times it by quantity
    cost_to_make = (price / package_amount) * quantity
    Cost_to_make.append(cost_to_make)

    # puts ingredient costs in to a total
    total += cost_to_make

    print("{:.2f}".format(cost_to_make))



# for item in ingredient_list:
#     item.append(0)


print('Ingredient', Ingredient)
print('Amount needed', Quantity)
print('Unit', Units)
print('Package amount', Package_amount)
print('Price', Price)
print('Cost to make', Cost_to_make)



# Create a dataframe and set index to name column
ingredient_frame = pandas.DataFrame(ingredient_data_dict)
ingredient_frame = ingredient_frame.set_index('Ingredient')

# asks user how many people they will be serving
per_serve = num_check("How many people will you be serving? ", "Sorry, the amount must be a number more than 0")


# Devides the total by how many people they will be serving
price_per_serve = total / per_serve
Price_per_serve.append(price_per_serve)

# prints price_per_serve into two decimal places
print("Total: {:.2f}".format(total))
print("Price per serve: {:.2f}".format(price_per_serve))


