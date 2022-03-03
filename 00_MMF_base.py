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
            print("NOT a number")


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

  if name == "xxx":
    break

  print()

  # Get age (between 12 and 130
  age = int_check("How old? ")
  #check the age is valid...
  if age < 12:
    print("sorry you are too young for this movie")
    continue

  elif age > 130:
    print("that is very old _ it looks like a mstake")
    continue

  # if age is OK, increase ticket count
  count += 1

print("you have {} tickets left".format(MAX_TICKETS - count))

 
  


  # calculate ticket price

  # loop to ask for snacks

  # calculate snack price

  # ask for payment method (and apply surcharge if necessary)


# calculate total sales and profits

# output data to nexts file