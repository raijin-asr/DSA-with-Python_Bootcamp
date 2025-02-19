# Introduction
"""
A linked list is a linear data structure that includes a series of connected elements. Each element of a linked list is called a node.

A node stores data and the address of the next node.
data | next
80   | -->

Here,
data - value of a node
next - address of the next node

Linked List
A linked list is a series of connected nodes.
data | next  -->  data | next  -->  data | next  -->  None
Head Node           A node            A node        Tail Node

The first node is the starting point of a linked list and is called the head of that linked list.
The address of the last node must point to None (null), as there are no elements after it.
"""

# Real-Life Analogy
"""
Imagine playing a game of Treasure Hunt, where you follow a trail of clues connecting one piece of information to the next until you finally reach the treasure.

A linked list is analogous to this trail of connected clues. And each clue (node) has

a piece of information (data)
a hint to find the next clue (address of the next node)
"""

# Create a Linked List
"""
Since a linked list is a collection of connected nodes, let's first learn to create nodes.

Create a Node
As mentioned before, a node stores data and the address of the next node.

  node
data | next
"""
# Let's implement a node in our Python code.
class Node:

    def __init__(self, data):   
        self.data = data
        self.next = None

# Here, the Node class has two fields:
    # data - to store the element
    # next - to store the address to the next node

# Note: We have initialized the value of next to None because, currently, there are no nodes after it.
# Now, we can create nodes and add data to them.

node1 = Node(11)
node2 = Node(2)
node3 = Node(88)

# Let's create a LinkedList class to implement linked lists.
class LinkedList:
    def __init__(self):
        # initialize the head field to None
        self.head = None

# Next, we will create a method to add nodes. For now, we will only add our first node to the linked list.
def create_linked_list(self):

    # create the first node
    node1 = Node(80)

    # set the head field to the first node
    self.head = node1
    
# At this point, our linked list looks like this:
# head -> 80 -> None


# Let's create the second node.
def create_linked_list(self):

    # create the first node
    node1 = Node(80)

    # set the head field to the first node
    self.head = node1

    # create the second node
    node2 = Node(9)

    # link the first and second nodes
    node1.next = node2

# Here, we have created a node named node2 with value 9. We then linked it with node1 by assigning node2 to the next field of node1.

# At this point, our linked list looks like this:

# head -> 80 -> 9 -> None

# Let's add the third node as well.
def create_linked_list(self):

    # create the first node
    node1 = Node(80)

    # set the head field to the first node
    self.head = node1

    # create the second node
    node2 = Node(9)

    # link the first and second nodes
    node1.next = node2

    # create the third node
    node3 = Node(14)

    # link the second and third nodes
    node2.next = node3

# This is how our linked list looks after adding three nodes.
# head -> 80 -> 9 -> 14 -> None

# Here,
# The head is the first node in the linked list.
# Each node is connected to each other.
# The last node points to None.

"""
Source Code: Create a Linked List
"""
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    # a linked list of three nodes:
    # 80->9->14
    def create_linked_list(self):
        # create and link nodes
        node1 = Node(80)
        self.head = node1

        node2 = Node(9)
        node1.next = node2

        node3 = Node(14)
        node2.next = node3

linked_list = LinkedList()

# create linked list
linked_list.create_linked_list()

"""Traverse Through the Linked List
"""

# Here are the steps involved in traversing a linked list:
# 1. Assign head to the current variable.
# get the address to the head of the list
current = self.head

# 2. Iterate until the current variable is None.
# iterate until current is None
# current is updated to the next node in each iteration
while current:
    current = current.next

# If current.next is None, we know for sure that it is the last node.


# Source Code: Traverse Through Linked List
# Let's add a method to our LinkedList class that will be used for traversal.
# method to traverse and print a linked list
def traverse_linked_list(self):
    current = self.head
    while current:
        print(f"{current.data}", end="->")
        current = current.next
    print(None)

# Output
# 80->9->14->None

"""
Problem 1: Create and Print a Linked List

Problem Description
Can you write a program to create a linked list and print it on your own?

-Create a Node class to initialize the data and next attributes of nodes.
-Create a LinkedList class to initialize the head attribute.
-Add the create_linked_list() method to the LinkedList class. This method will be used to add nodes to the linked list.
-Add another method, traverse_linked_list() to the LinkedList class. This method will be used to traverse and print the linked list.
"""

# Replace ___ with your code

# create the Node class
class Node:
     def __init__(self, data):
        self.data = data
        self.next = None


# create the LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None


    # method to create a linked list
    def create_linked_list(self):

        # take input for node data
        data1 = int(input())
        data2 = int(input())
        data3 = int(input())
        data4 = int(input())

        # create 4 nodes with input values
        node1 = Node(data1)
        node2 = Node(data2)
        node3 = Node(data3)
        node4 = Node(data4)

        # set head field to the first node
        self.head= node1

        # link the nodes
        node1.next = node2
        node2.next = node3
        node3.next = node4

    # method to traverse and print the nodes
    def traverse_linked_list(self):
        current = self.head
        while current:
            print(f"{current.data}", end="->")
            current = current.next
        print(None)


linked_list = LinkedList()

# create a linked list
linked_list.create_linked_list()

# print the linked list
linked_list.traverse_linked_list()

# Input 
# 10
# 20
# 30
# 40

# Your Output 
# 10->20->30->40->None

# Expected Output 
# 10->20->30->40->

"""
Example: Count Number of Nodes
In this example, we will count the number of nodes in a linked list.

To address this problem, we will traverse the linked list and increment a counter for each node we encounter
"""

# method to count elements in a linked list
def count_elements(self):
    current = self.head
    # initialize count to zero
    count = 0

    while current:
        #increment the count for each node encountered 
        count += 1
        # traverse to the next node
        current = current.next
# return count once all nodes are visited
    return count

# call count_elements and print the result
element_count = linked_list.count_elements()
print(f"Count = {element_count}")

# Output
# Count = 3

"""
Problem2:
Sum of All Elements in a Linked List

Problem Description
Write a program to find the sum of all nodes in a linked list.

-Create a Node class to represent a node.
-Create a LinkedList class to represent the linked list data structure.
-Within the LinkedList class, add the calculate_sum() method.
-The calculate_sum() method should compute the sum of all the nodes and return the result.
-Print the total sum outside of the classes.

Note: All necessary code, except for the calculate_sum() method, is provided for you in the editor.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def create_linked_list(self):
        data1 = int(input())
        data2 = int(input())
        data3 = int(input())

        node1 = Node(data1)
        node2 = Node(data2)
        node3 = Node(data3)

        self.head = node1
        node1.next = node2
        node2.next = node3

    # method to calculate the sum of nodes 
    def calculate_sum(self):
        sum = 0

        current = self.head
        while current:
            sum += current.data
            current = current.next

        return sum
    
# create a linked list
linked_list = LinkedList()
linked_list.create_linked_list()

# calculate the sum of elements
total = linked_list.calculate_sum()
print(total)

# Input 
# 9
# 1
# 1

# Your Output 
# 11

# Expected Output 
# 11