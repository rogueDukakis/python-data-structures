from classes.singleLinkedList1 import SLL

f = open("irs_list.txt", "r")

irs_list = SLL()

i_counter = 0
d_counter = 0
r_counter = 0

for i in f:
    
    # line breaks it up to four elements (0th is idr 1st is ssn 2nd and 3rd is the name f and l)
    line = i.split(" ")
    print(line)


    if line[0] == "i":
        check_insert = irs_list.insert(line[1], (line[2] + " " + line[3]))

        if check_insert is True:
            i_counter+=1
    #d
    elif line[0] == "d":
        check_delete = irs_list.delete(line[1])

        if check_delete is True:
            d_counter+=1

    else: # retrieve "r"
        check_retrieve = irs_list.retrieve(line[1])

        if check_retrieve is True:
            r_counter+=1


irs_list.printList()
irs_list.retrieve(760846483)
print(i_counter)
print(d_counter)
print(r_counter)
# TODO
#  modify the delete function in singlelinedlist1
# You are doing elif and else
