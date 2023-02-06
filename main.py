from graphics import Window, Line, Point


def run():
    win = Window(800, 600)
    l = Line(Point(50,50), Point(300,300))
    win.draw_line(l,"black")
    win.wait_for_close()


if __name__ == '__main__':
    run()
