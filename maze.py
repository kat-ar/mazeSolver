from cell import Cell
import time


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size, win=None):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size = cell_size
        self._win = win

        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        for _ in range(self._num_cols):
            col_cells = []
            for _ in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for col in range(self._num_cols):
            for row in range(self._num_rows):
                self._draw_cells(col, row)

    def _draw_cells(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size
        y1 = self._y1 + j * self._cell_size
        x2 = x1 + self._cell_size
        y2 = y1 + self._cell_size
        self._cells[i][j].draw_cell(x1, y1, x2, y2)
        self._animate()
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cells(0,0)
        self._cells[self._num_cols-1][self._num_rows-1].has_bottom_wall = False
        self._draw_cells(self._num_cols-1,self._num_rows-1)
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)
