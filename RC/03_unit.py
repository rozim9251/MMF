# Checks if items in list
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
                print("Unit: " + response)
                return item

        # output error if item is not in list
        print(error)
        print()

# Unit list
unit_list = ["kilograms", "grams", "milliliters"]

# asks for the unit, if not in list asks again
unit = choice_checker ("Units?", unit_list, "Invalid response, try again")
