"""
-------------------------------------------------------
Tests various array-based sorting functions.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 C
__updated__ = "2023-04-01"
-------------------------------------------------------
"""
# Imports
from random import *
from Number import Number
from Sorts_array import Sorts

# Constants
SIZE = 100  # Size of array to sort.
XRANGE = 1000  # Range of values in random arrays to sort.
TESTS = 100  # Number of random arrays to generate.

SORTS = (
    ('Bubble Sort', Sorts.bubble_sort),
    ('Insertion Sort', Sorts.insertion_sort),
    ('Merge Sort', Sorts.merge_sort),
    ('Quick Sort', Sorts.quick_sort),
    ('Selection Sort', Sorts.selection_sort),
    ('Bin. Ins. Sort', Sorts.binary_insert_sort),
    ('BST Sort', Sorts.bst_sort),
    ('Cocktail Sort', Sorts.cocktail_sort),
    ('Comb Sort', Sorts.comb_sort),
    ('Heap Sort', Sorts.heap_sort),
    ('Shell Sort', Sorts.shell_sort)
)


def create_sorted():
    """
    -------------------------------------------------------
    Creates a sorted list of SIZE Number objects with values
        from 0 up to SIZE-1.
    Use: values = create_sorted()
    -------------------------------------------------------
    Returns:
        values - a sorted list of SIZE Number objects (list of Number)
    -------------------------------------------------------
    """

    # your code here
    values = []

    for i in range(SIZE):
        values.append(Number(i))

    return values


def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed list of SIZE Number objects with values
        from SIZE-1 down to 0.
    Use: values = create_reversed()
    -------------------------------------------------------
    Returns:
        values - a reversed list of SIZE Number objects (list of Number)
    -------------------------------------------------------
    """

    # your code here
    a = create_sorted()
    values = a[::-1]

    return values


def create_randoms():
    """
    -------------------------------------------------------
    Create a 2D list of Number objects with TESTS rows and
    SIZE columns of values between 0 and XRANGE.
    Use: lists = create_randoms()
    -------------------------------------------------------
    Returns:
        arrays - TESTS lists of SIZE Number objects containing
            values between 0 and XRANGE (list of list of Number)
    -------------------------------------------------------
    """

    # your code here
    arrays = []
    rows = TESTS
    cols = TESTS

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append((Number(randint(0, XRANGE))))
        arrays.append(row)

    return arrays


def test_sort(title, func):
    """
    -------------------------------------------------------
    Test a sort function with Number data and prints the number 
    of comparisons necessary to sort an array:
    in order, in reverse order, and a list of arrays in random order.
    Use: test_sort(title, func)
    -------------------------------------------------------
    Parameters:
        title - name of the sorting function to call (str)
        func - the actual sorting function to call (function)
    Returns:
        None
    -------------------------------------------------------
    """

    # your code here
    in_order = create_sorted()
    reverse_order = create_reversed()
    rand_order = create_randoms()

    Number.comparisons = 0
    Sorts.swaps = 0
    for i in rand_order:
        func(i)
    rand_comparisons = Number.comparisons // SIZE
    rand_swaps = Sorts.swaps // SIZE

    Number.comparisons = 0
    Sorts.swaps = 0
    func(in_order)
    inorder_comparisons = Number.comparisons
    inorder_swaps = Sorts.swaps

    Number.comparisons = 0
    Sorts.swaps = 0
    func(reverse_order)
    reverse_comparisons = Number.comparisons
    reverse_swaps = Sorts.swaps

    print("{:14} {:8} {:8} {:8} {:8.1f} {:8.1f} {:8.1f}".format(title, inorder_comparisons,
                                                                reverse_comparisons, rand_comparisons, inorder_swaps, reverse_swaps, rand_swaps))

    return
