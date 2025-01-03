"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ashish Sharma
ID:      169044454
Email:   shar4454@mylaurier.ca
__updated__ = "2023-02-04"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_array import Priority_Queue
from utilities import array_to_pq, pq_to_array, priority_queue_test
# Constants

pq = Priority_Queue()
source = []

fh = open("movies.txt", "r", encoding='utf-8')

for line in fh:
    row = line.strip().split("|")
    source.append(row)
fh.close()

# pq test
priority_queue_test(source)

print('-' * 100)

# array to pq
print(f"Priority Queue [Before]: {pq}")
print(f'Source [Before]: {source}')
array_to_pq(pq, source)
print(f"Priority Queue [After]:")
for i in pq:
    print(i)
print(f'Source after: {source}')

print('-' * 100)

# pq to array
target = []
print(f"Target [Before]: {target}")
pq_to_array(pq, target)
print(f"Target [After]: {target}")
print(f"pq empty: {pq.is_empty()}")
