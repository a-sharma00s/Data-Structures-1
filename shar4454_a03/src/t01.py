"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ashish Sharma
ID:      169044454
Email:   shar4454@mylaurier.ca
__updated__ = "2023-02-06"
-------------------------------------------------------
"""
# Imports
from functions import stack_split_alt
from utilities import array_to_stack
from Stack_array import Stack
# Constants

a = [5, 7, 8, 9, 12, 14, 8]
source = Stack()
array_to_stack(source, a)
print(f'Source (stack): {source._values}')
target1, target2 = stack_split_alt(source)
print(f'Target 1: {target1._values}')
print(f'Target 2: {target2._values}')
