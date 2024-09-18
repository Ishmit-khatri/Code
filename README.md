

# Requisition System

## Project Overview

This project implements a simple requisition system for managing office supplies. It collects staff information, tracks requisition items, and calculates the total cost of items requested. The system is designed using object-oriented programming principles in Python.

## Features

- Collects staff information (date, staff ID, and name).
- Tracks requisition items (e.g., coffee, paper, pen) and calculates their total cost.
- Assigns a unique requisition ID for each request.
- Approves or marks requisitions as pending based on the total item cost.
- Provides a unique approval reference number for approved requisitions.
- Displays a summary of all requisitions, including approved, pending, and rejected.

## Code Structure


### Class: `Requisitionsystem`


#### Attributes:

- `date`: The date of the requisition.
- `requisition_id`: A unique id starting from 10001.
- `staff_id`, `staff_name`: Information of staff making the requisition.
- `status`: The current real status of the requisition (Approved or Pending).
- `requisition_item_total`: Total cost of items requested.
- `approval_reference_number`: A reference number for approval, created by combining `staff_id` and part of the `requisition_id`.

#### Methods:

1. `staff_info()`: 
   - Prompts the user to enter staff information (date, ID, and name) and displays it.
   - Returns a dictionary containing the staff details.

2. `requisitions_details()`:

   - Prompts the user to input the price of office items (coffee, paper, and pen).
   - Calculates and displays the total value of requisition items.

4. `requisitions_approval()`: 
   - Approves the requisition if the total is under $500.
   - If the total exceeds $500, the requisition is marked as "Pending."
   - Generates an approval reference number.

5. `respond_requisitions()`: 
   - Displays all the requisition information, including total cost, status, and approval reference number.

6. **Requisition Statistics:**
   - The system also displays requisition statistics whereby it is possible to view the number of approved, pending and rejected requisitions.

## How to Run

1. Ensure Python is installed on your system.
2. Run the `requisitionsystem.py` file using Visual Studio Code or a terminal.
3. Follow the prompts to input staff information and requisition details.
4. After running the script, you will see statistics for all the submitted requisitions.


## Conclusion:

This structure ensures all aspects of the system are well-documented and provides a better understanding to users.

## Example Output
```bash
Enter the date: 2024-09-17
Enter the staff ID: 123
Enter the staff name: Alice
Enter the price of coffee $: 5
Enter the price of paper $: 10
Enter the price of pen $: 3
The total value of requisition items is $ 18
Approval Reference Number: 1230001
...

Follow the prompts to enter staff information and requisition details.





