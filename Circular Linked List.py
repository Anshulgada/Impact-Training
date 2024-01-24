class Node:                       # This class is only for Node creation
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLinkList:
    def __init__(self):
        self.head = None            # Created the head node

    def insertAtStart(self, data):
        new_Node = Node(data)           # Calling Node class to put that data in a new object

        if self.head is None:
            self.head = new_Node            # If head is empty then add it to head's reference
            new_Node.next = self.head
            return

        current = self.head
        while current.next != self.head:    # To reach Last Node
            current = current.next

        current.next = new_Node             # Updation of Nodes' addresses
        new_Node.next = self.head
        self.head = new_Node


    def insertAtEnd(self, data):
        new_Node = Node(data)           # Calling Node class to put that data in a new object

        if self.head is None:
            self.head = new_Node            # If head is empty then add it to head's reference
            new_Node.next = self.head
            return

        current = self.head
        while current.next != self.head:    # To reach Last Node
            current = current.next

        current.next = new_Node         # Once while loop is over, add new node to current as last node
        new_Node.next = self.head


    def insertAfterData(self, data, data_position):
        new_Node = Node(data)           # Calling Node class to put that data in a new object

        if self.head is None:
            print("Data position not found")
            return

        current = self.head
        while current:
            if current.data == data_position:       # To reach wanted data
                new_Node.next = current.next
                current.next = new_Node
                return
            current = current.next

            if current == self.head:
                break

        print("Data position not found")


    # def insertByPosition(self,data, user_position):




    def display(self):

        if self.head is not None:
            print(self.head.data)
            current = self.head.next

            while current is not self.head:     # Alternatively check current.next and print current.data
                print(current.data)             # Need to add edge if only 1 node exists, then no current.next case
                current = current.next          # Also edge case for last node as c.n == s.h, so it won't print tail
            return                              # To do so, first print then check c.n == s.h

        print("List is Empty")


obj = CircularLinkList()
obj.insertAfterData(60, 90)
obj.insertAtStart(40)
# obj.insertAfterData(60, 90)
obj.insertAtStart(30)
obj.insertAtStart(20)
obj.insertAtStart(10)
obj.insertAtEnd(50)
obj.insertAtEnd(70)
obj.display()