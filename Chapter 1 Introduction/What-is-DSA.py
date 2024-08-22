# ++Data Structures----------
# --A data structure is a way of storing data in an organized manner so that it can be accessed efficiently. We can classify such structures into two types.

# a) Fundamental Data Structures
# --We know about lists, dictionaries, sets, etc., in Python—they are the built-in data structures of the language. Such data structures are called fundamental data structures.

# --Each of these data structures operates uniquely, and our choice among them depends on our specific requirements. For instance, it's better to use dictionaries if we need to work with key-value pairs, even though we can perform the same task using a list.

# b) Custom Data Structures
# --Built-in data structures are not enough for writing complex programs.

# Imagine working on a mapping service like Google Maps.
# --If we rely solely on built-in data structures to create a mapping service, our program won't be efficient.
# In such cases, we employ logic to develop custom data structures such as graphs, trees, hash maps, etc.

# Note: Custom data structures are developed using fundamental data structures.


# Algorithms----------
# An algorithm is a step-by-step process to solve a problem.

# For example, here is an algorithm to check whether a given number is odd or even.

# Step 1: Input: A number n
# Step 2: If n is perfectly divisible by 2, 
#          - Then print "The number is even" 
# Step 3: Else
#          - Print "The number is odd"
# Step 4: End

# If we implement this process, we will be able to write a program easily to check whether a number is even or odd.

n = 5
 
if n % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# Sum of Natural Numbers

def calculate_sum(n):
    
    total = 0
    
    for i in range(n+1):
        total += i
    
    return total
    
result = calculate_sum(100)
print(result)    # 5050

# Optimized: Sum of Natural Numbers
# We can find the sum of natural numbers using a simple formula:

# Sum of natural numbers= n∗(n+1) / 2

# Let's use this formula to find the sum of natural numbers.

def calculate_sum(n):
    return n * (n + 1) // 2
    
result = calculate_sum(100)
print(result)    # 5050

# This program runs in a fraction of a second, even for very large numbers. It's because we solved this problem with a single instruction, regardless of the size of the input.