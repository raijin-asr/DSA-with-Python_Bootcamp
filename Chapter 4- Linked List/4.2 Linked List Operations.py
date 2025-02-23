# Operations in Linked List

# 1. Inserting into a linked list
# 2. Deleting from a linked list

# Insert Into a Linked List
"""
We can insert a node at any position in a linked list. In general, there are three cases for node insertion.

Insert a node at the end of a linked list (append).
Insert at the beginning of a linked list.
Insert at any given position.
Let's see how we can append a node to a linked list.
"""

# Insert Node at the End (Append)
"""Suppose we have the following linked list:

head -> 80 | | -> 9 | | -> 14 | | -> None

Append a Node
Let's append a node with the data 20 to the linked list we previously mentioned. Here's how we can do it:

1. Create a new node.
We will use the Node class we discussed in the previous lesson to create a new node.

new_node = Node(20)

data next
20 -> None

2. Traverse until the last node of the linked list is reached.
Since we need to insert a node at the end, we must traverse until we reach the last node. We will add the new node after the last node.
# code snippet to find the last node
# current variable points to the head node
current = self.head

# traverse until the last node (node pointing to None)
while current:
    current = current.next
        
        Current
head -> 80 | | -> 9 | | -> 14 | | -> None
                  Current
head -> 80 | | -> 9 | | -> 14 | | -> None
                           Current
head -> 80 | | -> 9 | | -> 14 | | -> None

3. Add a new node after the last node (current node).
current.next = new_node

head -> 80 | | -> 9 | | -> 14 | | -> 20 | | -> None
"""
# Append Element to an Empty Linked List
""""
The code we discussed for appending to a linked list does not work if the linked list is empty.

If you recall the LinkedList class we introduced in the previous lesson, its head attribute is initially set to None.

class LinkedList:
    def __init__(self):
        self.head = None
This means that the head attribute of an empty linked list is None.

Therefore, to append a new node to an empty linked list, we will simply set head to point to new_node.

if not self.head:
    self.head = new_node
    return

head -> 10 | | -> None
"""

# Source Code: Append a Node
# method to append a node at the end
def append_node(self, data):
    new_node = Node(data)
    if not self.head:
        self.head = new_node
        return

    current = self.head
    while current.next:
        current = current.next
    current.next = new_node

# Output
# Original Linked List:
# 80->9->14->None

# After appending 20:
# 80->9->14->20->None

"""
Insert at the Beginning of the Linked List

Suppose we have the following linked list

head -> 8 | | -> 3 | | -> 9 | | -> 7 | | -> 6| | -> None

Here's how you can insert a node (10) at the beginning of a linked list.

1. Create a new node.
new_node = Node(10)

data next
10 -> None

2. Link the new node to the head node.
new_node.next = self.head

head -> 8 | | -> 3 | | -> 9 | | -> 7 | | -> 6 | | -> None
        new_node
        data next
        10 -> None

3. Make the new node the starting node (the head).
self.head = new_node
"""

# Source Code: Insert at the Beginning

# method to insert a node at the beginning
def insert_node_at_beginning(self, data):

    # create a new node
    new_node = Node(data)

    # link new_node to the head node
    new_node.next = self.head

    # make new_node the head node
    self.head = new_node

# Output
# Original Linked List:
# 80->9->14->None

# After inserting 10 at beginning:
# 10->80->9->14->None

"""
Add Node at the Beginning

Problem Description
Can you write a program to add a node at the beginning of an existing linked list?

Add the insert_node() method to the LinkedList class, following the outline provided in the editor.
The insert_node() method should insert a node at the beginning of the linked list.
Then, print the linked list by calling the display() method.
For example,

The starting linked list will always be:

90->80->60->50
If you insert a new node with data 12, the linked list should become:

12->90->80->60->50
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # create the linked list: 90->80->60->50
    def create_linked_list(self):
        node1 = Node(90)
        node2 = Node(80)
        node3 = Node(60)
        node4 = Node(50)

        self.head = node1
        node1.next = node2
        node2.next = node3
        node3.next = node4

    #  method to insert a node at the beginning
    def insert_node_at_beginning(self, data):
        # write your code here
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node



     # traverse the list
    def display(self):
        current = self.head
        while current:
            print(f"{current.data}", end="->")
            current = current.next
        print(None)

linked_list = LinkedList()

# create the initial linked list
linked_list.create_linked_list()

# input for data to append
data = int(input())
linked_list.insert_node_at_beginning(data)

# print the updated linked list
linked_list.display()   


"""
Insert Node at the Given Position

"""