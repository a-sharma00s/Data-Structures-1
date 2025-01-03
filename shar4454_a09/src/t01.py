"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ashish Sharma
ID:      169044454
Email:   shar4454@mylaurier.ca
__updated__ = "2023-04-03"
-------------------------------------------------------
"""
# Imports
from Hash_Set_array import Hash_Set
from functions import insert_words, comparison_total
# Constants

hs = Hash_Set(20)
fv = open("gibbon.txt", encoding="utf-8")
insert_words(fv, hs)
total, max_word = comparison_total(hs)
fv.close()

for slot in hs._table:
    for item in slot:
        print(item)

print('Using array-based list Hash_Set')
print(f'Total Comparisons: {total} ')
print(f'Word with maximum compariosns: {max_word}: {max_word.comparisons}')
