# functoins go here


def not_blank (question, error_messasge) :
    valid = False

    while not valid:
        response = input (question)

        if response !="":
             return response
        else:
              print(error_messasge)


#Main Routine goes here 
name = not_blank("Name: ",
                 "Sorry _ this can't be blank, please enter your name")                 