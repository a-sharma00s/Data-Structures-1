"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ashish Sharma
ID:      169044454
Email:   shar4454@mylaurier.ca
__updated__ = "2023-03-27"
-------------------------------------------------------
"""
# Imports
from BST_linked import *
# Constants

# testing __eq__
bst1 = BST()
bst2 = BST()
for i in range(10):
    bst1.insert(i)
for i in range(5):
    bst2.insert(i)

equals = (bst1 == bst2)
print(equals)
print(bst1.is_balanced())
