"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ashish Sharma
ID:      169044454
Email:   shar4454@mylaurier.ca
__updated__ = "2023-02-20"
-------------------------------------------------------
"""
# Imports
from Sorted_List_array import Sorted_List
from Movie import Movie
# Constants
target = Sorted_List()
m1 = Movie("Dellamorte Dellamore", 1994, "Michele Soavi", 7.2, [3, 4, 5, 8])
m2 = Movie("Dark City", 1998, "Alex Proyas", 7.8, [0])
m3 = Movie("I Am Legend", 2007, "Francis Lawrence", 7.1, [0, 6])
target2 = Sorted_List()
m4 = Movie("Spider-Man 3", 2007, "Sam Raimi", 7.5, [6])
m5 = Movie("Man Thing", 2019, "Sammy Man", 3.5, [0, 2, 8])
m6 = Movie("Man", 2000, "Man", 9.5, [1, 2, 6])
target._values.insert(m1)
target._values.insert(m2)
target._values.insert(m3)
target.insert(m4)
target.insert(m5)
target.insert(m6)
target.insert(m7)
target.insert(m8)
target.insert(m9)
print(target._values)
print(target2._values)

# Testing
b = m5 in target
print(b)

equals = target == target2
print(equals)

i = 1
value = target[i]
print(value)
