"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ashish Sharma
ID:      169044454
Email:   shar4454@mylaurier.ca
__updated__ = "2023-02-13"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue
from functions import queue_combine
# Constants


# insert content into 2 new queues
source1 = Queue()
source1.insert(5)
source1.insert(8)

source2 = Queue()
source2.insert(7)
source2.insert(9)
source2.insert(14)
print(f'Source1: {source1._values}')
print(f'Source2: {source2._values}')

# apply method
target = queue_combine(source1, source2)

print(f'Target: {target._values}')
