from graphics import Window
from cell import Cell


def run():
    win = Window(800, 600)
    first_cell = Cell(win)
    first_cell.has_left_wall = False
    first_cell.has_top_wall = False
    first_cell.draw(40, 40, 60, 60)

    second_cell = Cell(win)
    second_cell.has_right_wall = False
    second_cell.draw(20, 40, 40, 60)

    third_cell = Cell(win)
    third_cell.has_top_wall = False
    third_cell.draw(20,60,40,80)

    fourth_cell = Cell(win)
    fourth_cell.has_bottom_wall = False
    fourth_cell.draw(40,20,60,40)

    # fifth_cell = Cell(win)
    # fifth_cell.has_left_wall = False
    # fifth_cell.draw(60,40,80,60)

    first_cell.draw_move(second_cell)
    second_cell.draw_move(third_cell)
    first_cell.draw_move(fourth_cell)
    # first_cell.draw_move(fifth_cell)

    win.wait_for_close()


if __name__ == '__main__':
    run()
