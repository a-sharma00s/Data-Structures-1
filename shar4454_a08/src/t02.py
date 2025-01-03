"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ashish Sharma
ID:      169044454
Email:   shar4454@mylaurier.ca
__updated__ = "2023-03-27"
-------------------------------------------------------
"""
# Imports
from functions import do_comparisons, comparison_total
from Letter import *
from BST_linked import BST
# Constants


DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"

bst = BST()
for i in DATA1:
    bst.insert(Letter(i))

fh = open("gibbon.txt", "r", encoding="utf-8")
fh.close()

total = comparison_total(bst)
print(f'Comparison total: {total}')
