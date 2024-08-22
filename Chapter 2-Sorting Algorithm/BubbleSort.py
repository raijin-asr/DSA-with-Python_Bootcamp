# Bubble sort works by repeatedly comparing two adjacent elements and swapping them if they are not in the correct order.

# Bubble Sort Algorithm
# Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
# The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted.

# Working of Bubble Sort
# The bubble sort algorithm works as follows:
# 1. Compare the first two elements of the list.
# 2. If the first element is greater than the second element, swap them.
# 3. Move to the next pair of elements and repeat step 1.
# 4. Continue this process until you reach the end of the list.
# 5. Repeat steps 1-4 for each pass through the list until no swaps are needed.

# Thought Process to Implement Bubble Sort
# To implement bubble sort in Python:

# 1. Compare an element with its next element and swap them if necessary.

lst = [12, -4, 56, 67, 10]
j = 0

if lst[j] > lst[j + 1]:
    # swap elements       
    lst[j], lst[j + 1] = lst[j + 1], lst[j] # swap elements

# 2. Repeat Step 1 for each element in the list using a loop.
# Since we are comparing each element to its next element, we only need to run the loop up to the second-last element.
# This is because the last element will not have a next element for comparison.

for j in range(len(lst) - 1): # loop through the list
    if lst[j] > lst[j + 1]: # compare elements and swap if necessary
        lst[j], lst[j + 1] = lst[j + 1], lst[j] # swap elements 

# 3. Repeat Step 2 for each element in the list.
# Repeat the above steps for each position. With each iteration of the outer loop, one element will settle in its correct position, starting from the largest element.

for i in range(len(lst)): # loop through the list
    for j in range(len(lst) - 1): # loop through the list again 
        if lst[j] > lst[j + 1]:   
            lst[j], lst[j + 1] = lst[j + 1], lst[j]


# Source Code: Bubble Sort:---------------
def bubble_sort(lst): 
 
    # outer loop to access each list element
    for i in range(len(lst)):
 
        # inner loop to compare list elements
        for j in range(len(lst) - 1):
 
            # swap elements if necessary
            if lst[j] > lst[j + 1]: #ascending order, use > and for descending order use <
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst       
 
data_list = [15, 16, 6, 8, 5]
print(f"Unsorted List: {data_list}") # Output: Unsorted List: [15, 16, 6, 8, 5]
 
sorted_list = bubble_sort(data_list) 
 
print(f"Sorted List: {sorted_list}") # Output: Sorted List: [5, 6, 8, 15, 16]

"""Optimized Bubble Sort Algorithm
Our bubble sort program carries out several unnecessary, redundant comparisons.

We can avoid these redundant tasks and save time and resources by optimizing bubble sort."""

# Optimize Inner Loop
# This is the bubble sort algorithm we've been using so far:

def bubble_sort(lst):

    for i in range(len(lst)):
        for j in range(len(lst) - 1):           
            if lst[j] < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

# If we look at the inner loop, we can notice it always iterates up to the second-last element, making comparisons even for elements that are already in their correct positions.

# inner loop always runs up to the second-last element
for j in range(len(lst) - 1):           
# However, with every iteration of the outer loop, one element moves to its correct position.

# Hence, the inner loop can reduce its iterations by one with each pass of the outer loop.
# for the first outer loop iteration, i is 0.
# for the second outer iteration, i is 1.
# and so on.
    for j in range(len(lst) - 1 - i):

"""Optimize Loop Logic
In bubble sort, each iteration of the outer loop places one element in its correct position.
However, if no swaps occur during an entire pass of the inner loop, we know that elements are already in their correct positions—the list is sorted.

Here's how we can add this logic to our code:"""
for i in range(len(lst)):

    # initialize a variable as False
    # to indicate that no swaps have taken place 
    swapped = False

    for j in range(len(lst) - 1 - i):

        if lst[j] > lst[j + 1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

            # if any element is swapped, 
            # set swapped to True.
            swapped = True

    # if swapped remains False after the inner loop,
    # it means none of the elements were swapped
    # therefore, the list is already sorted, and we can exit.
    if not swapped:
        break

"""Optimize Outer Loop
Bubble sort places each element in its correct position, starting from the last position and moving towards the start.
When the correct element is placed at the second position, the correct element will be placed at the first position as well.

Therefore, we can modify the outer loop from:"""
for i in range(len(lst)):
# To:
for i in range(len(lst) - 1):

# Source Code: Optimized Bubble Sort:------
# Bubble sort in ascending order
def bubble_sort(data):
 
    for i in range(len(data) - 1): # optimize outer loop by -1 
        swapped = False
        for j in range(len(data) - 1 - i): # optimize inner loop by -1 and -i, works for both loops
            if data[j] > data[j + 1]:
                data[j], data[j+1] = data[j+1], data[j]
                swapped = True
        if not swapped: # break if no swaps occur
            break
        
    return data
 
data_list = [4, 6, 99, 45, 0]
 
sorted_list = bubble_sort(data_list)
print(sorted_list) # Output: [0, 4, 6, 45, 99]

"""Time Complexity of Bubble Sort
Let's say we have a list with a total of 8 elements.

Here's the breakdown of comparisons for each iteration:

First Iteration - 7 comparisons
Second Iteration - 6 comparisons
Third Iteration - 5 comparisons and so on
The total number of comparisons will be 7 + 6 + 5 + 4 + 3 + 2 + 1."""

# Hence, for n elements in a list, the total number of comparisons will be:
# Comparison(C)=(n−1)+(n−2)+...+2+1    = n(n−1)/2  = n**2

"""Time complexity of comparison-based sorting algorithms is based on the number of comparisons. Therefore, the time complexity is:
Time Complexity = O(n**2)

Worst Case Complexity: O(n**2)
Average Case Complexity: O(n**2)
Best Case Complexity: O(n)


Note: In the best-case scenario, the list is already sorted. In this situation, no swaps occur, and the loop terminates after the first iteration of the outer loop.

Why O(n^2)?
In big O notation, we're interested in the growth rate of a function as the input size (n) increases. We ignore constant factors and lower-order terms.

n(n-1)/2 can be simplified to (n^2 - n)/2.
Ignoring the constant factor (1/2) and the lower-order term (-n), we're left with n^2.
Therefore, the time complexity of bubble sort is O(n^2). """

# Space Complexity
# The space complexity of the bubble sort is O(1) because it only requires a constant amount of additional space for its variables.

"""Applications of Bubble Sort
When to use bubble sort?

Use bubble sort for:
Small datasets.
When simplicity is more important than efficiency.
When the data is already partially sorted.

When not to use bubble sort?
Avoid bubble sort for large datasets and performance-critical applications.

In such cases, sorting algorithms like merge sort or quick sort are more suitable."""