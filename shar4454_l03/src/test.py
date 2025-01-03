"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ashish Sharma
ID:      169044454
Email:   shar4454@mylaurier.ca
__updated__ = "2023-02-03"
-------------------------------------------------------
"""
# Imports
from utilities import queue_to_array, array_to_queue
from Queue_array import Queue
# Constants

queue = Queue()
source = [1, 2, 3, 4, 5]
print(f'Before: {source}')
print(f'Empty queue: {queue.is_empty()}')
array_to_queue(queue, source)
print(f'After: {source}')
print('Queue contents:')
for i in queue:
    print(i)
print('End of queue')
print(f'Empty queue: {queue.is_empty()}')

target = []
queue_to_array(queue, target)
print(f'Target: {target}')
