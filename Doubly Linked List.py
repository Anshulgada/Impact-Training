# Doubly Linked List has ref to both the previous and the next node
# Therefore it has a head and a tail

class Node:                       # This class is only for Node creation
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkList:
    def __init__(self):
        self.head = None
        self.tail = None

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

    def insertAtPosition(self,position,data):
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