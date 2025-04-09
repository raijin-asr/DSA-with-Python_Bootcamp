# Introduction
"""
Normally, in a linked list, every node points to its next node.
head -> 80 -> 90 -> 100 -> None

However, we can also create a linked list where a node points to both its previous and next elements. This type of linked list is called a doubly linked list.

head <-> 80 <-> 90 <-> 100 <-> None

For convenience, we will also take reference to the last node, which we will call the tail node
"""

# Why Doubly Linked Lists?
"""
Imagine you're designing a text editor where users can enter and edit text.

Now, suppose you want to add the undo and redo options. This requires moving through the memory in both directions.

Unfortunately, singly linked lists only move in a single direction, i.e., forward:

head -> Edit1 -> Edit2 -> Edit3

As a result, we can't perform an undo operation using a singly linked list.

Instead, we need to start from scratch and go through each step, which results in O(n) time complexity and is thus not ideal.

There's a simple and elegant solution: the doubly linked list.

Each node points to the next and previous nodes, forming a two-way chain.

<-> Edit1 <-> Edit2 <-> Edit3 <-> 

This speeds up redo (O(1)) and undo (O(1))—a game-changer in real-time text edits.

Doubly linked lists find applications beyond text editors, including task scheduling, cache management, and doubly ended queue implementations.
"""

# Create a Doubly Linked List
"""
As we know, in a regular linked list:

Each node contains a reference to the next node.
The last node points to None.


To convert this regular linked list to a doubly linked list, we will:
1. Add reference to the previous node to each node.

2. Add a tail pointer.

A tail pointer is similar to the head pointer; it just points to the last node in the linked list.

After we have added the tail pointer, we will:
-Make the next pointer of tail point to None.
-Make the previous pointer of head point to None.
"""

# Thought Process: Create a Doubly Linked List
"""
To implement a doubly linked list, we'll modify our single linked list code by adding a reference to the previous node in each node in our Node class.
"""
class Node:
    def __init__(self, data):
        # initialize a node with
        # data and next pointer
        self.data = data
        self.next = None

        # add a prev pointer to
        # convert to doubly linked list
        self.prev = None

# Then, we'll add a tail pointer in our class to handle the list.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

# Traverse Doubly Linked List
"""
Traversing a doubly linked list is the same as traversing a singly linked list. You move node by node until you reach None.
The key distinction here from a regular linked list is that a doubly linked list can also be traversed backward. This is known as reverse traversal, which we'll discuss next.
"""

# Reverse Traverse a Doubly Linked List
"""
In reverse traversal, we start from the tail and traverse backward using prev until we reach None.
"""

# Thought Process: Traversal of a Doubly Linked List
"""
Let's implement methods to traverse a doubly linked list in both forward and reverse directions.

Forward Traversal
For forward traversal of a doubly linked list, we will:

1. Start from the 'head' node.
current = self.head

2. Loop until the node is 'None' by utilizing the 'next' pointer.

while current is not None:
    current = current.next

Reverse Traversal
For reverse traversal of a doubly linked list, we will:

1. Start from the 'tail' node.

current = self.tail
2. Loop until the node is 'None' by utilizing the 'prev' pointer.

while current is not None:
    current = current.prev
Now, we'll add these methods of traversal to our linked list and get a working implementation.
"""

# Source Code: Traversal
 #  traverse the linked list
def traverse(self):
    # start at head
    current = self.head
    print("None", end = " <-> ")
    # loop until the node is None
    while current is not None:
        print(f"{current.data} <-> ", end="") 
        current = current.next
    print("None")

# reverse traverse the linked list
def reverse_traverse(self):
    # start at tail
    current = self.tail
    print("None", end = " <-> ")
    # loop until node is None
    while current is not None:
        print(f"{current.data} <-> ", end="") 
        current = current.prev
    print("None")

# Output
# None <-> 80 <-> 9 <-> 14 <-> None
# None <-> 14 <-> 9 <-> 80 <-> None

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
