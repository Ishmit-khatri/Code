Class: `Requisitionsystem`
Attributes: 
- `date`, `requisition_id`, `staff_id`, `staff_name`, `status`, `requisition_item_total`, `approval_reference_number`.
- The `requisition_id` starts at 10001.
  - 
Methods:
- `staff_info`: Collects and displays staff information (date, staff ID, staff name) and returns a dictionary containing this data.
- `requisitions_details`: Asks for the price of coffee and pen, but this part is not fully visible yet.

Requisition System

Project Overview

This project implements a simple requisition system for managing office supplies. It collects staff information, tracks requisition items, and calculates the total cost of items requested. The system is designed using object-oriented programming principles in Python.

Features

- Collecting staff information such as date, staff id, and name.
- Tracks requisition items (e.g., coffee, pen) and calculates their total cost.
- Assigns a unique requisition ID for each requisition.
  
Code Structure

Class: `Requisitionsystem`

Attributes:
- `date`: The date of the requisition.
- `requisition_id`: A unique ID starting from 10001.
- `staff_id`, `staff_name`: Information about the staff making the requisition.
- `status`: The current status of the requisition (not yet implemented).
- `requisition_item_total`: Total cost of items requested.
- `approval_reference_number`: A reference number for approval (not yet implemented).

Methods:
1. `staff_info()`: 
- Prompts for staff information (date, ID, and name) and displays it.
- Returns a dictionary containing the staff details.
     
2. `requisitions_details()`: 
- (Incomplete in this preview) Prompts the user for item prices (e.g., coffee, pen).

How to Run

1. Install Python (if not installed).
2. Run the `requisitionsystem.py` file in a Python environment.
3. Follow the prompts to enter staff information and requisition details.
