from classes.singleLinkedList1 import LinkedList, Node

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
irs_list = LinkedList()

#  STARTING HERE -- add an infinite loop while(1):
# TODO: Add File reader function to get info from sample.txt
# While reading the file

# If the letter code is i
are_you_done = 0
while are_you_done is not 1:
    if i_d_r == 'i':
        name = input("Please provide your full name: ")
        number = input("Please input your social security number: ")
        # You want to insert the new name and ssn only IF it is not in the data structure
        if (irs_list.traverse_list()) == True:
            print ("This SSN number already exists under a different name.")
        else:
            irs_list.add(number, name)
            i_ssn_counter += 1
            print ("This SSN/Name has been added to our system.")

    if i_d_r == 'd':
        x = input("Please input the social security number you want to delete: ")
        if irs_list.find(x) == True:
            irs_list.remove(x)
            print("The social security number you have entered and the name associated with it has been deleted.")
            d_ssn_counter += 1
        else:
            print("The social security number you have input does not exist.")

    if i_d_r == 'r':
        x = input("Please input the social security number you want to retrieve: ")
        if irs_list.find(x) is True:
            print ("The social security number you entered has been found in our database.")
            r_ssn_counter += 1
        else:
            print("The social security number you entered has not been found in our system.")
    
    are_you_done = int(input("are you done? if so type 1, if not type 0."))
    if are_you_done == 1:
        print (i_ssn_counter)
        print (d_ssn_counter)
        print (r_ssn_counter)
        irs_list.traverse_list()
    else:
        irs_list.traverse_list()
        i_d_r = ("If you want to select insert please type lowercase 'i', delete lowercase 'd' or lowercase 'r' if you wish to see if that SSN is in the system: ")


