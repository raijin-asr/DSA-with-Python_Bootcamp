# Examples: Circular Linked List
"""
You can also perform other operations in a circular linked list. Some of them are:

Find the maximum value in a circular linked list.
Reverse a circular linked list.
Search in a circular linked list.
"""

# Find Maximum in a Circular Linked List
"""
Suppose we have to find the maximum of the following circular linked list:
22->88->66->33

The output should be
88

Thought Process
To find the maximum of a circular linked list, follow the approach below.

1. Start with the head node and assume it is the maximum.
current = head
maximum = head.data

2. Move to the next node and compare with the current maximum. If the node's data is greater than the current maximum, change the maximum value.

current = current.next
if current.data > maximum:
    maximum = current.data

3. Repeat the process until you reach the head node again.

while current.next is not self.head:
    current = current.next
"""

# Source Code: Find Maximum in a Circular Linked List
def find_max(self):
    # empty circular linked list has no head
    if not self.head:
        return None

    # start with head
    current = self.head
    # assign first value as maximum
    maximum = current.data

    while current.next is not self.head:
        current = current.next
        if current.data > maximum:
            maximum = current.data

    return maximum

# Output
# 22 -> 88 -> 66 -> 33 -> 22
# Maximum Value: 88

# Reverse a Circular Linked List
"""
Suppose we have to reverse the following list:
11->22->33->44

To reverse a circular linked list, you can follow these steps.
1. Create three references.
prev_node = None
current = self.head
next_node = current.next

2. Make the current node point to its preceding node.
current.next = prev_node

3. Slide the references.
prev_node = current
current = next_node
next_node = current.next

4. Repeat Steps 2 and 3 until you reach the head node again.
while True:
    # step 2 and 3

    if current == self.head:
        break
"""

# Source Code: Reverse a Circular Linked List
# reverse method
def reverse(self):
    # in case of 0 or 1 elements, no need to reverse
    if self.node_count() < 2:
        return
    
    # define 3 pointers
    prev_node = None
    current = self.head
    next_node = current.next
    
    while True:
        
        # assign next pointer of current to previous node
        current.next = prev_node
        
        # slide the pointers
        prev_node = current
        current = next_node
        next_node = current.next
        
        # repeat until you reach head again
        if current == self.head:
            break
    
    # adjust head
    self.head.next = prev_node
    self.head = prev_node   
  

# Output
# Original Linked List:
# 3 -> 6 -> 9 -> 12 -> 15 -> 3

# Linked List After Reversal:
# 15 -> 12 -> 9 -> 6 -> 3 -> 15

# Search in a Circular Linked List
"""
Suppose we have to search in the following list.
head 11->22->33->44

Let's look at the thought process of searching in this circular linked list.

Thought Process - Case1: Value in List
Let us search for 33.

1. Start at the head node.
current = self.head

2. Loop until the node is found.
while True:
    current = current.next
    if current.data == 33
        return True

If the Value is Not in the List
If the value is not in the list, we stop the loop after we reach the head again. This implies that we have traversed all nodes, and we didn't find the value.

while True:
    current = current.next
    if current == self.head
        return False
"""

# Source Code: Searching in a Circular Linked List
# search method
def search(self, value):
    current = self.head
    
    while True:
        # move to next
        current = current.next
        # True if value is found
        if(current.data == value):
            return True
        # False if loop is complete
        if(current == self.head):
            return False
        
# Output

# Element 33 is found in the circular linked list.
# Element 55 is not found in the circular linked list.
# This marks the end of circular linked lists. Next, we move on to doubly linked lists.