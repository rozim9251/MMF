#   imports statement


#  functions go here

def not_blank (question, error_messasge) :
    valid = False

    while not valid:
        response = input (question)

        if response !="":
             return response
        else:
              print(error_messasge)


#**********Main Routine**********

# set up dictionaries / lists needed to hold data

# initialise variables
count = 0
MAX_TICKETS = 5

# Ask if they have used the program before & show instructions if necessary

# Loop to get ticket details
name = ""
while name != "xxx" and count < MAX_TICKETS:
    print ("You have {} seats left". format (MAX_TICKETS - count)) 


    # Get details...
    # Get name (can't be blank)
    name = not_blank ("Name: ", "Sorry, this can't be blank")
    count += 1
    print()
 
  
  # Get age (between 12 and 130

  # calculate ticket price

  # loop to ask for snacks

  # calculate snack price

  # ask for payment method (and apply surcharge if necessary)


# calculate total sales and profits

# output data to nexts file