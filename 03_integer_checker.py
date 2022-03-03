# functions go here


# checks for interger more than 0
def int_check(question):

    error = "please ente a whole number that is more than 0"

    valid = False
    while not valid:
        try:
            response = int(input("Number: "))
            print(response)
            if response <= 0: 
                print (error)  

            else:
                return response    

        except ValueError:
            print("NOT a number")

      


#  ***** Main Routine ********
age = int_check("How old? ")
