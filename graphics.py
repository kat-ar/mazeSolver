from tkinter import Tk, BOTH, Canvas

BACKGROUND_COLOR = "white"
PATH_COLOR = "red"
WALL_COLOR = "black"
BACKTRACK_COLOR = "gray"

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze solver")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def close(self):
        self.__running = False


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, first_point, second_point):
        self.first_point = first_point
        self.second_point = second_point

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.first_point.x, self.first_point.y,
            self.second_point.x, self.second_point.y,
            fill=fill_color, width=2
        )
        canvas.pack(fill=BOTH, expand=1)
