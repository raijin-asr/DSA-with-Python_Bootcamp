"""# Find the Largest Number in a Linked List

# The process of finding the largest value in a linked list is similar to how we find the largest number in a list.
# To find the largest value in a linked list, we start by assuming the first node's value is the largest.
# Then, we traverse through each node. As we go through the nodes, we compare each node's value with our current largest value and update the largest value if needed.

# Source Code"""

# method to return the largest number 
def find_largest(self):
    # condition to handle empty linked list
    if not self.head:
        return None
    
    current = self.head

    # initialize the value of head as largest
    largest = current.data

    # iterate until the last node
    while current:
        # update largest if necessary
        if current.data > largest:
            largest = current.data
        current = current.next
    return largest

# Output
# Linked List: 85->90->78->92->88->None
# Largest value: 

"""
# Example: Check if a Linked List is Sorted


To check if a linked list is sorted in ascending order, we need to traverse the list.
If the next node is smaller than the current node, we know the linked list is not sorted.
But if each node is smaller than the next node right until the end of the linked list, then it is sorted. 

Source Code:
"""
# method to check if a linked list is sorted 
def is_sorted(self):
    # empty linked list is considered sorted
    if not self.head:
        return True
    current = self.head
        
    # traverse the linked list
    while current.next:
        # if current node is greater than next
        # the linked list is unsorted
        if current.data > current.next.data:
            return False
        current = current.next
    return True

# Output
# Linked List: 3->5->2->12->16->None
# Is sorted?: False

"""
Remove Duplicates From a Sorted Linked List

Remove Duplicates From a Sorted Linked List

head
30 | | -> 55 | | -> 55 | | -> 80 | | -> 80 | | 80 | | -> None

After removal of duplicate values, the linked list should be:
30->55->80

To remove duplicates from a sorted linked list, we need to traverse the linked list and compare subsequent nodes.
If the current node and the next node have equal values, we will delete the next node.

Note: The nodes have been inserted in sorted order.

Source Code: Remove Duplicates From a Sorted Linked List
"""
# delete duplicate nodes from sorted list
def remove_duplicates(self):
    # condition to handle empty linked list
    if not self.head:
        return
    current = self.head 
    # traverse the linked list
    while current.next:
        # if current and next nodes are equal
        # delete the next node
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next 

# Output
# Original Linked List:
# 30->55->55->80->80->80->None

# After removing duplicates:
# 30->55->80->

"""
Reverse Elements of a Linked List

Suppose we are given a linked list. And we have to reverse the elements of the linked list.
head
2 | | -> 4 | | -> 6 | | -> 8 | | -> None 

In this case, the reversed linked list will look like this:

head
8 | | -> 6 | | -> 4 | | -> 2 | | -> None

Source Code: Reverse Elements of a Linked List
To reverse elements of a linked list, we will

Copy the values of the linked list to a new list.
Iterate through the new list in reverse order.
Assign the reversed values to the nodes of the linked list.
"""
def reverse_elements(self):
    # new list to copy the values
    values = []
    current = self.head

    # copy values of linked list to the new list
    while current:
        values.append(current.data)
        current = current.next
    
    current = self.head

    # iterate through the new list in reverse order
    for value in reversed(values):
        # copy the reversed value to the original list
        current.data = value
        current = current.next    

# Output

# Original Linked List:
# 2->4->6->8->None

# Reversed Elements:
# 8->6->4->2->None


"""
Reverse a Linked List

Suppose we are given a linked list, and we need to reverse it.

      node1     node2    node3     node4
head  -> 2 | | -> 4 | | -> 6 | | -> 8 | | -> None

Here's how a reversed linked list looks like:

        node1     node2    node3     node4
head  -> 8 | | -> 6 | | -> 4 | | -> 2 | | -> None

The data of the linked list will remain the same. However, they will point to its preceding node, instead of pointing to their succeeding node.

Reminder: In the previous example, we reversed the elements of the linked list. Here, we are reversing the linked list itself.

For that, we could point the next pointer of node 2 to node 1.

head -> 2 | | <- 4 | | -> 6 | | -> 8 | | -> None
        ^  -  -  -  |

As you can see, there is no reference to node 3. Now, the linked list is not accessible from node 3.

To solve this, we can use the sliding references technique. Next, we will see how the sliding pointer works.
"""

"""
As you can see, there is no reference to node 3. Now, the linked list is not accessible from node 3.

To solve this, we can use the sliding references technique. Next, we will see how the sliding pointer works.
1. Start by setting three references.

previous = None
current = self.head
next_node = current.next

2. Move to the succeeding nodes.
prev_node = current
current = next_node
next_node = next_node.next

Since multiple references slide or move together in a coordinated manner; they are called sliding references.
"""

# Reverse Linked List
# To reverse a linked list, we will use the following steps.

# 1. Create three references.
prev_node = None
current = self.head
next_node = current.next

# 2. Make the current node point to its preceding node.
current.next = prev_node

# 3. Slide the references.
prev_node = current
current = next_node
next_node = next_node.next

# 4. Repeat Steps 2 and 3 until the subsequent node of the current node points to None.
while True:
    # Step 2 and 3

    if next_node == None:
        current.next = prev_node
        break

# 5. Make the current node the new head node.
self.head = current

# Source Code: Reverse a Linked List
# reverse linked list
def reverse_linked_list(self):

    prev_node = None
    current = self.head
    next_node = current.next

    while True:

        current.next = prev_node
                
        prev_node = current
        current = next_node
        next_node = next_node.next
                
        if next_node == None:
            current.next = prev_node
            break

    self.head = current

# Output
# Original Linked List:
# 2->4->6->8->None

# Reversed Linked List:
# 8->6->4->2->None