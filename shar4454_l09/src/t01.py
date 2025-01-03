"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ashish Sharma
ID:      169044454
Email:   shar4454@mylaurier.ca
__updated__ = "2023-03-25"
-------------------------------------------------------
"""
# Imports
from functions import hash_table
# Constants

lst = []
with open("movies.txt", "r", encoding='utf-8') as fv:
    for line in fv:
        lst.append(line.strip())


hash_table(7, lst)
