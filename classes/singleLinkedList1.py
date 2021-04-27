class Node: 
    def __init__(self, name, ssn):  
        self.name = name
        self.ssn = ssn
        self.next = None


# Single Linked List class
class SLL: 

	def __init__(self):
		self.headPtr = None
		self.size_i = 0
		self.size_d = 0
		self.size_r = 0

	def get_size_i(self):
		return self.size_i

	def get_size_d(self):
		return self.size_d

	def get_size_r(self):
		return self.size_r
    
    # Insert a new node at the end of the linked list
	def insert(self, new_name, new_ssn):
		new_node = Node(new_name, new_ssn)
		if self.headPtr is None:
			self.headPtr = new_node
			return
		last_entered = self.headPtr
		while(last_entered.next):
			last_entered = last_entered.next
		last_entered.next = new_node
		self.size_i += 1

    

    # Delete a selected node, provided in the linked list
	def delete(self, delete):
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

		self.size_d += 1
		


	# Print the list/Search for a node
	def printList(self):
		printPtr = self.headPtr
		while printPtr is not None:
			print(printPtr.ssn, printPtr.name)
			printPtr = printPtr.next
		self.size_r += 1

SLL = SLL()

SLL.insert("Peter Fonda", 23194185)
SLL.insert("Jane Fonda", 3131941)
SLL.insert("Hanna Fonda", 14124913)
SLL.delete(14124913)
SLL.printList()