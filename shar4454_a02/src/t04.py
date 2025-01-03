"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ashish Sharma
ID:      169044454
Email:   shar4454@mylaurier.ca
__updated__ = "2023-01-30"
-------------------------------------------------------
"""
# Imports
from Movie_utilities import read_movies, get_by_genres
# Constants

fv = open("movies.txt", "r", encoding="utf-8")
movies = read_movies(fv)
print('Movies Unchanged')
print("-" * 80)
for i in movies:
    print(i)
print("-" * 80)

genres = [0, 6]
m = get_by_genres(movies, genres)

print(f'Movies by Genre code: {genres}')
print("-" * 80)
for i in m:
    print(i)
print("-" * 80)

fv.close()
