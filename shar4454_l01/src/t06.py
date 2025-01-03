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
from Movie_utilities import read_movie
# Constants

line = 'Incredibly Strange Creatures Who Stopped Living and Became Mixed-Up Zombies!!?, The|1964|Ray Dennis Steckler|2.2|8'
movie = read_movie(line)
print(movie)

"""
Hard code/testing
# Treating line as a file line
line = 'Dellamorte Dellamore|1994|Michele Soavi|7.2|3,4,5,8'
movie_details = line.split('|')
# preview split data
print(movie_details)
print('-' * 80)
# retrieve data by index and set as appropriate values
title = movie_details[0]
year = int(movie_details[1])
director = movie_details[2]
rating = float(movie_details[3])
# split string list
genre_codes = movie_details[4].split(',')
genres = []
# preview
print(genre_codes)
print('-' * 40)
# iterate through string list and add values as integers
for number in genre_codes:
    genres.append(int(number))
# preview data
print(genres)
print(f'Title: {title}')
print(f'Year: {year}')
print(f'Director: {director}')
print(f'Rating: {rating}')
print(f'Genres: {genres}')
print('-' * 40)
# create object with given data
movie = Movie(title, year, director, rating, genres)
# print object
print(movie)
"""
