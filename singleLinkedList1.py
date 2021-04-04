


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
            n = self.headPtr
            while n is not None:
                print (n.value, " ")
                n = n.next

    def insert_at_start(self, number):
        new_node = Node(number)
        new_node.next = self.headPtr
        self.headPtr= new_node

    def insert_at_end(self, number):
        new_node = Node(number)
        if self.headPtr is None:
            self.headPtr = new_node
            return
        n = self.headPtr
        while n.next is not None:
            n= n.next
        n.next = new_node

    def insert_after_value(self, x, number):
        n = self.headPtr
        print(n.next)
        while n is not None:
            if n.value == x:
                break
            n = n.next
        if n is None:
            print("value not in the list")
        else:
            new_node = Node(number)
            new_node.next = n.next
            n.next = new_node

    def insert_before_value(self, x, number):
        if self.headPtr is None:
            print("List has no element")
            return

        if x == self.headPtr.value:
            new_node = Node(number)
            new_node.next = self.headPtr
            self.headPtr = new_node
            return

        n = self.headPtr
        print(n.next)
        while n.next is not None:
            if n.next.value == x:
                break
            n = n.next
        if n.next is None:
            print("value not in the list")
        else:
            new_node = Node(number)
            new_node.next = n.next
            n.next = new_node

    def insert_at_index(self, index, number):
        if index == 1:
            new_node = Node(number)
            new_node.next = self.headPtr
            self.headPtr = new_node
        i = 1
        n = self.headPtr
        while i < index-1 and n is not None:
            n = n.next
            i = i+1
        if n is None:
            print("Index out of bound")
        else: 
            new_node = Node(number)
            new_node.next = n.next
            n.next = new_node


    def get_count(self):
        if self.headPtr is None:
            return 0
        n = self.headPtr
        count = 0
        while n is not None:
            count = count + 1
            n = n.next
        return "The count is " + str(count) + "."
    
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

        n = self.headPtr
        while n.next.next is not None:
            n = n.next
        n.next = None

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

    def reverse_linkedlist(self):
        prev = None
        n = self.headPtr
        while n is not None:
            next = n.next
            n.next = prev
            prev = n
            n = next
        self.headPtr = prev


print("-------- WELCOME PEEPS ---------")
testList = SingleLinkedList()
testList.insert_at_start(5)
testList.insert_at_end(10)
testList.insert_after_value(5, 4)
testList.insert_before_value(10, 12)
testList.insert_at_index(3, 8)
testList.traverse_list()
##print(testList.get_count())
##testList.search_value(10)
##print(testList.make_new_list())
##testList.delete_at_start()
##testList.traverse_list()
##print(testList.get_count())
##testList.delete_at_end()
##testList.traverse_list()
##print(testList.get_count())
testList.delete_element_by_value(8)
testList.traverse_list()
##print(testList.get_count())
#testList.reverse_linkedlist()
#testList.traverse_list()