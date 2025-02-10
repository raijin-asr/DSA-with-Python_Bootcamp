# Introduction------------------
# Merge sort breaks a list into multiple sublists, and each sublist is then sorted individually.
# Then, the sorted sublists are combined to form the sorted list.
# This strategy is known as divide-and-conquer.

"""
How do Divide-And-Conquer Algorithms Work?-----
The divide-and-conquer approach involves three main steps:

1. Divide: Divide the given problem into smaller subproblems (mostly using recursion).
2. Conquer: Solve the smaller subproblems recursively. If the subproblem is small enough, solve it directly using a base case.
3. Combine: Combine the solutions of the subproblems that are part of the recursive process to solve the actual problem.
"""

# Working of Merge Sort:-----------
"""
Suppose we have the following unsorted list.
5,4,7,3,2

This is how the merge sort works.

1. Divide the list into two halves.
5,4 and 7,3,2

Note: In the case of a list with an odd number of elements, the lengths of two halves will differ by 1

2. Continue dividing each half recursively until we get individual elements.

5,4 -> 5 and 4
7,3,2 -> 7  and 3, 2
3,2 -> 3 and 2

3. Merge the individual elements in a sorted manner.

Here, the conquer and combine steps go side by side.

5,4 -> 4,5
3,2 -> 2,3

7,2,3 -> 2,3,7

4,5 and 2,3,7 -> 2,3,4,5,7

This is how the merge sort works. It is a stable sorting algorithm and has a time complexity of O(n log n).
"""

# Thought Process to Implement Merge Sort----------
"""Divide the List Recursively
First, we need to divide the list into equal halves recursively until we get individual elements. Here's how we can do it:

1. Find the midpoint of the list."""
def merge_sort(lst):
    mid = len(lst) # 2

# 2. Divide the list's smaller halves recursively until individual elements are retrieved.   
def merge_sort(lst):

    mid = len(lst) # 2

    # end recursion if list is divided into individual elements
    # i.e. when list length is 1
    if len(lst) <= 1:
        return lst

    # get the left half portion of list and recursively divide it again
    left_partition = merge_sort(lst[: mid])

    # get the right half portion of list and recursively divide it again
    right_partition = merge_sort(lst[mid: ])

# Source Code: Divide the List Recursively----------

def merge_sort(lst):
 
    # if length of lst in 1 or less,
    # we know lst is completely divided
    # end recursion in this case       
    if len(lst) <= 1:
        return lst
        
    print(f'lst: {lst}')
 
    # get the mid-point of the list
    mid = len(lst) // 2
 
    print(f'mid: {lst[mid]}')
 
    # get the left half portion of list
    # and recursively divide it again
    left = merge_sort(lst[: mid])
    print(f'Left partition: {left}')
 
    # get the right half portion of list
    # and recursively divide it again
    right = merge_sort(lst[mid: ])
    print(f'Right partition: {right}')
 
    return '---'
 
data = [6, 8, 1, 4, 5, 3, 7, 2]
merge_sort(data)


# Here, we have added print() statements to get an idea on how our merge_sort() function works.

# Output
"""
lst: [6, 8, 1, 4, 5, 3, 7, 2]
mid: 5
lst: [6, 8, 1, 4]
mid: 1
lst: [6, 8]
mid: 8
Left partition: [6]
Right partition: [8]
Left partition: ---
lst: [1, 4]
mid: 4
Left partition: [1]
Right partition: [4]
Right partition: ---
Left partition: ---
lst: [5, 3, 7, 2]
mid: 7
lst: [5, 3]
mid: 3
Left partition: [5]
Right partition: [3]
Left partition: ---
lst: [7, 2]
mid: 2
Left partition: [7]
Right partition: [2]
Right partition: ---
Right partition: ---


As you can see, the merge_sort() function is dividing lists until we get a list of one element.
In the program, the merge_sort() function is returning '---'.
However, to perform conquer and combine, we will call another function merge() from the return statement. This function will combine individual elements in a sorted manner, which we will explore next.
"""


"""# Thought Process: The merge() Function----------"""
# Suppose we have two sorted lists: left and right.
left = [5]
right = [4]

# Our goal is to get this sorted list, [4, 5], by merging them.
# The merge() function should also work for lists with more than one element.

# Suppose we have two sorted lists: left and right.
left = [4, 5]
right = [2, 3, 7]

# Our goal is to get this sorted list, [2, 3, 4, 5, 7], by merging them.

# Here's how we can implement this functionality inside the merge() function.

# 1. Compare the elements of left and right and add the smaller element to the output list
# [left, right] = [[4, 5], [2, 3, 7]]     
# compare 4 from left and 2 from right, so 2 is smaller and add it to the output list

# empty list to store the merged result
output = []

# index for the left sublist
i = 0

# index for the right sublist
j = 0

# if element of left list is smaller
# add that element to the output list
if left[i] < right[j]:
    output.append(left[i])

# else, add the element of right list
else:
    output.append(right[j])

# 2. Repeat Step 1 for all elements in both lists until we reach the end of one of the lists.
# Using a loop, we need to compare elements of left with the element elements of right in the manner shown below:

[4, 5], [2, 3, 7], output = [2]
[4, 5], [3, 7], #again, compare 4 and 3, 3 is smaller, so output = [2, 3]
[4, 5], [7], #again, compare 4 and 7, 4 is smaller, so output = [2, 3, 4]
[5], [7], #again, compare 5 and 7, 5 is smaller, so output = [2, 3, 4, 5]
[], [7], #left list is empty, so add all elements of right to the output list

# This allows us to extract the smallest elements one by one.
output = [ ]

i = 0
j = 0

# loop through both the lists
while i < len(left) and j < len(right):

    if left[i] < right[j]:
        output.append(left[i])
        i += 1;    # increment i
    else:
        output.append(right[j])
        j += 1;    # increment j
# The loop terminates once one of the lists exceeds its bounds.

# 3. Outside the loop, append the remaining elements and return the output list.
def merge(left, right):
    output = [ ]

    i = 0
    j = 0

    while i < len(left) and j < len(right): 

        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j]) 
            j += 1

    # copy the remaining elements to output
    output.extend(left[i:])
    output.extend(right[j:])

    return output


"""Source Code: merge() Function
"""
def merge(left, right):
    output = [ ]
 
    i = 0
    j = 0
 
    while i < len(left) and j < len(right): 
 
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j]) 
            j += 1
 
    # copy the remaining elements to output
    output.extend(left[i:])
    output.extend(right[j:])
 
    return output
 
 
print(merge([5], [8]))    # [5, 8]
print(merge([8], [5]))    # [5, 8]
print(merge([3, 4], [7, 10]))  # [3, 4, 7, 10]
print(merge([3, 4], [7, 10, 11]))  # [3, 4, 7, 10, 11]

# Note: For this function to work, left and right must already be sorted.
# As you can see, the merge() function merges two lists in a sorted order.

"""Next, we will combine the divide part and the merge part in the same code to create our merge sort program.

Source Code: Merge Sort
"""
# function to perform merge sort
def merge_sort(lst):
 
    # base condition:
    # recursion ends if the length of the list is 1 or less    
    if len(lst) <= 1:
        return lst
 
    mid = len(lst) // 2
 
    # get the left half of the list
    # and further divide it using recursion
    left_partition = merge_sort(lst[: mid])
 
    # get the right half of the list
    # and further divide it using recursion
    right_partition = merge_sort(lst[mid:])
 
    # call the merge() function 
    # combine list recursively
    return merge(left_partition, right_partition)
 
# function to sort and merge sublists (conquer phase)
def merge(left, right):
 
    output = []
 
    i = 0   
    j = 0 
 
    # merge elements in a sorted manner 
    # from left and right portions
    while i < len(left) and j < len(right):
 
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1
 
    # append the remaining element
    output.extend(left[i:])
    output.extend(right[j:])
        
    return output
        
data = [6, 8, 1, 4, 5, 3, 7, 2]
print(f"Unsorted: {data}")
 
result = merge_sort(data)
 
print(f"Sorted: {result}")

# Output

# Unsorted: [6, 8, 1, 4, 5, 3, 7, 2]
# Sorted: [1, 2, 3, 4, 5, 6, 7, 8]

# In this program, the merge_sort() function handles the divide part and the merge() function handles the conquer part.

# Idea Emoji
# Tip: If you're learning merge sort for the first time, its implementation can be challenging to grasp. If you have any confusion, we suggest you go through this lesson again. You will have a much better understanding on the second read.


"""PROBLEM1: Merge Sort Implementation

Problem Description
Can you write the merge sort program on your own?

Create a function named merge_sort() that takes a list of numbers as its argument.
Sort the list using merge sort and return it.
Outside the function, print the returned list."""

def merge_sort(lst):
    
# base condition:
    # recursion ends if the length of the list is 1 or less    
    if len(lst) <= 1:
        return lst
 
    mid = len(lst) // 2
 
    # get the left half of the list
    # and further divide it using recursion
    left_partition = merge_sort(lst[: mid])
 
    # get the right half of the list
    # and further divide it using recursion
    right_partition = merge_sort(lst[mid:])
 
    # call the merge() function 
    # combine list recursively
    return merge(left_partition, right_partition)
 
# function to sort and merge sublists (conquer phase)
def merge(left, right):
 
    output = []
 
    i = 0   
    j = 0 
 
    # merge elements in a sorted manner 
    # from left and right portions
    while i < len(left) and j < len(right):
 
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1
 
    # append the remaining element
    output.extend(left[i:])
    output.extend(right[j:])
        
    return output

# take integer inputs and convert it to a list
data_list = list(map(int, input().split()))

sorted_list = merge_sort(data_list)

print(sorted_list)



"""
Practice: PROBLEM2
Merge Sort in Descending Order
Easy
Problem Description
Write a program to sort the list items in descending order using merge sort.

Create a function named merge_sort() that takes a list as its argument.
Sort the list in descending order within the function and return the sorted list.
Print the sorted list from outside the function.
"""

def merge_sort(lst):
    
# base condition:
    # recursion ends if the length of the list is 1 or less    
    if len(lst) <= 1:
        return lst
 
    mid = len(lst) // 2
 
    # get the left half of the list
    # and further divide it using recursion
    left_partition = merge_sort(lst[: mid])
 
    # get the right half of the list
    # and further divide it using recursion
    right_partition = merge_sort(lst[mid:])
 
    # call the merge() function 
    # combine list recursively
    return merge(left_partition, right_partition)
 
# function to sort and merge sublists (conquer phase)
def merge(left, right):
 
    output = []
 
    i = 0   
    j = 0 
 
    # merge elements in a sorted manner 
    # from left and right portions
    while i < len(left) and j < len(right):
 
        if left[i] > right[j]:  #DESCENDING ORDER
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1
 
    # append the remaining element
    output.extend(left[i:])
    output.extend(right[j:])
        
    return output

# take integer inputs and convert it to a list
data_list = list(map(int, input().split()))

sorted_list = merge_sort(data_list)

print(sorted_list)



"""
Practice:
Nth Smallest Element of Two Sorted Lists
Easy
Problem Description
Write a program to find the nth smallest element after merging and sorting two sorted lists.

Create a function named find_smallest_number() that takes three arguments: two lists and an integer n.
Assumption: The input lists will always be in ascending order.
Inside the function, merge two lists in ascending order.
Then, find the nth element from the list and return it.
Print the nth smallest element from outside the function.
For example,

For lists [4, 9, 11] and [3, 5, 7]. It's 4th smallest element is 7.

It's because if we merge these lists in ascending order, we will get [3, 4, 5, 7, 9, 11]. Hence, the 4th smallest element is 7.

Tip: Use the logic of the merge() function we previously created to merge lists in ascending order. Then, find the nth element.
"""

def find_smallest_number(nums1, nums2, n):
    output = [ ]
 
    i = 0
    j = 0
 
    while i < len(nums1) and j < len(nums2): 
 
        if nums1[i] < nums2[j]:
            output.append(nums1[i])
            i += 1
        else:
            output.append(nums2[j]) 
            j += 1
 
    # copy the remaining elements to output
    output.extend(nums1[i:])
    output.extend(nums2[j:])
 
    return output[n - 1]

# take integer inputs and convert it to a list
nums1 = list(map(int, input().split()))

# take integer inputs and convert it to a list
nums2 = list(map(int, input().split()))

# take integer input
n = int(input())

result = find_smallest_number(nums1, nums2, n)

print(result)

# OUTPUT:
# Input 
# 5 6 7
# 3 5 9
# 2

# Your Output 
# 5

# Expected Output 
# 5


"""
Time Complexity
As recursion is used in merge sort, we need to use the master theorem to find its complexity.

Best Case Complexity: O(n log n)
Worst Case Complexity: O(n log n)
Average Case Complexity: O(n log n)
"""


"""
Space Complexity
In the merge phase, elements from two sublists are copied into a newly created list. In the very last merge step, the new list is exactly as large as the list to be sorted.
Thus, if the input list is twice as large, the additional storage space required is doubled.

So, the space complexity of the merge sort is O(n).
"""

# Applications of Merge Sort
# Use merge sort to sort large amounts of data accurately and efficiently. It works better than bubble sort, selection sort, and insertion sort in most cases.