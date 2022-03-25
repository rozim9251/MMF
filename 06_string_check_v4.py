

# functions go here
def string_check(choice, options):...


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
    if check_snack == "yes":

        desired_snack = ""
        while desired_snack != "xxx":
            # ask user for desired snack and put it in lower case
            desired_snack = input("snack: ") .lower()

            if desired_snack == "xxx":
                break

            # check if snack is valid
            snack_choice = string_check(desired_snack, valid_snacks)
            print("snack choice: ", snack_choice)

            # add snack to list...

            # check that snack is not the exit code before adding
            if snack_choice != "xxx" and snack_choice != "invalid choice":
                snack_order.append(snack_choice)

# show sncak orders
print()
if len(snack_order) == 0:
    print("snack ordered: None")

else:
    print("snacks ordered")

    for item in snack_order:
        print(item)

