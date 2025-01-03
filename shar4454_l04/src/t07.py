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
from utilities import list_test
# Constants

source = []
for i in range(20):
    source.append(i)
"""
fh = open("movies.txt", "r", encoding='utf-8')
for line in fh:
    row = line.strip().split("|")
    source.append(row)
fh.close()
"""
list_test(source)
