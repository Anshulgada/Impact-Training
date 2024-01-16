# A linked list is represented by a pointer to the first node of the linked list
# The first node is called of the head. If the LL is empty, then value of the head is NULL.
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

