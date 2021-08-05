import time
from functools import wraps

def show_process_time(method):
    """(5 pts) Method decorator

    Show the processing time of the decorated method
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        pass

    return wrapper


class Sudoku:
    """Sudoku solver

    A sudoku is represented by a 9x9 matrix. Each element
    in the matrix is an integer value from 1 to 9.

    For example:

            columns
                                      +-----+    +-----+   +-----+
       9,5,7,6,1,3,2,8,4              |9,5,7|    |6,1,3|   |2,8,4|
       4,8,3,2,5,7,1,9,6              |4,8,3|    |2,5,7|   |1,9,6|
    r  6,1,2,8,4,9,5,3,7              |6,1,2|    |8,4,9|   |5,3,7|
    o  1,7,8,3,6,4,9,5,2   ------->   +-----+    +-----+   +-----+
    w  5,2,4,9,7,1,3,6,8   ------->   block0     block1    block2
    s  3,6,9,5,2,8,7,4,1
       8,4,5,7,9,2,6,1,3              +-----+    +-----+   +-----+
       2,9,1,4,3,6,8,7,5              |1,7,8|    |3,6,4|   |9,5,2|
       7,3,6,1,8,5,4,2,9              |5,2,4|    |9,7,1|   |3,6,8|
                                      |3,6,9|    |5,2,8|   |7,4,1|
                                      +-----+    +-----+   +-----+
                                      block3     block4    block5

                                      +-----+    +-----+   +-----+
                                      |8,4,5|    |7,9,2|   |6,1,3|
                                      |2,9,1|    |4,3,6|   |8,7,5|
                                      |7,3,6|    |1,8,5|   |4,2,9|
                                      +-----+    +-----+   +-----+
                                      block6     block7    block8

    A finished sudoku must satisfy following requirements:
        1. Each row consists of a sequence of numbers from 1 to 9
            ,and each digit can only occur once
        2. Each col consists of a sequence of numbers from 1 to 9
            ,and each digit can only occur once
        3. Each block consists of a sequence of numbers from 1 to 9
            ,and each digit can only occur once

    Argument:
        fname (str): sudoku file name
    """
    def __init__(self, fname):
        """(5 pt) Construct the sudoku 2D matrix from file named as 'fname'"""
        pass

    def __str__(self):
        """(5 pt) Return printable string representing current sudoku 2D matrix

        For example:

            9 5 7 6 1 3 2 8 4
            4 8 3 2 5 7 1 9 6
            6 1 2 8 4 9 5 3 7
            1 7 8 3 6 4 9 5 2
            5 2 4 9 7 1 3 6 8
            3 6 9 5 2 8 7 4 1
            8 4 5 7 9 2 6 1 3
            2 9 1 4 3 6 8 7 5
            7 3 6 1 8 5 4 2 9
        """
        pass

    def check_block(self, block_idx):
        """(10 pt) Return True if the block with index 'block_idx' is valid

        Note:
            Refer the docstring of the Sudoku class. `block_idx` is an integer from 0 to 8.
            valid means no repeated numbers in the block except 0
        """
        pass

    def check_row(self, row_idx):
        """(5 pt) Return True if the row with index 'row_idx' is valid

        Note:
            Refer the docstring of the Sudoku class. `row_idx` is an integer from 0 to 8.
            valid means no repeated numbers in the row except 0
        """
        pass

    def check_col(self, col_idx):
        """(5 pt) Return True if the col with index 'col_idx' is valid

        Note:
            Refer the docstring of the Sudoku class. `col_idx` is an integer from 0 to 8.
            valid means no repeated numbers in the col except 0
        """
        pass

    def is_solved(self):
        """(5 pt) Return True if the sudoku is solved

        Note:
            A solve sudoku must satisfy following requirements:
                1. Each row consists of a sequence of numbers from 1 to 9
                    ,and each digit can only occur once
                2. Each col consists of a sequence of numbers from 1 to 9
                    ,and each digit can only occur once
                3. Each block consists of a sequence of numbers from 1 to 9
                    ,and each digit can only occur once
        """
        pass

    # Uncomment the line below when you finish the decorator show_process_time
    # @show_process_time
    def solve(self):
        """(60 pt) Solve the sudoku puzzle automatically

        Note:
            You can define others functions inside this method to help you solve the puzzle
        """
        pass
