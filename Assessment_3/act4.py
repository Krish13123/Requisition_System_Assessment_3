# for priciple please see 36 line.

from act3 import requisition_approval   # Import requisition_approval so i can use and run every function that i have created before.

def display_requisitons():   # create function to display requisitions.
    status, r_num, total_price, d_date, staff_id, staff_name, requisition_id = requisition_approval()   

        """
        i used while loop beacuse if staff needs to input more requisitons so
        they can able to add and if staff input except yes/no so it says error. 
        """

    while True:   
        choice = input("\nIf needs more Requisitions type 'yes' or 'no': ")   # Ask to staff needs more requisition yes or no .

        if choice == "no":   # If staff dont want requisitions.
            print("\nPrinting Requisitions: ")   # Print details.
            print(f"\nDate: {d_date}")
            print(f"Requisition ID: {requisition_id}")
            print(f"Staff ID: {staff_id}")
            print(f"Staff name: {staff_name}")
            print(f"Total: {total_price}")
            print(f"Status: {status}")
            print(f"Approval reference number: {r_num}")
        
        elif choice == "yes":   # If staff wants more requisitions.
            print("\nPrinting Requisitions: ")   
            print(f"\nDate: {d_date}")
            print(f"Requisition ID: {requisition_id}")
            print(f"Staff ID: {staff_id}")
            print(f"Staff name: {staff_name}")
            print(f"Total: {total_price}")
            print(f"Status: {status}")
            print(f"Approval reference number: {r_num}") # Print details again.and then below:
            """
            in my code, i write function again for new requisition.
            and here i used DRY (Dont Repeat Yourself) principle,
            because when the user types ‘yes’, the program should ask again for a new requisition. 
            Calling the function again makes the process repeat without writing extra code.”
            """
             display_requisitons()   

        else:   # If input is not yes or no.
            print("Please enter a Valid input")   # Show error message.

display_requisitons()   # run the whole system.
