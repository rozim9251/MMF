# start of loop

# initiate loop so that it runs at least once
name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:
    print ("You have {} seats left". format (MAX_TICKETS - count)) 


     # Get details...
    name = input ("Name: ")
    count += 1
    print()

if count == MAX_TICKETS:
    print("You have sold all the availabel tickets!")
else:
    print("You have sold {} tickets. /n There are {} places still avilabel .format(count, MAX_TICKETS - count)")         