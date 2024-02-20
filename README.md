# 2x2-Sudoku-Solver
  User-friendly script that solves 2x2 sudoku puzzles using brute-force approach.

# A 2x2 sudoku puzzle has the following form:
    #       
    # a1 a2 | a3 a4
    # b1 b2 | b3 b4
    # -------------      
    # c1 c2 | c3 c4
    # d1 d2 | d3 d4
    #
    # Where an, bn, cn, dn represent numbers
    # ranging in value from 1 to 4. Rows span 
    # 4 consecutive numbers horizontally, 
    # columns span 4 consecutive numbers 
    # vertically, and the 4 squares contain 4
    # each. They are visualized above.
    # Each row, column, and square may only
    # contain one instance of each number
    # meaning no duplicates of a number are 
    # allowed to be present in a single row,
    # column, or square.

## How to Use
  1. **Input**: Run the program and input the values for each block of the puzzle following the prompts.
  2. **Solver**: The program will attempt to solve the puzzle using brute-force approach.
  3. **Output**: If a solution is found, it will display the solved puzzle.

## Unit Testing
Unit tests are included (unittest.py) to ensure the correctness of the solver functions. You can run the unit tests using the `unittest` framework.

## Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests with your improvements.

## License
This project is licensed under the [GNU General Public License](LICENSE.txt).

## Installation
To run the solver locally, follow these steps:

  1. Clone the repository:
  git clone https://github.com/SLUprogramming/2x2-Sudoku-Solver.git

  2. Navigate to the project directory:
  cd 2x2-Sudoku-Solver

  3. Run the program:
  python main.py
