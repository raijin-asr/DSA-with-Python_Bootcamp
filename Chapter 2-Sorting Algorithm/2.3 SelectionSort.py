"""Selection sort works by repeatedly selecting the smallest (or largest) unsorted element and placing it towards the beginning of the list.

Working of Selection Sort:
1. Find the smallest element and swap it with the first element in the list.
--At this point, the correct element is placed at the first position. However, the portion of the list from the second position to the last remains unsorted.

2. Find the smallest element in the unsorted portion of the list and swap it with the second element.

3. Continue this process until all the elements are sorted.

The image below shows the final step in this process.

In the last step, the last two elements may be unsorted. Once the elements are swapped (if necessary), the list will be sorted."""

# Thought Process to Implement Selection Sort:------

# 1. Find the index of the smallest element in the list.

lst = [18, 10, 8, 14, 1]
min_index = 0
 
# iterate from second element to last
for j in range(1, len(lst)):
    
    # get the index of the smallest element
    if lst[j] < lst[min_index]:
        min_index = j # update the index of the smallest element
 
print(min_index)  # 4 index having value 1

# 2. Swap the smallest element with the first element.

# swap the smallest element with the first element
lst[min_index], lst[0] = lst[0], lst[min_index]

# Now, the smallest element is placed in the first position.
# We need to continue these steps for each position.
# Next, we will add an outer loop to this code (with some adjustments) so that this process is repeated for all positions.

# 3. Repeat step 2 for each element in the list.

for i in range(len(lst)):
    min_index = i

    for j in range(i + 1, len(lst)):
        if lst[j] < lst[min_index]:
            min_index = j

# Here, we have added an outer loop to ensure that each element in the list is considered, not just the first element.

# Source Code: Selection Sort:------------
def selection_sort(lst):
   
    for i in range(len(lst)):
        # assume the first unsorted element is the minimum
        min_index = i
    
        # iterate over unsorted elements
        for j in range(i + 1, len(lst)):
            # find index of the smallest element
            # in the unsorted part of the list
            if lst[j] < lst[min_index]:
                min_index = j
    
        # swap the smallest element with the first element
        # of the unsorted part 
        lst[min_index], lst[i] = lst[i], lst[min_index]
    
    return lst
 
 
data = [18, 10, 8, 14, 1]
print(f'Unsorted List: {data}') # [18, 10, 8, 14, 1]
 
sorted_list = selection_sort(data)  
print(f'Sorted List: {sorted_list}')    # [1, 8, 10, 14, 18]

#PROBLEM1: in ascending order sorting
def selection_sort(lst):
    # write your code here
    for i in range(len(lst)):
        min_ind=i
        for j in range(i+1,len(lst)):
            if lst[j] < lst[min_ind]: #for descending order change < to >
                min_ind=j
        lst[min_ind], lst[i] = lst[i], lst[min_ind]
    return lst

# take integer inputs and convert it to a list
data_list = list(map(int, input().split()))

# call the selection_sort() function
result = selection_sort(data_list)

# print the sorted list
print(result)

#PROBLEM2:  Write a program to count the number of swaps made during the selection sort process.
def count_swaps(lst):   
    # set number of swaps to 0
    swaps = 0   
    for i in range(len(lst)):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        # swap only if lst[i] and lst[min_index] are not equal     
        if lst[i] !=lst[min_index]:
            lst[min_index], lst[i] = lst[i], lst[min_index]
            # increment the swaps variable
            swaps+=1    
    return swaps

# take integer inputs and convert it to a list
data = list(map(int, input().split()))
result = count_swaps(data)
print(result)

# Time Complexity:--------------
# same as bubble sort, it has two nested loops, so the time complexity is O(n**2).
# # Comparison(C)=(n−1)+(n−2)+...+2+1    = n(n−1)/2  = n**2 

"""Time complexity of comparison-based sorting algorithms is based on the number of comparisons. Therefore, the time complexity is:
Time Complexity = O(n**2)

Worst Case Complexity: O(n**2)
Average Case Complexity: O(n**2)
Best Case Complexity: O(n**2)

The time complexity of selection sort is the same in all the cases."""

# Space Complexity:--------
# The space complexity of the selection sort is O(1) because it only requires a constant amount of additional space for its variables.

"""
Applications of Selection Sort
When to use selection sort?
Use selection sort for small lists where simplicity is more important than speed.
While this also applies to bubble sort, selection sort generally requires fewer swaps.
Therefore, it's favored over bubble sort when the cost of swapping significantly outweighs the cost of comparisons.

When not to use selection sort?
Avoid selection sort for larger lists or situations where speed is crucial. Merge sort and quick sort are preferable for larger lists.
"""