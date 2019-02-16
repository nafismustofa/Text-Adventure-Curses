import curses
from player import Player

def main():
    stdscr = curses.initscr()
    Player().player()
    curses.endwin()

if __name__ == "__main__":
    main()
