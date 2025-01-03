"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ashish Sharma
ID:      169044454
Email:   shar4454@mylaurier.ca
__updated__ = "2023-04-03"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST
# Constants

b = BST()
b.insert(2)
b.insert(10)
b.insert(22)
b.insert(7)
b.insert(1)
b.insert(3)
print(b.node_counts())
