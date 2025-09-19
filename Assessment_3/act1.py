"""
i used KISS (keep it simple stupid) principle to make this task.
i keep this function simple so it only collects staff details.
"""

num_counter = 0   # Start a counter at 0 so we can track of how many requisitions are made.

def staff_info():   # create a function called staff info.
    global num_counter   # Use global so we can increment num_counter as given in scenario.
    num_counter = num_counter + 1   # Increase the counter by one each time so can use for genrating id.
    requisition_id = num_counter + 10000   # i Create a requisition ID by adding 10000 to the counter beacuse we need to start from 10001.

# i used the while loop beacuse if staff input empty input so we cannot go to the next input is that called data validation.
# and i used data validation for all inputs in four task.

    while True:   
        staff_name = input("\nEnter the name of staff: ")   # Ask staff for staff name.
        if staff_name == "":   
            print("incorrect input. please try again.")    # Print error message if empty.
        else:
            break  

    while True:  
        d_date = input("Enter the date: ")   # Ask staff for date.
        if d_date == "":   
            print("Incorrect input. please try again.")   # Print error message if empty.
        else:
            break  
    
    while True:   
        staff_id = input("Enter the staff ID: ")   # Ask staff for staff ID.
        if staff_id == "":   
            print("Incorrect input. please try again.")   # Print error message if empty.
        else:
            break   

    print("\nprinting staff information: ")   # Print header message.
    print(f"\nDate: {d_date} ")   # Print the date.
    print(f"Staff ID: {staff_id}")   # Print staff ID.
    print(f"Staff Name: {staff_name}")   # Print staff name.
    print(f"Requisition ID: {requisition_id}")   # Print requisition ID.

# Return all  details so i am able to use and run in another function.
    return d_date, staff_id, staff_name, requisition_id   
