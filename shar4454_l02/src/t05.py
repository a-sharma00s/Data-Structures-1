"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ashish Sharma
ID:      169044454
Email:   shar4454@mylaurier.ca
__updated__ = "2023-01-28"
-------------------------------------------------------
"""
# Imports
from utilities import stack_test
# Constants
lst = []

fh = open("movies.txt", "r", encoding="utf-8")
for line in fh:
    data = line.strip().split("|")
    lst.append(data)

stack_test(lst)
fh.close()
# print(lst)
