# imports...



# Functions go here

# checks that string is not blank
from cgi import print_exception


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
        for item in valid_list:
            if response == item[0] or response == item:
                print()
                return item

        # output error if item is not in list
        print(error)
        print()


def cost_for_ingredient():
    # Get name (can't be blank)
    name = not_blank ("Ingredient Name: ", "Sorry, this can't be blank")

    # asks for the quantity, if quantity = 0 puts error message than asks question again
    quantity = num_check("how much do you need? ", "Sorry, the amount must be a number or a number more than 0")
    
    # asks user for package amount
    package_amount = num_check("Package amount: ", "Sorry, the amount must be a number or a number more than 0")

    # asks user for the cost of ingredient
    price = num_check ("Package Cost: $", "The amount must be a number more than 0")
  
    # asks for the unit, if not in list asks again
    unit = choice_checker ("Units? ", unit_list, "Invalid response, try again")

    cost_to_make = ""

    return cost_to_make

# ***** Main routine *****

# unit list
unit_list = ["kilograms","kg", "grams", "g", "millilitres", "ml"]

for item in range(0,4):
    var_item_cost = cost_for_ingredient()

    print(var_item_cost)

























# Printing area
