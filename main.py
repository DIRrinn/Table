import curses
import open_win

class Main(object):
    def __init__(self, stdscreen):
        self.screen = stdscreen
        self.screen.box(0, 0)
        self.screen.addstr(0, 1, "Cursive", curses.A_DIM)
        self.screen.refresh()

        self.size_y = curses.COLS
        self.size_x = curses.LINES

        curses.start_color()
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED)
        curses.curs_set(0)

        self.menu = MainList(self.screen)
        ow = open_win.ControlWindow((0, 0), 1, 2)

class MainList(object):
    def __init__(self, screen):
        self.screen = screen
        self.size_x = curses.COLS
        self.size_y = curses.LINES

        self.window = curses.newwin(self.size_y, self.size_x, self.size_y, self.size_x)
        self.window.keypad(1)
        self.window.bkgd(' ', curses.color_pair(1))

        self.window.refresh()
        curses.doupdate()
        self.window.getch()

if __name__ == "__main__":
    curses.wrapper(Main)
