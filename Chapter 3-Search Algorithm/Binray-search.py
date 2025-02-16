# Introduction
"""
Similar to linear search, binary search is used to find an element within a list.

However, unlike linear search, binary search can only be implemented in a sorted list. If the elements in the list are unsorted, we need to sort the elements first.
"""

# Thought Process: Binary Search
"""
Suppose we have the following sorted list, and we have to find the index of element 4 (the target value).
3,4,5,6,7,8,9
index: 0,1,2,3,4,5,6
"""

# This is how binary search works:
# 1. Set the first index as low and the last index as high.

# set low and high index
low = 0
high = len(lst) - 1

# here, 3 is the low index, and 9 is the high index.

# 2. Find the middle element.

mid = (low + high) // 2

here, mid = (0 + 6) // 2 = 3

# 3. Check for three possibilities.
# Possibility 1: If the target value is equal to the middle element, we have found the element.
if target_value == lst[mid]:
    result_index = mid
# Since our target_value is 4 and the current middle element is 6, this condition has not been met yet.

# Possibility 2: If the target value is greater than the middle element, update the low index to mid + 1.
if target_value > lst[mid]:
    low = mid + 1
# This condition has not been met yet.

# Possibility 3: If the target value is less than the middle element, update the high index to mid - 1.
if target_value < lst[mid]
    high = mid - 1

here, 3 is low and 5 is high

# Basically, we are updating the low and high indexes such that they are closer to both the mid value and the target element.

# 4. We update the mid element again and repeat step 3.
# We will repeat the process until low is greater than high. If low is greater than high, our target value is not in the list.

# if low is greater than high,
# the element is not found in the list 
while low <= high:

    # update middle point in each iteration
    mid = (low + high) // 2

    # condition for target value found
    if target_value == lst[mid]:
        return mid

    # update either low or high
    elif target_value < lst[mid]:
        high = mid - 1
    else:
        low = mid + 1

# Basically, in each iteration, we are updating either the low or high index to bring it closer to the position of the target element.

# In our case, the target element is found in the second iteration.
# here, in 3,4,5; 4 is mid

"""
Source Code: Binary Search
"""
# function to perform binary search
def binary_search(lst, target):
    
    # set low and high index
    low = 0
    high = len(lst) - 1
    
    # if low is greater than high,
    # the element is not found in the list 
    while low <= high:
        
        # find middle element
        mid = (low + high) // 2
        
        # if target value is equal to middle element
        # return the element
        if target == lst[mid]:
            return mid
        
        # if target value is less than the middle element
        # update high to mid - 1 
        elif target < lst[mid]:
            high = mid - 1
        
        # if target value is less than the middle element
        # update low to mid + 1 
        else:
            low = mid + 1
    
    return None

lst = [4, 5, 6, 7, 8, 9, 10]

# set a target value
target_value = 7

result = binary_search(lst, target_value)

if result:
    print(f"Element {target_value} is found at index {result}")
else:
    print(f"{target_value} is not found in the list")

# Output
# Element 7 is found at index 3

# Tip: We encourage you to add print() statements in the above program to display low, high and mid values to get an idea of how binary search updates these values.


"""
Source Code: Binary Search Using Recursion
"""
def binary_search(lst, target, low, high):

    if high >= low:
        mid = (high + low) // 2

        if lst[mid] == target:
            return mid

        elif lst[mid] > target:
            return binary_search(lst, target, low, mid - 1)

        else:
            return binary_search(lst, target, mid + 1, high)

    else:
        return None

lst = [3, 4, 5, 6, 7, 8, 9]

# target value to be searched for
target = 5

result = binary_search(lst, target, 0, len(lst) - 1)

if result:
    print(f"Element {target} is found at index {result}")
else:
    print("f{target} is not found in the list")

# Sample Output
# Element 5 is found at index 2

"""
Explanation: Binary Search Using Recursion

"""
# We call the binary_search() function recursively until low is greater than high (similar to the iterative process).
if high >= low:
    # 1. update the mid element
    # 2. if target is equal to mid, return index of mid
    # 3. update either low or high and make recursive calls
else:
    return None

# If low is greater than high, it means the target element is not in the list. We return None in this case.

# 1. Update the mid element.
mid = (low + high) // 2

# 2. If the target is equal to mid, return the index of mid.
if lst[mid] == target:
    return mid

# If the middle element is equal to the target, we have found the element. In this case, we return the index of the middle element, and the recursion ends.

# 3. Update either low or high elements and make recursive calls.
# Similar to the iterative process:
    # If the mid element is greater than the target, we update high to mid - 1.
    # If the mid element is less the target, we update low to mid + 1.
    # Then we call the binary_search() function with these updated values.
elif lst[mid] > target:
    return binary_search(lst, target, low, mid - 1)
else:
    return binary_search(lst, target, mid + 1, high)


"""
Complexity Analysis
The time and space complexities of binary search is given below:

Best Case Time Complexity	O(1)
Worst Case Time Complexity	O(logn)
Average Time Complexity	O(logn)
Space Complexity	O(1)
"""

