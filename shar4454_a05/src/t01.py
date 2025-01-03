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
from List_array import List
from Movie import Movie
# Constants

# 1) __eq__ method test
print('Testing: __eq__')
# testing with numbers
target = List()
arr = List()

for i in range(10):
    target.append(i)
    arr.append(i)

print(f'array: {arr._values}')
print(f'target: {target._values}')
equals = (target == arr)
print(f'equal: {equals}')
print()
# testing with movie objects
movie1 = Movie("Dark City", 1998, "Alex Proyas", 7.8, [0])
movie2 = Movie("I Am Legend", 2007, "Francis Lawrence", 7.1, [0, 6])
print(f'{movie1}')
print()
print(f'{movie2}')
movie_equals = (movie1 == movie2)
print(f'movies equal: {movie_equals}')
# empty list test
print()
blank_1 = List()
blank_2 = List()
blank_eq = (blank_1 == blank_2)
print(f'list one: {blank_1._values}')
print(f'list two: {blank_2._values}')
print(f'equal: {blank_eq}')
print()
# end of __eq__ testing

# 2) Testing __get__item
print('Testing: __getitem__')
source = List()
# test with movie objects
source.append(movie1)
source.append(movie2)
i = 1
value = source[i]
print(f'item at index {i}:')
print(value)
print()
# end of __getitem__ testing

# 3) testing append
print('Testing append')
numbers = List()
print(f'before append: {numbers._values}')
numbers.append(1)
numbers.append(2)
numbers.append(3)
print(f'after append: {numbers._values}')
# test with movie objects:
print()
print('source before: ')
for i in source:
    print(i)
    print()
movie3 = Movie("Spider-Man 3", 2007, "Sam Raimi", 7.5, [6])
source.append(movie3)
print('source after: ')
for i in source:
    print(i)
    print()
# end of append

# 4) testing clean
print('Testing clean...')
for i in range(4):
    numbers.append(10)
print(f'numbers before: {numbers._values}')
numbers.clean()
print(f'numbers after: {numbers._values}')
# testing with movie objects
for i in range(4):
    source.append(movie3)
print('source before: ')
for i in source:
    print(i)
    print()
source.clean()
print('source after: ')
for i in source:
    print(i)
    print()
# end of combine

# 5) testing intersection
print('Testing intersection...')
s1 = [5, 5, 5, 1, 2, 3]
s2 = [4, 5, 6, 1, 2, 3]
s_list = List()
print(f'list before intersection: {s_list._values}')
s_list.intersection(s1, s2)
print(f'list after: {s_list._values}')
print()
# test with movie objects
movie4 = Movie("Man Thing", 2019, "Sammy Man", 3.5, [0, 2, 8])
mov_test = List()
m1 = []
m2 = []
m1.append(movie1)
m1.append(movie2)
m1.append(movie3)
m2.append(movie3)
m2.append(movie4)
m2.append(movie4)
m2.append(movie4)
mov_test.intersection(m1, m2)
for i in mov_test:
    print(i)
print()
# end of intersection

# 6) Testing prepend
print('Testing prepend...')
print(s_list._values)
s_list.prepend(6)
print(s_list._values)
print()
# testing with movie data
movie5 = Movie("Man", 2000, "Man", 9.5, [1, 2, 6])
source.prepend(movie5)
for i in source:
    print(i)
# end of prepend

# 7) Testing remove_front
print()
print('Testing remove front...')
# testing with movie data
print('Before:')
for i in source:
    print(i)
source.remove_front()
print()
print('After:')
for i in source:
    print(i)
# end of remove_front

# 8) Testing remove_many
print()
print('Testing remove_many')
new_movie = Movie("Attacked Squirrel", 2023, "Moon", 10.0, [7])
nm_lst = List()
for i in range(4):
    nm_lst.append(new_movie)
nm_lst.remove_many(new_movie)
nm_lst.append(movie5)
for i in nm_lst:
    print(i)
# end of remove_many

# 9) Testing split
