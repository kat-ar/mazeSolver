from graphics import Point, Line


class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.visited = False

    def draw_cell(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        line = Line(Point(x1, y1), Point(x2, y1))
        if self.has_top_wall:
            self._win.draw_line(line)
        else:
            self._win.draw_line(line, fill_color="white")
        line = Line(Point(x2, y1), Point(x2, y2))
        if self.has_right_wall:
            self._win.draw_line(line)
        else:
            self._win.draw_line(line, fill_color="white")
        line = Line(Point(x2, y2), Point(x1, y2))
        if self.has_bottom_wall:
            self._win.draw_line(line)
        else:
            self._win.draw_line(line, fill_color="white")
        line = Line(Point(x1, y2), Point(x1, y1))
        if self.has_left_wall:
            self._win.draw_line(line)
        else:
            self._win.draw_line(line, fill_color="white")

    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
        # coordinates of the centers of cells we want to connect
        x_middle = (self._x1 + self._x2)/2
        y_middle = (self._y1 + self._y2)/2

        to_x_middle = (to_cell._x1 + to_cell._x2)/2
        to_y_middle = (to_cell._y1 + to_cell._y2)/2
        # fill color - draw or backtrack
        fill_color = "red"
        if undo:
            fill_color = "gray"
        # moving horizontal - y constans
        # moving left:
        if self._x1 > to_cell._x1:
            line = Line(Point(x_middle, y_middle), Point(to_cell._x2, y_middle))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_cell._x2, y_middle), Point(to_x_middle, y_middle))
            self._win.draw_line(line, fill_color)
            # line = Line(Point(x_middle, y_middle), Point(to_x_middle, y_middle))
            # self._win.draw_line(line, fill_color)
        # moving right
        elif self._x1 < to_cell._x1:
            line = Line(Point(x_middle, y_middle), Point(to_cell._x1, y_middle))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_cell._x1, y_middle), Point(to_x_middle, y_middle))
            self._win.draw_line(line, fill_color)
        # moving vertical - x constans
        # moving up
        elif self._y1 > to_cell._y1:
            line = Line(Point(x_middle, y_middle), Point(x_middle, self._y1))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_x_middle, to_cell._y2), Point(to_x_middle, to_y_middle))
            self._win.draw_line(line, fill_color)
        # moving down
        elif self._y1 < to_cell._y1:
            line = Line(Point(x_middle, y_middle), Point(x_middle, self._y2))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_x_middle, to_y_middle), Point(to_x_middle, to_cell._y1))
            self._win.draw_line(line, fill_color)


