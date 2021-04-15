class Node:
    # This class provides a generic node for a linked list. 
    def __init__(self, number, name):
        self.value = int(number) #number element, in this case ssn
        self.name = str(name) #name element attached to ssn
        self.next = None #pointer

class IRS_Single_Linked_List:
    def __init__(self):
        self.headPtr = None

    def traverse_list(self):
        if self.headPtr is None:
            print("List has no element")
            return
        else:
            iterative_node= self.headPtr
            while iterative_node is not None:
                print (iterative_node.value, " ")
                iterative_node = iterative_node.next

    def insert_at_end(self, number, name):
        new_node = Node(number, name)
        if self.headPtr is None:
            self.headPtr = new_node
            return
        iterative_node = self.headPtr
        while iterative_node.next is not None:
            iterative_node= iterative_node.next
        iterative_node.next = new_node

    # Search to see if an ssn exists in the SLL. If it does -- return True. Else return false 
    def search_value(self, x):
        if self.headPtr is None:
            print("List has no elements")
            
        else: 
            iterative_node = self.headPtr
            while iterative_node is not None:
                if iterative_node.value == x:
                    print("value found")
                    return True
                iterative_node = iterative_node.next
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

        iterative_node = self.headPtr
        while iterative_node.next is not None:
            if iterative_node.next.value == x:
                break
            iterative_node = iterative_node.next

        if iterative_node.next is None:
            print("value not found in the list")
        else:
            iterative_node.next = iterative_node.next.next

################# Driver Section ################## 

print("Welcome to the new IRS database!")
print("We are still in beta mode so please be patient.")
print("The site is able at this time to insert, delete and replace")
print("a tax payers information but it will require a SSN for data input.")
print("Listed below are a collection of SSN's and names that need to be")
print("inserted into the database. Please complete this task.")

irs_file = open("irs_list.txt", "r")
print(irs_file.read())

i_d_r = input("If you want to select insert please type lowercase 'i', delete lowercase 'd' or lowercase 'r' if you wish to see if that SSN is in the system: ")
i_ssn_counter = 0
d_ssn_counter = 0
r_ssn_counter = 0

# Defining a single linked list object 
irs_list = IRS_Single_Linked_List()


# TODO: Add File reader function to get info from sample.txt
# While reading the file

# If the letter code is i
if i_d_r == 'i':
    name = input("Please provide your full name: ")
    number = input("Please input your social security number: ")
    # You want to insert the new name and ssn only IF it is not in the data structure
    if (irs_list.search_value(number)) == True:
        print ("This SSN number already exists under a different name.")
    else:
        irs_list.insert_at_end(number, name)
        i_ssn_counter += 1
        print ("This SSN/Name has been added to our system.")
    
if i_d_r == 'd':
    x = input("Please input the social security number you want to delete: ")
    if irs_list.search_value(x) == True:
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

irs_list.traverse_list()

