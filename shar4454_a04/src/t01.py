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
from Queue_circular import Queue

# Constants
source = Queue()
target = Queue()
for i in range(10):
    source.insert(i + 1)
    target.insert(i + 1)
print(f'source: {source._values}')
print(f'target: {target._values}')
source_empty = source.is_empty()
target_empty = target.is_empty()
print(f'source empty: {source_empty}')
print(f'target empty: {target_empty}')
source_full = source.is_full()
target_full = target.is_full()
print(f'source full: {source_full}')
print(f'target full: {target_full}')
n = len(source)
m = len(target)
print(f'source length: {n}')
print(f'target length: {m}')
equals = source == target
print(f'source = target: {equals}')
v = source.remove()
print(f'removed from source: {v}')
print(f'source now: {source._values}')
p = target.peek()
print(f'peeking target: {p}')
