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

quantity = num_check("how much do you have?", "The amount must be a whole number more than 0")