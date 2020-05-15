import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
'''for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)'''
# The old code is an O(n^2) function it ran in 12.37 seconds on my local machine
# the old code appended 64 duplicates.

# Use a Binary Sorted Tree
from bst import BSTNode

bst = BSTNode(names_1[0]) # Make a root node

for name in names_1[1:]: # Insert remaining nodes from names_1
    bst.insert(name)

for name in names_2: # Checking if my bst contains a name in names_2
    if bst.contains(name):
        duplicates.append(name)
# The new code is O(log n) it takes 0.25 seconds on my local machine
# the new code appended 64 duplicates. 


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
