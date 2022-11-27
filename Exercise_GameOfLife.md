# Kata Game of Life

## Background
The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970.

## Exercise
Initially, there is a grid with some cells which may be alive or dead. Our task is to generate the next generation of cells based on the following rules: 

### Rules
The board is made up of a 2 dimensional grid of cells (like an infinite chessboard).
Each cell has an initial state: live or dead/empty. 
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal).
A cell dies of continues to life or is born from an empty cell using the following four rules

* Any live cell with fewer than 2 live neighbors dies as if caused by underpopulation.
* Any live cell with 2 or 3 live neighbors lives on to the next generation.
* Any live cell with more than 3 live neighbors dies, as if by overpopulation.
* Any dead cell with exactly 3 live neighbors becomes a live cell, as if by reproduction.

The next generation of cells are calculated based on the current generation.

### Example
*Generation 1
|   | X |   |
|   |   | X |
| X | X | X |
|   |   |   |

*Generation 2
|   |   |   |
| X |   | X |
|   | X | X |
|   | x |   |
