# Examples: Doubly Linked List
"""
You can also perform other operations in a doubly linked list. Some of them are:

Reverse a doubly linked list.
Check if the given list is a palindrome.
"""
# Reverse a Doubly Linked List
"""
1. Start from the 'head' node.
current = self.head

2. Swap the 'prev' and the 'next' pointers.
current.prev, current.next = current.next, current.prev

3. Move to the new 'prev' node.
current = current.prev

4. Repeat Steps 2 and 3 until you reach the end of the list.
while True:
    # Step 2 and 3

    if current is None:
        break

5. Swap the 'head' and 'tail' node.
self.head, self.tail = self.tail, self.head
"""

# Source Code: Reverse Doubly Linked List
def reverse(self):
    
    # no need to reverse in case of 0 or 1 nodes
    if self.length() < 2:
        return
    
    # start from head
    current = self.head
    while True:
        # swap previous and next node pointers
        current.prev, current.next = current.next, current.prev
        
        # move to the new previous node
        current = current.prev
        
        # repeat until you reach None
        if current == None:
            break
        
    # swap head and tail
    self.head, self.tail = self.tail, self.head

"""
Output

Original Linked List:
None <-> 11 <-> 22 <-> 33 <-> 44 <-> None

Reversed Linked List:
None <-> 44 <-> 33 <-> 22 <-> 11 <-> None
"""

# Check Palindrome
"""
1. Get references to both the 'head' and 'tail' nodes.
start = self.head
end = self.tail

2. If the data doesn't match, return False.
if start.data != end.data:
    return False

3. Move forward from 'head' and backward from 'tail.'
start = start.next
end = end.prev

4. Repeat until the end is no longer after start.
while start != end and start.prev != end:
    if(start == end or start == end.next):
        return True
"""

# Source Code: Check Palindrome
# check if list is palindrome
def is_palindrome(self):
    # palindrome doesn't apply
    # for empty linked lists
    if not self.head:
        return False
    
    # get reference to both head and tail
    start = self.head
    end = self.tail

    while start != end and start.prev != end:
        # return False if data don't match
        if start.data != end.data:
            return False
        # move forward from head
        # and backward from tail
        start = start.next
        end = end.prev
        # repeat until end is
        # no longer after start
        if(start == end or start == end.next):
            return True

# Output

# None <-> 10 <-> 80 <-> 80 <-> 10 <-> None
# The list is a palindrome.