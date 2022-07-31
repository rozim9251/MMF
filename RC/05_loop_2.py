# imports...
import pandas
# Functions go here

# checks that string is not blank
def not_blank (question, error_messasge) :
    valid = False

    while not valid:
        response = input (question)

        if response !="":
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
# unit list
unit_list = ["kilograms","kg", "grams", "g", "liters", "l", "millilitres", "ml", ""]

total = 0
ingredient_name = ""
ingredient_order = []

# start of loop
# initiate loop so that it runs at least once
while ingredient_name != "xxx":
    
    # Get name (can't be blank)
    ingredient_name = not_blank ("Enter Ingredient Name: ", "Sorry, this can't be blank")

    if ingredient_name == "xxx":
        break

    # asks for the quantity, if quantity = 0 puts error message than asks question again
    quantity = num_check("How much do you need? ", "Sorry, the amount must be a number or a number more than 0")

    # asks user for package amount
    package_amount = num_check("Enter Package amount: ", "Sorry, the amount must be a number or a number more than 0")
        
    # asks user for the cost of ingredient
    price = num_check ("Enter the price: $", "Sorry, the amount must be a number more than 0")

    # asks for the unit, if not in list asks again
    unit = choice_checker ("Enter the unit: ", unit_list, "Invalid response, try again")

    # calculates price over package_amount then times it by quantity
    cost_to_make = (price / package_amount) * quantity  
    
    # puts ingredient costs in to a total
    total += cost_to_make

    print("{:.2f}".format(cost_to_make))

print("Total: {:.2f}".format(total)) 

# asks user how many people they will be serving
per_serve = num_check("How many people will you be serving? ", "Sorry, the amount must be a number more than 0")

price_per_serve = total/per_serve
print("{:.2f}".format(price_per_serve))