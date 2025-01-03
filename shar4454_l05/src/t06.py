"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ashish Sharma
ID:      169044454
Email:   shar4454@mylaurier.ca
__updated__ = "2023-02-18"
-------------------------------------------------------
"""
# Imports
from functions import bag_to_set
# Constants

bag = [4, 5, 3, 4, 5, 2, 2, 4]
print(f'Old List: {bag}')
new_set = bag_to_set(bag)
print(f'New List: {new_set}')
