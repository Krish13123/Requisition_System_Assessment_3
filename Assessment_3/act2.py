"""
I used the Avoid Premature Optimisation principle because I focused on making the code correct
and easy to understand first and not making it complex.
"""

from act1 import staff_info   # import staff_info to run and use staf information.

def requisitions_total():   # create a function to calculate item costs.
    d_date, staff_id, staff_name, requisition_id = staff_info()   

    while True:   # i used try and except beacuse if user is not inputing int so it can be show error.
        try:
            ask_staff = int(input("\nEnter Number of the items: "))   # Ask user for number of items.
        except ValueError:  
            print("Incorrect input. please try again.")   # Show error if input is not number.
        else:
            break 

    total_price = 0   # Start total cost at 0.

        """
        i used a for loop because i needed to print every item 
        that the user entered earlier the number of items. 
        """
   
    for items_num in range(ask_staff):   
        print(f"Item {items_num+1}")   # i used items_num+1 beacuse whenever we are giving range it start from 0 and i need to start from 1.

        while True:   
            items_name = input("Enter the name of item: ")   # Ask for items name.
            if items_name == "":   
                print("incorrect input. please try again.")    # Print error message if empty.
            else:
                break   

        while True:   
            try:
                cost_item = float(input("Price :$"))   # Ask for price of items.
            except ValueError:   
                print("Incorrect input. please try again.")  # Show error if input is not number.
            else:
                break  

        total_price = total_price + cost_item   # Add item cost to total.

    print(f"Total cost of the items: {total_price}")   # printing final total.

    return total_price, d_date, staff_id, staff_name, requisition_id   # Return all  details so i am able to use and run in another function.


