class Node: 
    def __init__(self, name, ssn):  
        self.name = name
        self.ssn = ssn
        self.next = None


# Single Linked List class
class SLL: 

	def __init__(self):
		self.headPtr = None
  
    # Insert a new node at the end of the linked list
	def insert(self, new_ssn, new_name):

		is_in_sll = self.retrieve(new_ssn) # this variable is going to be a true or false

		if is_in_sll is False: # YOu want to insert to data structure IFF it is not present in the list AFTER YOU HAVE SEAARCHED FOR IT

			new_node = Node(new_ssn, new_name)
			if self.headPtr is None:
				self.headPtr = new_node
				return
			last_entered = self.headPtr
			while(last_entered.next):
				last_entered = last_entered.next
			last_entered.next = new_node

			return True
		else: # It's already punched in, so return false because we didn't have to insert
			return False

	def delete(self, delete):

		# Search for ssn. store variable as "is_ssn_sll"
		# if is_ssn_sll is False
			# NOT DELETING so this function (delete) returns FALSE
		# else
			# It is in the list (retreive returned TRUE) this function (delete) also return TRUE
		is_ssn_sll = self.retrieve(delete)

		if is_ssn_sll is False:
			return False
		
		else:

			HeadVal = self.headPtr
		
			if HeadVal is not None:
				if HeadVal.ssn == delete:
					self.headPtr = HeadVal.next
					HeadVal = None
					return
		
			while HeadVal is not None:
				if HeadVal.ssn == delete:
					break
				prev = HeadVal
				HeadVal = HeadVal.next

			if HeadVal == None:
				return

			prev.next = HeadVal.next

			HeadVal = None

			return True
	
	# Searching to see if the ssn is punched in to the data structure. I return true if it;s present. Or else, it aint there so return false
	def retrieve(self, new_ssn):

		HeadVal = self.headPtr

		while HeadVal is not None:
			if(HeadVal.ssn is new_ssn):
				return True
			HeadVal = HeadVal.next
		
		return False
    

    # Delete a selected node, provided in the linked list

		


	# Print the list/Search for a node
	def printList(self):
		printPtr = self.headPtr
		while printPtr is not None:
			print(printPtr.ssn, printPtr.name)
			printPtr = printPtr.next


#SLL = SLL()
#
#SLL.insert(23194185, "Peter Fonda")
#SLL.insert(3131941, Jane Fonda)
#SLL.insert(14124913, "Hanna Fonda")
#SLL.delete(3131941)
#SLL.printList()