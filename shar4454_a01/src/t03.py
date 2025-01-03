"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ashish Sharma
ID:      169044454
Email:   shar4454@mylaurier.ca
__updated__ = "2023-01-22"
-------------------------------------------------------
"""
# Imports
from functions import find_subs
# Constants

string = input('String: ')
sub = input('Sub: ')
locations = find_subs(string, sub)
print(locations)
