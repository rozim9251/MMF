import re


#  functions go here


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


def not_blank (question, error_messasge) :
    valid = False

    while not valid:
        response = input (question)

        if response !="":
             return response
        else:
              print(error_messasge)

# checks for interger more than 0
def int_check(question):

    error = "please enter a whole number that is more than 0"

    valid = False
    while not valid:
        try:
            response = int(input(question))
            print(response)
            if response <= 0: 
                print (error)  

            else:
                return response    

        except ValueError:
            print(error)

def get_snack():
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

    # holds snack order for a single user
    snack_order = []

    desired_snack = ""
    while desired_snack != "xxx":

        snack_row = []

        # ask user for desired snack and put it in lower case
        desired_snack = input("snack: ") .lower()

        if desired_snack == "xxx":
            return snack_order


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
        snack_row.append(amount)
        snack_row.append(snack_choice)

          # check that snack is not the exit code before adding
        if snack_choice != "xxx" and snack_choice != "invalid choice":
            snack_order.append(snack_row)



#**********Main Routine**********

# set up dictionaries / lists needed to hold data

# initialise variables
count = 0
profit = 0
MAX_TICKETS = 5

# Ask if they have used the program before & show instructions if necessary

# Loop to get ticket details
name = ""
while name != "xxx" and count < MAX_TICKETS:
  print ("You have {} seats left". format (MAX_TICKETS - count)) 


  # Get details...
  # Get name (can't be blank)
  name = not_blank ("Name: ", "Sorry, this can't be blank")

  if name == "xxx":
    break

  print()

  

  # Get age (between 12 and 130)
  age = int_check("How old? ")
  #check the age is valid...
  if age < 12:
    print("sorry you are too young for this movie")
    continue

  elif age > 130:
    print("that is very old _ it looks like a mistake")
    continue

  # ask user for desired snack and put it in lower case
  desired_snack = input("snack: ") .lower()
 
  # calculate ticket price based on age
  if age < 16:
    ticket_price = 7.5
  elif age < 65:
    ticket_price = 10.5
  else:
    ticket_price = 6.5    


  # if age is OK, increase ticket count
  count += 1

  profit_made = ticket_price - 5
  profit += profit_made

  print("{}  : ${:.2f}".format(name, ticket_price))  

  print("Profit from Tickets: ${:.2f}".format(profit))

  # loop to ask for snacks

  # calculate snack price

  # ask for payment method (and apply surcharge if necessary)


  # ***** Loop for getting information ends here.  ****

# calculate total sales and profits

# output data to text file


# Ending stuff.  Might not need it after all??
print("you have {} tickets left".format(MAX_TICKETS - count))