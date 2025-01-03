"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ashish Sharma
ID:      169044454
Email:   shar4454@mylaurier.ca
__updated__ = "2023-03-11"
-------------------------------------------------------
"""
# Imports
from List_linked import List
# Constants

# Test methods
lst = List()
values = [1, 2, 3, 4, 5]
for i in values:
    # append testing
    lst.append(i)
# prepend testing
lst.prepend(0)
# insert testing
lst.insert(2, 10)
print('Linked List Contents..')
for i in lst:
    print(i)

# linear search testing
previous, current, index = lst._linear_search(3)
print(f'{previous}, {current}, {index}')
