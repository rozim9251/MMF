#import libraries

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


# *** Main Routine goes here ***

