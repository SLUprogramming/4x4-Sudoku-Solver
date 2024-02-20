import unittest
from sudoku_solver import instructions, unfilled, check_valid_input

class TestSudokuSolver(unittest.TestCase):
    def test_instructions(self):
        # Redirect stdout to a StringIO object to capture the printed output
        import sys
        from io import StringIO
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the instructions function
        instructions()

        # Reset the stdout
        sys.stdout = sys.__stdout__

        # Get the printed output
        printed_message = captured_output.getvalue()

        # Define the expected message
        expected_message = "This program solves 2x2 sudoku puzzles"

        # Assert that the expected message is in the printed output
        self.assertIn(expected_message, printed_message)

    def test_unfilled(self):
        # Test if the unfilled function correctly returns unfilled blocks
        all_blocks = {'a1': ' ', 'a2': ' ', 'b1': ' ', 'b2': ' '}
        unfilled_blocks = list(all_blocks.keys())
        self.assertEqual(unfilled_blocks, ['a1', 'a2', 'b1', 'b2'])

    def test_check_valid_input(self):
        # Test if the check_valid_input function returns False for an invalid input
        self.assertTrue(check_valid_input('a2', '1'))

if __name__ == "__main__":
    unittest.main()
