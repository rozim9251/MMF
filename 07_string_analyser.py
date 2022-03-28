import re

# works out whether string has numbers
# and seperates string into amount item

test_strings = [
    "popcorn",
    "2 pc",
    "1.50J",
    "40J",
]

for item in test_strings:

    # regular expression to find if item starts with a number
    number_regex = "^[1-9]"
    
    #if item has a number, seperate it into two (number / item)
    if re.match(number_regex, item):
        amount = int(item[0])
        desired_snack = item[1:]

    else:
        amount = 1
        desired_snack = item
        
        # remove white sapce arounf snack
        desired_snack = desired_snack.strip()

        # if item does not have a number in front, set number to 1

    # print order
    print("amount:", amount)
    print("snack:", desired_snack)
    print("lenght of snack:", len(desired_snack))