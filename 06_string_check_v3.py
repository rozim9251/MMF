

#functions go here
def string_check(choice, options):

    for var_list in options:

        #if the snack is one of the lists, retrun the full
        if choice is var_list:

            #get full name of snack and put it
            #in title case so it liiks nice when outputted
            chosen = var_list[0].title()
            is_valid = "yes"
            break

        #if the chosen optoni is not valid, set is_valid to no
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

# loop ten times to make testing quicker
for item in range(0, 10):

    # ask user for desired snack and put it in lowercase
    desired_snack = input("snack: ") .lower()

    #check if snack is valid
    snack_choice = string_check(desired_snack, valid_snacks)
    print("snack choice: ", snack_choice)