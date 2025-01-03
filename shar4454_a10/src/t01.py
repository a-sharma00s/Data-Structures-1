"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ashish Sharma
ID:      169044454
Email:   shar4454@mylaurier.ca
__updated__ = "2023-04-10"
-------------------------------------------------------
"""
# Imports
from Sorts_array import Sorts
# Constants
print("Before: ")
arr = [12, 43, 65, 98, 57, 4, 8, 25, 33, 41]
print(arr)
Sorts.radix_sort(arr)
print()
print("After: ")
print(arr)
