"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ashish Sharma
ID:      169044454
Email:   shar4454@mylaurier.ca
__updated__ = "2023-02-06"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from enum import Enum
# Constants
OPERATORS = "+-*/"
MIRRORED = Enum('MIRRORED',
                {'IS_MIRRORED': "is a mirror", 'TOO_MANY_LEFT': "too many characters in L",
                 'TOO_MANY_RIGHT': "too many characters in R", 'MISMATCHED': "L and R don't match",
                 'INVALID_CHAR': "invalid character", 'NOT_MIRRORED': "no mirror character"})


def stack_split_alt(source):
    """
    -------------------------------------------------------
    Splits the source stack into separate target stacks.
    When finished source stack is empty. Values are
    pushed alternately onto the returned target stacks.
    Use: target1, target2 = stack_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - the stack to split into two parts (Stack)
    Returns:
        target1 - contains alternating values from source (Stack)
        target2 - contains other alternating values from source (Stack)
    -------------------------------------------------------
    """
    target1 = Stack()
    target2 = Stack()
    alternate = False

    for i in source:
        if alternate == False:
            target1.push(source.pop())
            alternate = True
        else:
            target2.push(source.pop())
            alternate = False

    return target1, target2


def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    palindrome = True
    s = Stack()
    string = string.lower()
    letters = ""
    count = 0
    for i in string:
        if i.isalpha():
            s.push(i)
            letters += i

    n = len(letters)
    while count < n and not s.is_empty():
        if s.pop() != letters[count]:
            palindrome = False
        count += 1

    return palindrome


def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    s = Stack()
    for i in string.split():
        if i.isdigit():
            s.push(float(i))
        elif i in OPERATORS:
            a = s.pop()
            b = s.pop()
            if i == '+':
                c = b + a
            elif i == '-':
                c = b - a
            elif i == '*':
                c = b * a
            elif i == '/':
                c = b / a
            s.push(c)
        else:
            answer = "invalid operators"
    answer = s.pop()
    return answer


def stack_maze(maze):
    """
    -------------------------------------------------------
    Solves a maze using Depth-First search.
    Use: path = stack_maze(maze)
    -------------------------------------------------------
    Parameters:
        maze - dictionary of points in a maze, where each point
            represents a corridor end or a branch. Dictionary
            keys are the name of the point followed by a list of
            branches, if any. First point is named 'Start', exit
            is named 'X' (dict)
    Returns:
        path - list of points visited before the exit is reached,
            None if there is no exit (list of str)
    -------------------------------------------------------
    """
    s = Stack()
    path = []
    end = {}
    key = "Start"

    s.push(key)
    end[key] = []
    check = s.is_empty()

    while check == False:
        current = s.pop()
        path.append(current)
        if current == 'X':
            return path
        for i in maze.get(current, []):
            if i not in end:
                s.push(i)
                end[i] = path

    return path


def is_mirror_stack(string, valid_chars, m):
    """
    -------------------------------------------------------
    Determines if string is a mirror of characters in valid_chars around the pivot m.
    A mirror is of the form LmR, where L is the reverse of R, and L and R
    contain only characters in valid_chars.
    Use: mirror = is_mirror_stack(string, valid_chars, m)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
        valid_chars - a string of valid characters (str)
        m - the mirror pivot string (str - one character not in valid_chars)
    Returns:
        mirror - the state of the string (Enum MIRRORED)
    -------------------------------------------------------
    """
    assert m not in valid_chars, \
        f"cannot use '{m}' as the mirror character"
    mirror = MIRRORED.IS_MIRRORED
    stack = Stack()
    n = len(string)
    i = 0

    while i < n and string[i] != m:
        if string[i] in valid_chars:
            stack.push(string[i])
            i += 1
        else:
            mirror = MIRRORED.INVALID_CHAR

    # skip over the mirror character
    i += 1

    while mirror and i < n and not stack.is_empty():
        c = stack.pop()
        if string[i] != c:
            mirror = MIRRORED.MISMATCHED
        else:
            i += 1

    # check final conditions
    if not (i == n and stack.is_empty()):
        mirror = MIRRORED.NOT_MIRRORED
    return mirror
