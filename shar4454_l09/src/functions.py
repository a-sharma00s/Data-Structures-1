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
from Movie import *
# Constants


def hash_table(slots, values):
    """
    -------------------------------------------------------
    Print a hash table of a set of values. The format is:
    Hash     Slot Key
    -------- ---- --------------------
    1652346    3 Dark City, 1998
    848448    6 Zulu, 1964
    Do not create an actual Hash_Set.
    Use: hash_table(slots, values)
    -------------------------------------------------------
    Parameters:
       slots - the number of slots available (int > 0)
       values - the values to hash (list of ?)
    Returns:
       None
    -------------------------------------------------------
    """
    print('Hashes')
    print('Hash    Slot    Key')
    print('-' * 80)
    for i in range(len(values)):
        h = hash(values[i])
        key = values[i]
        slot = h % slots
        print(f'{h}    {slot}    {key}')
    return
