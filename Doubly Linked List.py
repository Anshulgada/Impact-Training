# Doubly Linked List has ref to both the previous and the next node
# Therefore it has a head and a tail

class Node:                       # This class is only for Node creation
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkList:
    def __init__(self):
        self.head = None        # Created the head node
        self.tail = None        # Created the tail node

    def insertAtStart(self, data):
        new_Node = Node(data)           # Calling Node class to put that data in a new object

        if not self.head:
            self.head = new_Node
            self.tail = new_Node
            return                      # Just use return so it exits the function loop
        self.head.prev = new_Node
        new_Node.next = self.head       # Use else block as normal so if for loop is not used
        self.head = new_Node            # So no return & hence these 3 lines execute

    def insertAtEnd(self, data):
        new_Node = Node(data)           # Calling Node class to put that data in a new object

        if not self.head:
            self.head = new_Node
            self.tail = new_Node
        else:
            self.tail.next = new_Node
            new_Node.prev = self.tail
            self.tail = new_Node

    def insertAtPosition(self, position, data):
        new_Node = Node(data)

        if position == self.tail.data:      # To check if position of data is last, then add new Node in the end
            self.tail.next = new_Node
            new_Node.prev = self.tail       # These lines ar e to update the prev & next refs and tail's refs
            self.tail = new_Node
            return

        current = self.head
        while current and current.data != position:     # Loop through all nodes
            current = current.next

        if not current:                 # If data not found run this loop and then exit function with return
            print("Data not found")
            return

        new_Node.next = current.next    # Actual insertion if position is found
        new_Node.prev = current
        current.next.prev = new_Node
        current.next = new_Node


    def deleteStart(self):
        if not self.head:
            print("List is empty")
            return

        self.head = self.head.next      # Point head to 2nd Node
        self.head.prev = None           # Point prev of 2nd to None (To remove 1st node from backward reference)



    def deleteEnd(self):
        if not self.head:
            print("List is empty")
            return

        self.tail = self.tail.prev      # Point Tail to 2nd Last Node
        self.tail.next = None           # Point next of 2nd Last to None (To remove Last node from forward reference)


    def deleteByData(self, data):

        if self.head.data == data:
            self.deleteStart()
            return

        if self.tail.data == data:
            self.deleteEnd()
            return

        position = 1
        current = self.head.next
        while current and position != data:     # Loop through all nodes
            current = current.next

        if not current:                 # If data not found run this loop and then exit function with return
            print("Data not found")
            return


    def deleteByPosition(self, user_position):
        position = 1
        if user_position == 1:              # Head case
            self.deleteStart()
            return


        current = self.head
        while current  and position != user_position:
            position += 1
            current = current.next

        if current:
            if current.next is None:        # Tail case
                self.deleteEnd()
                return

            current.prev.next = current.next        # Middle case
            current.next.prev = current.prev
            return

        print("Index not found")

    def display(self):
        current = self.head         # Current gets the head's reference

        while current:                      # While current is pointing to a node
            print(current.data)             # print data we have stored
            current = current.next          # Iterate to next

    def display_backwards(self):
        current = self.tail         # Current gets the tail's reference

        while current:                      # While current is pointing to a node
            print(current.data)             # print data we have stored
            current = current.prev          # Iterate to previous

    def count_nodes(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count


obj = DoublyLinkList()        # Creating a new node with LinkList class which uses Node class

print("\nInsertion ==>")

obj.insertAtEnd(1)     # Inserting node at the end
obj.insertAtEnd(2)
obj.insertAtEnd(3)
obj.insertAtEnd(4)
obj.insertAtEnd(5)
obj.display()           # Use display func to print the nodes
print("\n")
# obj.display_backwards()   # Works properly

print("\nTotal Nodes ==>", obj.count_nodes())

print("\nDeletion ==>")

obj.deleteByPosition(5)
obj.display()


# Question ==>
#     If input contains zeros, add them to the end
#  Logic ==>
#     If zero comes in while loop, increase counter and continue iteration
#     Add zeros to the end as per counter count