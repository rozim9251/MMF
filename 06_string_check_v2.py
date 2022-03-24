
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

# initialise variables
snack_ok = ""
snack = ""

# loop three times to make testing quicker
for item in range(0, 10):

    # ask user for desired snack and put it in lowercase
    desired_snack = input("snack: ") .lower()

    for var_list in valid_snacks:

        # if the snack is one of the lists< return full names
        if desired_snack in var_list:

            # get full name of snack and put it in 
            # in title case so it looks nice when outputted
            snack = var_list[0].title()
            snack_ok = "yes"
            break

        #if the chosen snack is not valid, set snack_ok to no
        else:
            snack_ok = "no"

    #if snack is not OK - ask question again.
    if snack_ok == "yes":
        print("snack choice: ", snack)
    else:
        print("invalid choice")
