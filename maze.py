import time, random
from cell import Cell
from graphics import Point

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()
        if seed is not None:
            self._seed = random.seed(seed)
    
    def _create_cells(self):
        if self._win is None:
            return
        for i in range(self._num_cols):
            col = []
            for j in range(self._num_rows):
                col.append(Cell(self._win))
            self._cells.append(col)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

    def _draw_cell(self, i, j):
        x1 = self._x1 + (i * self._cell_size_x)
        y1 = self._y1 + (j * self._cell_size_y)
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True
        while True:
            to_visit = []
            if i + 1 < self._num_cols and not self._cells[i + 1][j].visited:
                to_visit.append((i + 1, j))
            if i - 1 < self._num_cols and i - 1 > 0 and not self._cells[i - 1][j].visited:
                to_visit.append((i - 1, j))
            if j + 1 < self._num_rows and not self._cells[i][j + 1].visited:
                to_visit.append((i, j + 1)) 
            if j - 1 < self._num_cols and j - 1 > 0 and not self._cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
            if to_visit == []:
                self._draw_cell(i, j)
                return
            direction = random.randint(0, len(to_visit) - 1)
            chosen_cell = self._cells[to_visit[direction][0]][to_visit[direction][1]]
            if current_cell._x2 == chosen_cell._x1 and current_cell._y1 == current_cell._y1:
                current_cell.has_right_wall = False
                chosen_cell.has_left_wall = False
            if current_cell._x1 == chosen_cell._x2 and current_cell._y1 == current_cell._y1:
                current_cell.has_left_wall = False
                chosen_cell.has_right_wall = False
            if current_cell._y2 == chosen_cell._y1 and current_cell._x1 == current_cell._x2:
                current_cell.has_bottom_wall = False
                chosen_cell.has_top_wall = False
            if current_cell._y1 == chosen_cell._y2 and current_cell._x1 == current_cell._x2:
                current_cell.has_top_wall = False
                chosen_cell.has_bottom_wall = False
            self._draw_cell(i, j)
            self._break_walls_r(to_visit[direction][0], to_visit[direction][1])
            
          