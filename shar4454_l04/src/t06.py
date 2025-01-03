"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ashish Sharma
ID:      169044454
Email:   shar4454@mylaurier.ca
__updated__ = "2023-02-11"
-------------------------------------------------------
"""
# Imports
from utilities import array_to_list, list_to_array
from List_array import List
# Constants

llist = List()
array = [1, 2, 3, 4, 5]
print(f'List: {array}')
array_to_list(llist, array)

print(f'List object: {llist._values}')

target = []
list_to_array(llist, target)
print(f'Target: {target}')
print(llist._values)
