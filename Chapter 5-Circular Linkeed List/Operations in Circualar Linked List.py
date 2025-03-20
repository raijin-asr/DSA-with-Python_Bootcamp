# Operations in Circular Linked Lists
"""
Similar to linked lists, circular linked lists support several common operations. Let's take a look at each of them:

1. Insert
-Insert at the beginning of a circular linked list.
-Insert at the end of a circular linked list.
-Insert at any given position in a circular linked list.

2. Delete
-Delete from the beginning of a circular linked list.
-Delete from any given position in a circular linked list.
"""

# Insert Into Linked List
"""
We can insert a node at any position in a linked list. There are three cases for node insertion.
--Insert node at the end of the linked list (append).
--Insert at the beginning of the linked list.
--Insert at any given position.

Let's begin by inserting it at the end of a linked list."""

# Append an Element to a Circular Linked List
"""
To append an element to a circular linked list, we follow the steps below:

1. Traverse to the last node of the linked list.
2. Point the next pointer of the last node to the new node.
3. Make the new node point to the head node.
"""

# Append Element in an Empty Linked List
"""
There might also be cases where there are no elements in a linked list. That means there is a head node pointing to None.

In that case, we will simply mark the new node as the head, and then make that node point to itself.
"""

# Code: Append Element
# So, our helper function to append an element to a linked list will look like this:
def append_into_empty(self, data):
    new_node = Node(data)
    self.head = new_node
    new_node.next = self.head

def append_node (self, data):
    # create a new node
    new_node = Node(data)

    # traverse to the end of the list
    current = self.head
    while current.next != self.head:
        current = current.next

    # adjust the next pointers
    current.next = new_node
    new_node.next = self.head

# Insert at the Beginning
"""
Imagine we have the following list.

head 
8 | | -> 3 | | -> 9 | | -> 7 | | -> 6 | |
^______________________________________|
Figure: Example of Circular Linked List

Suppose we need to insert a node 10 at the beginning, we follow the given steps:
1. Traverse the list and make the last node point to the new node.

head
8 | | -> 3 | | -> 9 | | -> 7 | | -> 6 | | -> 10 | |

10 | | new_node                                  |
^________________________________________________|

2. Make the new node point to the head node and then make it the new head node.

8 | | -> 3 | | -> 9 | | -> 7 | | -> 6 | | -> 10 | |
^
|_____
head  |                                            |
10  |  |
^__________________________________________________|
"""

# Code: Insert at the Beginning
# insert at the beginning of the linked list
def insert_at_beginning(self, data):

    # create a new node
    new_node = Node(data)

    # traverse the linked list
    current = self.head
    while current.next != self.head:
        current = current.next

    # update the next pointers
    current.next = new_node
    new_node.next = self.head

    # update the head attribute
    self.head = new_node

# Insert at a Given Position
"""
Suppose we have the following linked list.
head
8 | | -> 3 | | -> 9 | | -> 7 | | -> 6 | |

To insert a new node 11 at the fifth position, we perform the following steps.

1. Traverse from the head node to the node at the 4th position (i.e., position - 1).
        current
head -> 8 | | -> 3 | | -> 9 | | -> 7 | | -> 6 | |
                current
head -> 8 | | -> 3 | | -> 9 | | -> 7 | | -> 6 | |

                        current
head -> 8 | | -> 3 | | -> 9 | | -> 7 | | -> 6 | |

                                current
head -> 8 | | -> 3 | | -> 9 | | -> 7 | | -> 6 | |

2. Make the new node point to the next node of the current node.
                                            new_node
head                                current  | 
8 | | -> 3 | | -> 9 | | -> 11 | | -> 7 | | -> 6 | |

3. Make the next pointer of the current node point to the new node.

head                                        ->new_node -|
8 | | -> 3 | | -> 9 | | -> 11 | | -> 7 | | -|            -> 6 | |
"""

# Code: Insert at Given Position
# So, our helper function to insert nodes at a given position will look like this:
def insert_at_position(self, data, position):
    # create a new node
    new_node = Node(data)

    current = self.head

    # bring a pointer to position - 1
    # assign it to the current variable
    for i in range(1, position-1):
        current = current.next

    # make the new node point to
    # the next node of the current node
    new_node.next = current.next

    # make next pointer of current
    # point to the new node
    current.next = new_node

# Source Code: Insert Elements in a Circular Linked List
def insert_node(self, data, position=None):
    if not self.head:
        self.append_into_empty(data)
    elif not position or position == self.length() + 1:
        self.append_node(data)
    elif position == 1:
        self.insert_at_beginning(data)
    else:
        self.insert_at_position(data, position)

# Output

# Original Linked List: 5 -> 5 
# Linked List After Inserting 10 at the Beginning: 10 -> 5 -> 10 
# Linked List After Inserting 15: 10 -> 5 -> 15 -> 10 
# Linked List After Inserting 20: 10 -> 5 -> 20 -> 15 -> 10

# In the above program, we implemented all the helper methods we have learned so far to insert a node.
# Then, we incorporated these helper methods into a single method named insert_node() to handle all cases of insertion.

# Delete From the Linked List
"""
We can delete a node at any position in a circular linked list. There are two cases for node deletion:

Delete the first node.
Delete a node at a given position.
"""

# Delete the First Node
"""
Deleting the first node in a linked list is a special case. This is because the first node is the head node of the linked list. And the only way to access the linked list is through the head node.
So suppose we have a linked list like this:

head
8 | | -> 3 | | -> 9 | | -> 7 | | -> 6 | |

To delete the first node (i.e., 8) from this linked list, we perform the following steps:
1. Get reference to the head node.
temp = self.head
      temp
head -> 8 | | -> 3 | | -> 9 | | -> 7 | | -> 6 | |

2. Get reference to the last node.

current = self.head
while current.next is not self.head:
    current = current.next

      temp                                current
head -> 8 | | -> 3 | | -> 9 | | -> 7 | | -> 6 | |

3. Move the head to the second node.
self.head = self.head.next

3. Move the head to the second node.
temp    head                      current
8 | | -> 3 | | -> 9 | | -> 7 | | -> 6 | |
^______________________________________|
4. Make the last node point to the new head node.
current.next = self.head

temp    head
8 | | -> 3 | | -> 9 | | -> 7 | | -> 6 | |
        ^_______________________________|
"""

# Code: Delete First Node
# Here's our helper function to delete the first node

def delete_from_beginning(self):
    # get a reference to head
    temp = self.head
    current = self.head

    # get a reference to the last node
    while current.next is not self.head:
        current = current.next

    # shift head to second node    
    self.head = self.head.next

    # adjust the next pointer of the last node to the new head
    current.next = self.head

# Delete From a Circular Linked List With a Single Node
