# A linked list is represented by a pointer to the first node of the linked list
# The first node is called of the head. It only has reference (No Data).
# If the LL is empty, then value of the head is NULL.

# Each node in a list consists of at least 2 parts:
# 1. Data
# 2. Pointer (or Reference) to the next node in the linked list

# To DELETE the last node from the linked list ==>
# Delete the address of the previous node and set it to NULL.
# This way the node with that address is sent to the garbage collector.

# To DELETE the first node from the linked list ==>
# Change the address of the head node to next address, hence deleting the first node.

# To DELETE a middle node from the linked list ==>
# Change the address of the prev node to next address.
# Also change the address of the delete node to NULL.


class Node:                       # This class is only for Node creation
    def __init__(self,data):
        self.data = data
        self.next = None

# obj = Node(10)        # Creating a new node with value

class LinkList:
    def __init__(self):
        self.head = None            # Created the head node


    def insertAtStart(self, data):
        new_Node = Node(data)           # Calling Node class to put that data in a new object

        # if not self.head:               # Alternate method to not use else loop
        #     self.head = new_Node
        #     return                      # Just use return so it exits the for loop
        # new_Node.next = self.head       # Use else block as normal so if for loop is not used
        # self.head = new_Node            # So no return & hence these 2 lines execute

        if self.head is None:
            self.head = new_Node        # If head is empty then add it to head's reference

        else:
            new_Node.next = self.head   # Else add ref which head already has of old node to new node
            self.head = new_Node        # Then add new node's ref to head, so it is added in the beginning



    def insertAtEnd(self, data):
        new_Node = Node(data)

        if self.head is None:
            self.head = new_Node

        else:
            current = self.head         # Current gets the head's reference

            # We used current.next in while loop as we want to check if next node is present or not in the LL
            while current.next:           # Iterate over the nodes till you reach last node This way you can reach
                current = current.next    # the end of the LL So once we are at the end we basically just append the new node

            current.next = new_Node       # Once while loop is over, add new node to current as last node



    def insertAnywhere(self, position, data):
        new_Node = Node(data)

        if not self.head:
            self.head = new_Node
            return

        current = self.head
        while current:
            if current.data == position:
                new_Node.next = current.next
                current.next = new_Node
            current = current.next



    def deleteAtStart(self):
        if not self.head:
            print("List is empty")
        else:
            current = self.head
            self.head = current.next



    def deleteLast(self):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None



    def deleteAnywhere(self, position):
        if not self.head:
            print("List is empty")
            return

        current = self.head
        while current is not None and current.next.data is not position:    # Error when data not in LL
            current = current.next
        if current is not None:
            current.next = current.next.next
        else:
            print("Given data is not present in list")



    def display(self):
        current = self.head         # Current gets the head's reference

        while current:                      # While current is pointing to a node
            print(current.data)             # print data we have stored
            current = current.next          # Iterate to next


obj = LinkList()        # Creating a new node with LinkList class which uses Node class
print("\nInsertion ==>")
obj.insertAtStart(10)   # Inserting node at the beginning
obj.insertAtEnd(12)     # Inserting node at the end
obj.insertAnywhere(10, 11)
obj.display()           # Use display func to print the nodes
print("\nDeletion ==>")
obj.deleteAtStart()
obj.deleteLast()
obj.deleteAnywhere(15)
obj.display()