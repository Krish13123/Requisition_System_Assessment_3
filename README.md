
# Requisition Management System 

## Introduction

i created the that python program to staff can create requisitions on the basis of need. The program will ask staff to enter their details, record of items they want, automatically check approval based on total cost, and display the requisition details.  

## How the code is Working? (Analyze)
The program is divided into four tasks:

**Task 1: staff_info()**  
Collects staff details such as staff name, ID, date, and generates a unique requisition ID.  
This ensures each requisition has a unique identifier and the input is validated so staff cannot leave fields empty.  

**Task 2: requisitions_total()**  
Asks the staff for the number of items, their names, and prices.  
and then calculates the total cost of all items entered.  
and also i used (try/except) so the program doesn’t show error if the user types except their requirements means int or float.  

**Task 3: requisition_approval()**  
Checks if the requisition should be Approved or Pending based on total cost.  
If the total is less than $500, it is automatically approved. Otherwise, the status is set to pending.  
Generates an approval reference number for if status is approved. and when status is pending so it shows reference number N/A.  

**Task 4: display_requisitions()**   
Displays the requisition details including staff info, items, total cost, and approval status.  
Asks the user if they want to create another requisition. If “yes,” the function calls itself and repeats the process.  

## Software Design Principles Used in My Tasks



### 1. KISS (Keep It Simple Stupid)
In my first task, I used the KISS principle because the function is only for collecting staff information. Keeping it simple makes the code easy to understand, easy to debug, and easy to maintain without adding extra complexity.

### 2. Avoid Premature Optimisation
In my second task, I used Avoid Premature Optimisation because I focused on making the code correct and readable before worrying about performance. This means it is better to have working, simple code first and only make it faster later if really needed and also i doing to many copy/paste beacuse used to many same loops.

### 3. Separation of Concerns
In my third task, I used Separation of Concerns because the function only handles approval logic and not staff input or item totals. This makes each part of the program do one clear job, which makes it easier to test and fix problems.

### 4. DRY (Don’t Repeat Yourself)
In my fourth task, I used the DRY principle because the same printing logic works for both “yes” and “no” options. Reusing the function that i have created instead of copying it keeps the program maintain.


## Other Principles that i have not used

### 5. Open/Closed Principle
if we need in future, Code should allow new features to be added without changing the existing code. This makes the program safer because old parts will not break when new functionality is added. i have example of this code, in this code we are using only approved and pending status but in part b scenario is given like we need to put three status: Approved, pending or not approved.

### 6. Composition > inheritance
I did not use Composition Over Inheritance because my tasks did not involve complex classes or object hierarchies. The program was small and simple, so combining small parts and i not using a class.

### 7. Single Responsibility Principle
I did not follow the Single Responsibility Principle in Task 2 and Task 4 because some functions handled multiple jobs, like input and calculation together, or printing and decision logic together. Since the tasks were small, and other have means task 1 and 3 have on responsibility but i not mention in my code.

### 8. YAGNI (You Aren’t Gonna Need It)
I did that we should only write code for what is needed right now. Writing extra features that need later can make the program more complicated. Keeping it simple helps us to understand the code easily.

### 9. Refactor, Refactor, Refactor
Code should be as possible as improved existing code without changing its external behavior. This makes the code cleaner and easier to read. It also helps the program run more efficiently and reduces errors.

### 10. Clean Code Over Clever Code
we can keep Code should be easy to read rather than overly complicated. Clear code is easier to understand and fixing the error. and also This makes it simpler to update and reduces mistakes.

