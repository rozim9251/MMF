

#functions go here
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

yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

check_snack = "invalid choice"
while check_snack == "invalid choice":
    want_snack = input("do you want to order snacks? ").lower()
    check_snack = string_check(want_snack, yes_no)
    print(check_snack)


# loop ten times to make testing quicker
for item in range(0, 10):

    # ask user for desired snack and put it in lowercase
    desired_snack = input("snack: ") .lower()

    #check if snack is valid
    snack_choice = string_check(desired_snack, valid_snacks)
    print("snack choice: ", snack_choice)