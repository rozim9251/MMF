# cheks that string is not blank
def not_blank (question, error_messasge) :
    valid = False

    while not valid:
        response = input (question)

        if response !="":
             return response
        else:
              print(error_messasge)
        

name = ""
while name != "xxx":
# Get name (can't be blank)
     name = not_blank ("Ingredient Name: ", "Sorry, this can't be blank")

