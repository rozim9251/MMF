import re


# functions go here
def string_check(choice, options):

    for var_list in options:

        #if the snack is one of the lists, retrun the full
        if choice in var_list:

            #get full name of snack and put it
            #in title case so it looks nice when outputted
            chosen = var_list[0].title()
            is_valid = "yes"
            break

        #if the chosen option is not valid, set is_valid to no
        else:
            is_valid = "no"

     # if the snack is not OK - ask again
    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"  



 # regular expression to find if item starts with a number
number_regex = "^[1-9]"

#valid snacks holds list of all snacks
#each item in valid snacks is a list with
#valid options for each <full name, letter code (a - e)  
# , and possible abbreviations etc>
valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&M's", "m&m's", "mms", "m", "b"],  #first item is M&M's
    ["pita chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"]
]

# valid options for yes / no questions
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

# holds snack order for a single user
snack_order = []


# ask user if they want snack
check_snack = "invalid choice"
while check_snack == "invalid choice":
    want_snacks = input("do you want to order snacks? "). lower()
    check_snack = string_check(want_snacks, yes_no)


# if they say yes, ask what snack they want (and add to our snack)
if check_snack == "Yes":

    desired_snack = ""
    while desired_snack != "xxx":
        # ask user for desired snack and put it in lower case
        desired_snack = input("snack: ") .lower()

        
        if desired_snack == "xxx":
            break

              #if item has a number, seperate it into two (number / item)
        if re.match(number_regex, desired_snack):
            amount = int(desired_snack[0])
            desired_snack = desired_snack[1:]

        else:
            amount = 1
            desired_snack = desired_snack



        # remove white space around snack
        desired_snack = desired_snack.strip()

        # check if snack is valid
        snack_choice = string_check(desired_snack, valid_snacks)

        # check snack amount is valid (less than 5)
        if amount >= 5:
            print("sorry - we have a four snack maximum")
            snack_choice = "invalid choice"

        # add snack AND amount to list...
        amount_snack = "{} {}". format(amount, snack_choice)

        # check that snack is not the exit code before adding
        if snack_choice != "xxx" and snack_choice != "invalid choice":
            snack_order.append(amount_snack)

# show snack orders
print()
if len(snack_order) == 0:
    print("snacks ordered: None")

else:
    print("snacks ordered:")    

    for item in snack_order:
        print(item)
