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
from utilities import stack_to_array, array_to_stack
from Stack_array import Stack
# Constants

stack = Stack()
data = [0, 1, 2, 3, 4]
array_to_stack(stack, data)
print(f'Stack empty: {stack.is_empty()}')
print('Values in stack: ')
for i in stack:
    print(i)

target = []
print(f'List before: {target}')
stack_to_array(stack, target)


print(f'List after: {target}')
# print(stack.is_empty())
print(f'Stack empty: {stack.is_empty()}')
