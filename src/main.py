import curses
from player import Player

def main():
    stdscr = curses.initscr()

    Player().player()

    stdscr.getch()
    curses.endwin()

if __name__ == "__main__":
    main()
