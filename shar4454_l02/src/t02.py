"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ashish Sharma
ID:      169044454
Email:   shar4454@mylaurier.ca
__updated__ = "2023-01-28"
-------------------------------------------------------
"""
# Imports
from utilities import array_to_stack
from Stack_array import Stack
# Constants

s = Stack()
data = [0, 1, 2, 3, 4]
print(f'list before: {data}')
print(f'stack empty: {s.is_empty()}')
array_to_stack(s, data)


print('Values in stack: ')
for i in s:
    print(i)
print(f'list after: {data}')
print(f'stack empty: {s.is_empty()}')
