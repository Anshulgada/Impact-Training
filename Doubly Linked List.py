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