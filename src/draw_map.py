import curses

class DrawMap:
    def draw_map(self):
        stdscr = curses.initscr()

        stdscr.addstr(0 , 0 , "####################")
        for i in range(1 , 9):
            stdscr.addstr(i , 0 , "#                  #")
        stdscr.addstr(9 , 0 , "####################")
