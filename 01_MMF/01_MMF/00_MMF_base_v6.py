import re

import pandas

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
    ["mms", "M&M's", "m&m's", "m", "b"],  #first item is M&M's
    ["pita chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"],
    ["orange juice", "oj", "juice", "e"]
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
        
        if snack_choice == "invalid choice":
            print("sorry that is not a valid snack choice")
    

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

yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

# list valid responses for payment method
pay_method = [
      ["cash", "ca"],
      ["credit", "cr"]
]      

# initialise looop so that it runs at least once
MAX_TICKETS = 5

name = ""
ticket_count = 0
ticket_sales = 0

# Initialise lists (to make data-frame in due course)
all_names = []
all_tickets = []
popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

snack_lists = [popcorn, mms, pita_chips, water, orange_juice,]

# store surcharge multiplier
surcharge_multi_list = []

# Data frame Dictionary
movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets,
    'Popcorn': popcorn,
    'Water' : water,
    'Pita Chips': pita_chips,
    'Mms': mms,
    'Orange Juice': orange_juice,
    'Surcharge Multiplier': surcharge_multi_list
}

# initialise variables
count = 0
profit = 0
MAX_TICKETS = 5

# Ask if they have used the program before & show instructions if necessary

# cost of each snack
price_dict = {
    'Popcorn': 2.5,
    'Water': 2,
    'Pita Chips':4.5,
    'Mms':3,
    'Orange Juice': 3.25
}

# Loop to get ticket details
name = ""
while name != "xxx" and count < MAX_TICKETS:
    print ("You have {} seats left". format (MAX_TICKETS - count)) 
    # Get details...
    
    # Get name (can't be blank)
    name = not_blank ("Name: ", "Sorry, this can't be blank")

    if name == "xxx":
        break
    else:
        all_names.append(name)

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


    # calculate ticket price based on age
    if age < 16:
        ticket_price = 7.5
    elif age < 65:
        ticket_price = 10.5
    else:
        ticket_price = 6.5  

    all_tickets.append(ticket_price)          


    # if age is OK, increase ticket count 
    count += 1

    ticket_profit = ticket_price - 5
    profit += ticket_profit

    print("{}  : ${:.2f}".format(name, ticket_price))  

    print("Profit from Tickets: ${:.2f}".format(profit))



    # loop to ask for snacks
    # ask user if they want snack
    check_snack = "invalid choice"
    while check_snack == "invalid choice":
        want_snacks = input("do you want to order snacks? "). lower()
        check_snack = string_check(want_snacks, yes_no)
        if check_snack == "invalid choice":
            print("Please enter yes / no")

    # if they say yes, ask what snacks they want (and add to our snack list)
    if check_snack == "Yes":
        snack_order = get_snack()

    else:
        snack_order = []    

    # Assume no sncks have been bought...
    for item in snack_lists:
        item.append(0)

    # show snack orders
    for item in snack_order:
        if len(item) > 0:
            to_find = (item[1]) 
            amount = (item[0])
            add_list = movie_data_dict[to_find] 
            add_list [-1] = amount


      # Get payment method (ie: work out if surchatge is needed)
      # ask for payment method
    how_pay = "invalid choice"
    while how_pay == "invalid choice":
        how_pay = input("please choose a payment method (cash / credit)?").lower()
        how_pay = string_check(how_pay, pay_method)
        
    if how_pay == "Credit":
        surcharge_multiplier = 0.05
    else:
        surcharge_multiplier = 0

    surcharge_multi_list.append(surcharge_multiplier)
  
  # calculate snack price

  # ask for payment method (and apply surcharge if necessary)
# Create dataframe and set index to name column
movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index('Name')

# create column called 'Sub Total'
# fill it price for snacks and ticket

movie_frame["Sub Total"] = \
    movie_frame['Ticket'] + \
    movie_frame['Popcorn']*price_dict['Popcorn'] + \
    movie_frame['Water']*price_dict['Water'] + \
    movie_frame['Pita Chips']*price_dict['Pita Chips'] + \
    movie_frame['Mms']*price_dict['Mms'] + \
    movie_frame['Orange Juice']*price_dict['Orange Juice']

movie_frame["Surcharge"] = \
    movie_frame["Sub Total"] * movie_frame["Surcharge Multiplier"]

movie_frame["Total"] = movie_frame["Sub Total"] + \
    movie_frame['Surcharge']   

    # shorten column names
movie_frame = movie_frame.rename(columns={'Orange Juice': 'OJ',
                                        'Pita Chips': 'Chips',
                                         surcharge_multiplier: 'SM'})

#set columns to be printed ...
pandas.set_option('display.max_columns', None)

# Display numbers to 2 dp
pandas.set_option('precision', 2)

print_all = input("print all columns?? (y) for yes")
if print_all == "y":
    print(movie_frame)
else:
    print(movie_frame[['Ticket', 'Sub Total', 'Surcharge', 'Total']])

print() 

ticket_profit=ticket_sales-(5*ticket_count)
print("ticket profit: ${:.2f}".format(ticket_profit))

print(movie_frame)


  # ***** Loop for getting information ends here.  ****

# calculate total sales and profits

# output data to text file
 

# Ending stuff.  Might not need it after all??
print("you have {} tickets left".format(MAX_TICKETS - count))