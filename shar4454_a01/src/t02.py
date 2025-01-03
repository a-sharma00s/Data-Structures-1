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
from functions import file_analyze
# Constants

fv = open('randomtext.txt', 'r', encoding="utf-8")

u, l, d, w, r = file_analyze(fv)
print(f'{u} {l} {d} {w} {r}')
fv.close()
