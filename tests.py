import unittest
from maze import Maze
from graphics import Window

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 10
        num_rows = 12
        m1 = Maze(10, 10, num_rows, num_cols, 10, 10, Window(800, 800))
        test = len(m1._cells)
        expected = num_cols
        self.assertEqual(test, expected)
        test = len(m1._cells[0])
        expected = num_rows
        self.assertEqual(test, expected)

    def test_maze_create_cells2(self):
        num_cols = 20
        num_rows = 8
        m1 = Maze(10, 10, num_rows, num_cols, 10, 10, Window(800, 800))
        test = len(m1._cells)
        expected = num_cols
        self.assertEqual(test, expected)
        test = len(m1._cells[0])
        expected = num_rows
        self.assertEqual(test, expected)

    def test_maze_break_entrance_and_exit(self):
        num_cols = 10
        num_rows = 12
        m1 = Maze(10, 10, num_rows, num_cols, 10, 10, Window(800, 800))
        test = m1._cells[0][0].has_top_wall
        expected = False
        self.assertEqual(test, expected)
        test = m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall
        expected = False
        self.assertEqual(test, expected)

    def test_maze_break_entrance_and_exit2(self):
        num_cols = 10
        num_rows = 12
        m1 = Maze(10, 10, num_rows, num_cols, 10, 10, Window(800, 800))
        test = m1._cells[0][0].has_top_wall
        expected = False
        self.assertEqual(test, expected)
        test = m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall
        expected = False
        self.assertEqual(test, expected)
        

if __name__ == "__main__":
    unittest.main()