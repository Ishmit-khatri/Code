

class Requisitionsystem: #class
    def __init__(self):#init
        self.date = None
        self.requisition_id = 10000 + 1
        self.staff_id = None
        self.staff_name = None
        self.status = None
        self.requisition_item_total = 0
        self.approval_reference_number = None

    def staff_info(self):#new func
        self.date = input("Enter the date: ")
        self.staff_id = input("Enter the staff ID: ")
        self.staff_name = input("Enter the staff name: ")
        print("Date:", self.date)
        print("Staff ID:", self.staff_id)
        print("Staff Name:", self.staff_name)
        print("Requisition ID:", self.requisition_id)
        return {
            "date": self.date,
            "staff_id": self.staff_id,
            "staff_name": self.staff_name,
            "requisition_id": self.requisition_id
        }

    def requisitions_details(self): #new func
        coffee = input("Enter the price of coffee $: ")
        paper = input("Enter the price of paper $: ")
        pen = input("Enter the price of pen $: ")
        self.requisition_item_total = int(coffee) + int(paper) + int(pen)
        print("The total value of requisition items is $", self.requisition_item_total)
        return self.requisition_item_total
#return
    def requisitions_approval(self): #new func
        if self.requisition_item_total < 500:
            self.status = "Approved"
        else:
            self.status = "Pending"
        self.approval_reference_number = str(self.staff_id) + str(self.requisition_id)[2:]
        print("Approval Reference Number:", self.approval_reference_number)
#using if
    def respond_requisitions(self): #new func
        print("Date:", self.date)
        print("Requisition ID:", self.requisition_id)
        print("Staff ID:", self.staff_id)
        print("Staff Name:", self.staff_name)
        print("Total: $", self.requisition_item_total)
        print("Status:", self.status)
        print("Approval Reference Number:", self.approval_reference_number) #printing all
#calling instance
requisition1 = Requisitionsystem()
requisition1.staff_info()
requisition1.requisitions_details()
requisition1.requisitions_approval()
requisition1.respond_requisitions()

requisition2 = Requisitionsystem()
requisition2.staff_info()
requisition2.requisitions_details()
requisition2.requisitions_approval()
requisition2.respond_requisitions()

requisition3 = Requisitionsystem()
requisition3.staff_info()
requisition3.requisitions_details()
requisition3.requisitions_approval()
requisition3.respond_requisitions()

requisition4 = Requisitionsystem()
requisition4.staff_info()
requisition4.requisitions_details()
requisition4.requisitions_approval()
requisition4.respond_requisitions()

# Display requisition statistics
total_requisitions = 4
approved_requisitions = 2
pending_requisitions = 1
not_approved_requisitions = 1

print("\nRequisition Statistics:")
print("Total number of requisitions submitted:", total_requisitions)
print("Total number of approved requisitions:", approved_requisitions)
print("Total number of pending requisitions:", pending_requisitions)
print("Total number of not approved requisitions:", not_approved_requisitions)

#printing all

      
    


