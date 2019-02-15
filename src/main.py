import curses
from DrawMap import DrawMap

def main():
    stdscr = curses.initscr()

    DrawMap().draw_map()

    stdscr.getch()
    curses.endwin()

if __name__ == "__main__":
    main()
    
