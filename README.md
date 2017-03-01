#xSudoku 

**xSudoku**
xSudoku is a variant of Sudoku. Just like Sudoku, it is usually played on a 9 x 9 grid. The goal is to fill up numbers 1 to 9 in the grid such that the rows, columns and each of the 3 x 3 grids have the numbers 1 to 9. In addition to the usual Sudoku constraints, the two diagonals should also have unique numbers. Some numbers will be given at the beginning to start off, the goal is to complete the board while satisfying these constraints.

<img src='http://i.imgur.com/nVDren1.png' title='Sudoku' width='' alt='Overview' />

**Implementation Description**
In this project, we are to implement CSP (Constraint Satisfaction Problem) to solve sudoku. CSP's goal is to find a solution that satisfies certain constraints, in which the problem is defined by a new set of variables, their domains, and a set of constraint they need to follow. The constraints can involve one, two, or multiple variables at a time. 
