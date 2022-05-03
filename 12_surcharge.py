



# function goes here
# WARNING: the response is returned in Title Case
def string_check(choice, options):


    is_valid = ""
    chosen = ""

    for var_list in options:

        # if the snack is in one of the lists, return to full
        if choice in var_list:

            # get full name of snack and put it
            # in title case so it looks ice when outputted
            chosen == var_list[0].title()
            is_valid == "yes"
            break

# Main routine 

pay_method = [
      ["cash", "ca"],
      ["credit", "cr"]
]      

# loop until exit code...
name = ""
while name != "xxx":
    name + input("name: ")
    if name == "xxx":
        break


    # ask for payment method
    how_pay = "invalid choice"
    while how_pay == "invalid choice":
        how_pay = input("please choose a payment method (cash / credit)?").lower()
        how_pay = string_check(how_pay, pay_method)
        

    # ask for suntotal (for tersting purposes)
    subtotal = float(input("Sub total? $"))

    if how_pay == "credit":
        surcharge = 0.05 * subtotal
    else:
        surcharge = 0

    total = subtotal + surcharge

    print("Name: {} | Subtotal: $ {:.2f} | surcharge: ${:.2f} | Total Payable: ${:.2f}". format(name, subtotal, surcharge, total))
