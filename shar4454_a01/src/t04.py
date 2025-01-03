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
from functions import is_leap_year
# Constants

year = int(input('Year: '))
leap_year = is_leap_year(year)
print(leap_year)
