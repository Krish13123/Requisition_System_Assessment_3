"""
I used the Separation of Concerns principle because this function only handles approval status checking 
the total and deciding status according to total oprice of items. this task will help staff to auto
generate status and reference number.
"""

from act2 import requisitions_total   # import requisitions_total to run and use info and total.

def requisition_approval():   # create a function to approve or pending requests and also genrate reference number.
    total_price, d_date, staff_id, staff_name, requisition_id = requisitions_total()   

    if total_price < 500:   # If cost is less than 500 then Approve requisition.
        status = "Approved"   
        r_num = staff_id + str(requisition_id)[-3:]   # if aprroved so genrate reference number using staff ID + last 3 digits of requisition ID.
    else:             
        status = "pending"  # If cost is 500 or more so Status is pending.
        r_num = "N/A"   # No reference number available if status pending.

    print(f"Approval reference number: {r_num}")   # print reference number.
    print(f"status: {status}")   # print approval status.

    return status, r_num, total_price, d_date, staff_id, staff_name, requisition_id   # Return details.

