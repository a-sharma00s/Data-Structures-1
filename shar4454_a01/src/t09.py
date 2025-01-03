"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ashish Sharma
ID:      169044454
Email:   shar4454@mylaurier.ca
__updated__ = "2023-01-23"
-------------------------------------------------------
"""
# Imports
from functions import shift
# Constants

estring = shift("abcdef", 1)
print(estring)

n = 1
fh = open("pelee.txt", "r", encoding="utf-8")
fv = open("shift.txt", "w", encoding="utf-8")

line = fh.readline()
data = line.strip().split()

while line != "":
    for word in data:
        shifted_word = shift(word, n)
        fv.write(f"{shifted_word}\n")
    line = fh.readline()

fh.close()
fv.close()

"""
values = [40, 50, 60, 70]
print(values)
e = []

for number in values:
    number = chr(number)
    e.append(number)

print(e)
"""
