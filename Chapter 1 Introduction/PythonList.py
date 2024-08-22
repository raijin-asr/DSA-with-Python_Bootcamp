# Python Lists:

# Slicing a List:
numbers = [10, 20, 30, 40, 50, 60 ]

# We can create a sublist with the items [30, 40, 50] from numbers using the slicing notation as follows:
numbers = [10, 20, 30, 40, 50, 60]
 
# start: 2
# end: 5
new_numbers = numbers[2: 5] #start index is inclusive, but the end index is exclusive.
print(new_numbers)    # [30, 40, 50]

# items from index 0 to 3
print(numbers[0: 4])    # [10, 20, 30, 40]
 
# items from index 3 to 4
print(numbers[3: 5])   # [40, 50]
 
# using negative index in slicing
 
# items from the fourth item (3rd index)
# to the second-last item
 
print(numbers[3: -1])   # [40, 50]

# Omit Start and End Index in Slicing

# Omit the Start Index:
# If we omit the start index, the slicing starts from the first item.
numbers = [10, 20, 30, 40, 50, 60]
 
# items from first item to third index
print(numbers[: 4])    # [10, 20, 30, 40]

# Omit the End Index:
# If we omit the end index, the slicing goes up to the last item.

# items from 3rd index to last item
print(numbers[3: ])   # [40, 50, 60]

# What if we omit both the start and end indexes?
# If we omit both the start and end indexes, we get a new list that contains all the items from the original list (from the first item to the last item). 

# omitting both the start and end indexes
# items from first to last
print(numbers[:])   # [10, 20, 30, 40, 50, 60]

# Repetition with Lists:
# Suppose, we need to create a list with five elements, all having the value 0. We can easily achieve this using the * operator. For example,

lst = [0] * 5
print(lst)  # [0, 0, 0, 0, 0]

# List Methods:----------------------
# Now, let's cover a few commonly used list methods. These methods are used throughout the course.

# Method	Description
# append()	add an element to the end of the list
# extend()	add elements of an iterable (list, tuple, etc.) to the end of the list
# insert()	insert an element at the specified index
# pop()	    remove an element from the list and return it
# reverse() 	reverse the elements of the list

# List append() and extend():

# The append() method
# The append() method adds an element to the end of the list.
currencies = ['Dollar', 'Euro', 'Pound']
 
# append 'Yen' to the list
currencies.append('Yen')
 
print(currencies) #['Dollar', 'Euro', 'Pound', 'Yen']

# The extend() method

# The extend() method adds all the elements of an iterable (a list, tuple, string, etc.) to the end of the list.
languages = ['French', 'English']
languages1 = ['Spanish', 'Portuguese']
 
# append language1 elements to languages
languages.extend(languages1)
 
print(languages) #['French', 'English', 'Spanish', 'Portuguese']

# Note: The append() and extend() method also does not return any value; it only modifies the original list.

# we can also use the + operator to extend a list in Python. For example,

languages = ['French', 'English']
languages1 = ['Spanish', 'Portuguese']
 
# append language1 elements to languages
languages = languages + languages1 #same as extend()
 
print(languages)

# List pop()
# The pop() method removes the item at the specified index. The method also returns the removed item.

prime_numbers = [2, 3, 5, 7]
 
# remove the element at index 2
removed_element = prime_numbers.pop(2) # 2 is index of 5
 
print(f"Updated List: {prime_numbers}") #Updated List: [2, 3, 7]
print(f"Removed Element: {removed_element}") #Removed Element: 5

# If we do not pass any arguments to the pop() method, it removes the last element.
prime_numbers = [2, 3, 5, 7]
 
# remove the last item
prime_numbers.pop() # 7 is removed
 
print(f"Updated List: {prime_numbers}")


# List insert()
# The insert() method inserts an element at the specified index.

# create a list of vowels
vowel = ['a', 'e', 'i', 'u']
 
# insert 'o' at index 3 (4th position)
vowel.insert(3, 'o')
 
print(vowel) #['a', 'e', 'i', 'o', 'u']

# List reverse()
# The reverse() method reverses the elements of the list.

prime_numbers = [2, 3, 5, 7]
 
# reverse the order of list elements
prime_numbers.reverse()
 
print(prime_numbers) #[7, 5, 3, 2]

# enumerate()
# The for loop in Python doesn't automatically use indexes.

languages = ['Python', 'Java', 'JavaScript']
 
for language in languages:
    print(language) #Python, Java, JavaScript

# However, if we need to access the index during each iteration of a for loop, we can use the enumerate() function along with the loop.
# First, let's see how enumerate() works:

languages = ['Python', 'Java', 'JavaScript']
 
enumerate_languages = enumerate(languages)
 
# convert enumerate object to list
print(list(enumerate_languages)) #[(0, 'Python'), (1, 'Java'), (2, 'JavaScript')]

# enumerate() adds a counter to our list and returns it.
# Now, let's see how we can use it in a for loop.

languages = ['Python', 'Java', 'JavaScript']
 
for index, language in enumerate(languages):
    print(index, language) #0 Python, 1 Java, 2 JavaScript