import curses

class ControlWindow(object):
    def __init__(self, pos, size_y, size_x):
        self.label = "Control"
        
        self.size_y = size_y // 2
        self.size_x = size_x // 2
        self.window = curses.newwin(self.size_y, self.size_x, pos[0], pos[1] - self.size_x // 2)
        self.window.box(0, 0)
        self.window.keypad(1)
        self.window.addstr(0, 1, self.label)
        self.position = 0

        self.buttons = (("Open table", curses.flash), ("Create table", curses.flash), ("Exit", "exit"))

    def navigation(self, n):
        self.position += n
        if self.position < 0:
            self.position = 0

        elif self.position >= len(self.buttons):
            self.position = len(self.buttons) - 1

    def display(self):
        while True:
            pos = 2
            for index, item in enumerate(self.buttons):
                if index == self.position:
                    mode = curses.A_REVERSE
                else:
                    mode = curses.A_NORMAL

                self.window.addstr(8, pos, item[0], mode)
                pos += 10

            key = self.window.getch()

            if key in [curses.KEY_ENTER, ord("\n")]:
                if self.position == len(self.buttons) - 1:
                    return 0
                else:
                    self.options[self.position][1]()

            elif key == curses.KEY_UP:
                self.navigation(-1)
            elif key == curses.KEY_DOWN:
                self.navigation(1)

        self.window.clear()
        curses.doupdate()
