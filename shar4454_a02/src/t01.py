"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ashish Sharma
ID:      169044454
Email:   shar4454@mylaurier.ca
__updated__ = "2023-01-29"
-------------------------------------------------------
"""
# Imports
from Movie_utilities import get_by_year, read_movies
# Constants

fv = open("movies.txt", "r", encoding="utf-8")
movies = read_movies(fv)
print('Movies Unchanged')
print("-" * 80)
for i in movies:
    print(i)
print("-" * 80)

year = int(input('Search for movies by year: '))
ymovies = get_by_year(movies, year)

print(f'Movies by Year: {year}')
print("-" * 80)
for i in ymovies:
    print(i)
print("-" * 80)

fv.close()
