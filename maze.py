from cell import Cell
import time, random


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size, win=None, seed=None):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size = cell_size
        self._win = win
        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

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
        self._animate(time_sleep_secs=0.005)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cells(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cells(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            possible_directions = 0
            next_index_list = []  # list of tuples

            # decide if we can move in a direction:
            # left
            if i > 0 and not self._cells[i - 1][j].visited:
                possible_directions += 1
                next_index_list.append((i - 1, j))
            # up
            if j > 0 and not self._cells[i][j - 1].visited:
                possible_directions += 1
                next_index_list.append((i, j - 1))
            # right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                possible_directions += 1
                next_index_list.append((i + 1, j))
            # down
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                possible_directions += 1
                next_index_list.append((i, j + 1))

            # break out if there is no possible path
            if possible_directions == 0:
                self._draw_cells(i, j)
                return

            # direction to move to
            next_index = next_index_list[random.randrange(possible_directions)]

            # break adequate walls
            # left
            if next_index == (i - 1, j):
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            # up
            if next_index == (i, j - 1):
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False
            # right
            if next_index == (i + 1, j):
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # down
            if next_index == (i, j + 1):
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False

            # recursion call:
            self._break_walls_r(next_index[0], next_index[1])

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate(time_sleep_secs=0.09)
        self._cells[i][j].visited = True
        # if we have reached the goal cell (right-bottom most)
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        # check if we can move in a given direction:
        # there is a cell that is not visited
        # and no wall is blocking the access
        # left
        if i > 0 and not self._cells[i - 1][j].visited \
                and not self._cells[i][j].has_left_wall:
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], undo=True)
        # up
        if j > 0 and not self._cells[i][j - 1].visited \
                and not self._cells[i][j].has_top_wall:
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], undo=True)
        # right
        if i < self._num_cols - 1 and not self._cells[i + 1][j].visited \
                and not self._cells[i][j].has_right_wall:
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], undo=True)
        # down
        if j < self._num_rows - 1 and not self._cells[i][j + 1].visited \
                and not self._cells[i][j].has_bottom_wall:
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], undo=True)
        return False

    def _animate(self, time_sleep_secs=0.05):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(time_sleep_secs)
