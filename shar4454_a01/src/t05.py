"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ashish Sharma
ID:      169044454
Email:   shar4454@mylaurier.ca
__updated__ = "2023-01-23"
-------------------------------------------------------
"""
# Imports
from functions import is_valid
# Constants

name = input('variable: ')
valid = is_valid(name)
print(f'{name} : {valid}')
