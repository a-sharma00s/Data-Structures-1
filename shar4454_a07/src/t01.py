"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ashish Sharma
ID:      169044454
Email:   shar4454@mylaurier.ca
__updated__ = "2023-03-20"
-------------------------------------------------------
"""
# Imports
from List_linked import List
# Constants

lst = List()
lst2 = List()

# append
print('append')
for i in range(10):
    lst.append(i + 1)
    lst2.append(i + 1)
# prepend
print('Prepend:')
lst2.prepend(0)
print('Remove front')
value = lst2.remove_front()
print(value)
for i in lst:
    print(i, end=" ")
print()
for i in lst2:
    print(i, end=" ")
