class Node:
    # This class provides a generic node for a linked list. 
    def __init__(self, number):
        self.value = number #number element
        self.next = None #pointer

class SingleLinkedList:
    # Constructor
    def __init__(self):
        self.headPtr = None
    #
    def traverse_list(self):
        if self.headPtr is None:
            print("List has no element")
            return
        else:
            iterative_node= self.headPtr
            while iterative_node is not None:
                print (iterative_node.value, " ")
                iterative_node = iterative_node.next

    def insert_at_start(self, number):
        new_node = Node(number)
        new_node.next = self.headPtr
        self.headPtr= new_node

    def insert_at_end(self, number):
        new_node = Node(number)
        if self.headPtr is None:
            self.headPtr = new_node
            return
        iterative_node = self.headPtr
        while iterative_node.next is not None:
            iterative_node = iterative_node.next
        iterative_node.next = new_node

    def insert_after_value(self, x, number):
        iterative_node = self.headPtr
        print(iterative_node.next)
        while iterative_node is not None:
            if iterative_node.value == x:
                break
            iterative_node = iterative_node.next
        if iterative_node is None:
            print("value not in the list")
        else:
            new_node = Node(number)
            new_node.next = iterative_node.next
            iterative_node.next = new_node

    def insert_before_value(self, x, number):
        if self.headPtr is None:
            print("List has no element")
            return

        if x == self.headPtr.value:
            new_node = Node(number)
            new_node.next = self.headPtr
            self.headPtr = new_node
            return

        iterative_node = self.headPtr
        print(iterative_node.next)
        while iterative_node.next is not None:
            if iterative_node.next.value == x:
                break
            iterative_node = iterative_node.next
        if iterative_node.next is None:
            print("value not in the list")
        else:
            new_node = Node(number)
            new_node.next = iterative_node.next
            iterative_node.next = new_node

    def insert_at_index(self, index, number):
        if index == 1:
            new_node = Node(number)
            new_node.next = self.headPtr
            self.headPtr = new_node
        i = 1
        iterative_node = self.headPtr
        while i < index-1 and iterative_node is not None:
            iterative_node = iterative_node.next
            i = i+1
        if iterative_node is None:
            print("Index out of bound")
        else: 
            new_node = Node(number)
            new_node.next = iterative_node.next
            iterative_node.next = new_node


    def get_count(self):
        if self.headPtr is None:
            return 0
        iterative_node = self.headPtr
        count = 0
        while iterative_node is not None:
            count = count + 1
            iterative_node = iterative_node.next
        return "The count is " + str(count) + "."
    
    def search_value(self, x):
        if self.headPtr is None:
            print("List has no elements")
            return
        iterative_node = self.headPtr
        while iterative_node is not None:
            if iterative_node.value == x:
                print("value found")
                return True
            iterative_node = iterative_node.next
        print("value not found")
        return False


    def make_new_list(self):
        nums = int(input("How many nodes do you want to create: "))
     
        if nums == 0:
            return
        for i in range(nums):
            i = int(input("Enter the value for the node:"))
            self.insert_at_end(i)

    def delete_at_start(self):
        if self.headPtr is None:
            print("The list has no element to delete")
            return 
        self.headPtr = self.headPtr.next

    def delete_at_end(self):
        if self.headPtr is None:
            print("The list has no element to delete")
            return

        iterative_node = self.headPtr
        while iterative_node.next.next is not None:
           iterative_node = iterative_node.next
        iterative_node.next = None

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

    def reverse_linkedlist(self):
        prev = None
        iterative_node = self.headPtr
        while iterative_node is not None:
            next = iterative_node.next
            iterative_node.next = prev
            prev = iterative_node
            iterative_node= next
        self.headPtr = prev


#print("-------- WELCOME PEEPS ---------")
#testList = SingleLinkedList()
#testList.insert_at_start(5)
#testList.insert_at_end(10)
#testList.insert_after_value(5, 4)
#testList.insert_before_value(10, 12)
#testList.insert_at_index(3, 8)
#testList.traverse_list()
#print(testList.get_count())
#testList.search_value(10)
#print(testList.make_new_list())
#testList.delete_at_start()
#testList.traverse_list()
#print(testList.get_count())
#testList.delete_at_end()
#testList.traverse_list()
#print(testList.get_count())
#testList.delete_element_by_value(8)
#testList.traverse_list()
#print(testList.get_count())
#testList.reverse_linkedlist()
#testList.traverse_list()