from graphics import Window
from cell import Cell


def run():
    win = Window(800, 600)
    cell = Cell(win)
    cell.has_left_wall = False
    cell.draw(40,40,60,60)

    cell = Cell(win)
    cell.has_top_wall=False
    cell.has_bottom_wall=False
    cell.draw(70,70,100,100)
    win.wait_for_close()


if __name__ == '__main__':
    run()
