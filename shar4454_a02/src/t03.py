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
from Movie_utilities import read_movies, get_by_genre
# Constants

fv = open("movies.txt", "r", encoding="utf-8")
movies = read_movies(fv)
print('Movies Unchanged')
print("-" * 80)
for i in movies:
    print(i)
print("-" * 80)

genre = int(input('Search for movies by genre: '))
gmovies = get_by_genre(movies, genre)

print(f'Movies by Genre: {genre}')
print("-" * 80)
for i in gmovies:
    print(i)
print("-" * 80)

fv.close()
