class Node:
    # This class provides a generic node for a linked list. 
    def __init__(self, number, name):
        self.value = int(number) #number element, in this case ssn
        self.name = str(name) #name element attached to ssn
        self.next = None #pointer

class IRS_Single_Linked_List:
    def __init__(self):
        self.headPtr = None

    def insert_at_end(self, number, name):
        new_node = Node(number, name)
        if self.headPtr is None:
            self.headPtr = new_node
            return
        n = self.headPtr
        while n.next is not None:
            n= n.next
        n.next = new_node

    def search_value(self, x):
        if self.headPtr is None:
            print("List has no elements")
            return
        n = self.headPtr
        while n is not None:
            if n.value == x:
                print("value found")
                return True
            n = n.next
        print("value not found")
        return False

    def delete_element_by_value(self, x):
        if self.headPtr is None:
            print("The list has no element to delete")
            return

    # Deleting first node 
        if self.headPtr.value == x:
            self.headPtr = self.headPtr.next
            return

        n = self.headPtr
        while n.next is not None:
            if n.next.value == x:
                break
            n = n.next

        if n.next is None:
            print("value not found in the list")
        else:
            n.next = n.next.next

print("Welcome to the new IRS database!")
print("We are still in beta mode so please be patient.")
print("The site is able at this time to insert, delete and replace")
print("a tax payers information but it will require a SSN for data input.")

i_d_r = input("If you want to select insert please type lowercase 'i', delete lowercase 'd' or lowercase 'r' if you wish to see if that SSN is in the system: ")
i_ssn_counter = 0
d_ssn_counter = 0
r_ssn_counter = 0
irs_list = IRS_Single_Linked_List()
if i_d_r == 'i':
    name = input("Please provide your full name: ")
    number = input("Please input your social security number: ")
    if number not in irs_list:
        irs_list.insert_at_end(number, name)
        i_ssn_counter += 1
    else:
        print ("This SSN already exists in our system.")
    
if i_d_r == 'd':
    x = input("Please input the social security number you want to delete: ")
    if x in irs_list:
        irs_list.delete_element_by_value(x)
        print("The social security number you have entered and the name associated with it has been deleted.")
        d_ssn_counter += 1
    else:
        print("The social security number you have input does not exist.")

if i_d_r == 'r':
    x = input("Please input the social security number you want to retrieve: ")
    if irs_list.search_value(x) is True:
        print ("The social security number you entered has been found in our database.")
        r_ssn_counter += 1
    else:
        print("The social security number you entered has not been found in our system.")