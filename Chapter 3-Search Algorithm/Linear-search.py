# The linear search algorithm is used to find an element within a list.

"""
In this algorithm, we sequentially check each element of the list until the desired element is found.
Suppose we have the following list, and we have to find the index of element 4 (the target value).
9,10,5,8,7,11,6,15,3

In linear search, we sequentially check each index to see if the target value (in this case, element 4) is present. We start from index 0, then index 1, index 2, and so on, until the element is found.
In this particular case, the target value is at index 5. Once this element is found, the linear search ends.
"""

#Thought Process to Implement Linear Search


# To implement linear search, we follow these steps:
# 1. Use a loop to traverse (access elements one-by-one) along with its corresponding index.

for index, element in enumerate(lst):
    pass

# 2. Compare each element with the target value.
# Within the loop, we will compare list elements to the target value. If a match is found, we use the corresponding index of that value.
for index, element in enumerate(lst):
   if element == target:
        result = index

# 3. If the element is not found in the list, set the result to None.
for index, element in enumerate(lst):
   if element == target:
        result = index

result = None

"""
Source Code: Linear Search
"""

# function to perform  linear search
def linear_search(lst, target):
    
    # traverse through each element
    for index, element in enumerate(lst):
        
        # compare each element with a target value
        if element == target:
            return index
    
    # return None if the target isn't found in lst
    return None

lst = [9, 10, 5, 8, 7, 4, 11, 6, 15, 3]

# set a target value
target_value = 4

result = linear_search(lst, target_value)

if result:
    print(f"Index of the target value: {result}")
else:
    print("Target value not found in the list.")
 
"""
Problem: Find the Occurrence of a Number
"""
# Replace ___ with your code

def count_occurrences(lst, n):
    count = 0
    
    # traverse through each element
    for index, element in enumerate(lst):
        
        # compare each element with a target value
        if element == n:
            count += 1
    
    # return the number of occurrences
    return count

lst = [3, 3, 4, 5, 6, 6, 6, 2]

# take integer input
n = int(input())

# call count_occurrences() to
# count the number of occurrences of n
count = count_occurrences(lst, n)

print(count)

"""
Complexity Analysis
The time and space complexities for linear search is given by the table below:

Best Case Time Complexity	O(1)
Worst Case Time Complexity	O(n)
Average Time Complexity	O(n)
Space Complexity	O(1)
"""