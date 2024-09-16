def staff_info():
    #enter all the inputs
    name= str(input("enter staff name:"))
    staff_id= str(input("enter staff id:"))
    date= str(input("enter the date(dd/mm/yyyy):"))
    #this is the formula for counter
    requisition_id= 1 ++ 10000
  #print all the imputs
    print ("name", name)
    print ("staff_id", staff_id)
    print ("date", date)
    print ("requisition_id", requisition_id)
    #return 
    return {
        "name", name,
        "staff_id", staff_id,
        "date", date,
        "requisition_id", requisition_id
    }
#call the function here
staff_info()

def requisition_total():
   #call the fuction staff_info
    staff_info
    total= 0
    #input
    Coffee= input("the price of Coffe is $:")
    Paper= input("the price of Paper is $:")
    Pen= input("the price of Pen is $:")
    #add
    requisition_item_total= int(Coffee) + int(Paper) + int(Pen)
    print("total= $",requisition_item_total)
    #return
    return {
         requisition_item_total
    }
#requisition_total()



def requisition_approval():
    #call the fuction
    requisition_total()
    #while loop
    given_range= 0
    for i in range(given_range):
        if i >= 500:
            print ("Approved")
            #giving refrence number
            staff_id= input("enter your staff_id")
            requisition_id= input ("enter your requisition_id")
            x= staff_id
            y= requisition_id [:3]
            approval_reference_number= x + y
            return approval_reference_number
        else:
            print ("Pending")
            #return
            return None
requisition_approval()


def display_requisition():
    #calling all the function and printing them
    staff_info
    requisition_total
    requisition_approval
    print("printing requisition:")
    print(f"date: {staff_info['date']}")
    print(f"requisition_id: {staff_info['requisition_id']}")
    print(f"staff_id: {staff_info['staff_id']} ")
    print(f"name: {staff_info['name']}")
    print (f"total:{requisition_total['total']}")
    print (f"approved:{requisition_total['approved']}")
    print (f"approval_reference_number:{requisition_approval['approval_reference_number']}")
#displaying all output
display_requisition(staff_info, requisition_total, display_requisition)


