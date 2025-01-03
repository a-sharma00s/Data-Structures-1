"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ashish Sharma
ID:      169044454
Email:   shar4454@mylaurier.ca
__updated__ = "2023-03-13"
-------------------------------------------------------
"""
# Imports
from Deque_linked import Deque
# Constants
d = Deque()
for i in range(5):
    d.insert_front(i)

for j in d:
    print(i, end=" ")
