stoch_prizes = [208, 145,567,644,878]

# Number are stored in bites in the RAM 
# Access the element using the Index

print("Stock prize on Day 1: ", stoch_prizes[1])
print("Stock prize on Day 2: ", stoch_prizes[2])


# Insert the elements in array
# array.insert(index, value )
stoch_prizes.insert(0,1000)
print(stoch_prizes)

# Remove Elements 
# array.pop(index)
stoch_prizes.pop(0)
print(stoch_prizes)

# get all item 
for element in stoch_prizes:
    print(element)


"""
Advantages of Arrays

    Fast Access: Retrieve elements quickly using their index.
    Efficient Memory: Stores elements in contiguous memory locations.

Limitations of Arrays

    Fixed Size: Once declared, the size cannot be changed.
    Costly Insertions/Deletions: Adding or removing elements in the middle requires shifting elements.
    Homogeneity: All elements must be of the same type.

Use Cases

    Storing a list of items like names or numbers.
    Implementing other data structures (e.g., stacks, queues).
    Managing data in algorithms like sorting and searching.

"""


# Reverse Array 

def reverse_array(array):
    start = 0
    end = len(array)-1
    if start >= end:
        return array
    else:
        array[start], array[end] = array[end] , array[start]
        start+=1 
        end-=1 
        return array
    
print(reverse_array(stoch_prizes))


def using_stack(array):
    stack = []
    for num in array:
        stack.append(num)

    reversed_array = []
    while stack:
        reversed_array.append(stack.pop())

    print(reversed_array)

using_stack(stoch_prizes)


# Using Bulit in funciton 
print(stoch_prizes)