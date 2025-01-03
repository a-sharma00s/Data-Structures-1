"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ashish Sharma
ID:      169044454
Email:   shar4454@mylaurier.ca
__updated__ = "2023-02-12"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_array import Priority_Queue
# Constants
source = Priority_Queue()
source.insert(10)
source.insert(1)
source.insert(5)
source.insert(25)
source.insert(0)
print(f'source: {source._values}')
key = 5
print(f'key: {key}')
target1, target2 = source.split_key(key)
print(f'target1: {target1._values}')
print(f'target2: {target2._values}')
