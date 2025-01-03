"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ashish Sharma
ID:      169044454
Email:   shar4454@mylaurier.ca
__updated__ = "2023-01-20"
-------------------------------------------------------
"""
# Imports
from Movie_utilities import read_movies
# Constants

fv = open('movies.txt', "r", encoding="utf-8")
movies = read_movies(fv)

for i in movies:
    print(f'{i} \n')

fv.close()
