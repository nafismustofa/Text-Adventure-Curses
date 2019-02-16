import curses
from draw_map import DrawMap

class Player:
    __position_x = 1
    __position_y = 1
    __player = "o"
    __is_running = True

    __stdscr = curses.initscr()

    def player(self):
        self.__stdscr.keypad(True)
        curses.curs_set(0)
        curses.noecho()

        DrawMap().draw_map()
        self.__stdscr.addstr(self.__position_y , self.__position_x , self.__player)

        while self.__is_running:
            c = self.__stdscr.getch()

            if c == ord("w") or c == ord("W") or c == curses.KEY_UP:
                self.__position_y -= 1
                self.__stdscr.refresh()
                if self.__position_y == 0:
                    self.__position_y += 1
                DrawMap().draw_map()
                self.__stdscr.addstr(self.__position_y , self.__position_x , self.__player)

            if c == ord("s") or c == ord("S") or c == curses.KEY_DOWN:
                self.__position_y += 1
                self.__stdscr.refresh()
                if self.__position_y == 9:
                    self.__position_y -= 1
                DrawMap().draw_map()
                self.__stdscr.addstr(self.__position_y , self.__position_x , self.__player)

            if c == ord("a") or c == ord("A") or c == curses.KEY_LEFT:
                self.__position_x -= 1
                self.__stdscr.refresh()
                if self.__position_x == 0:
                    self.__position_x += 1
                DrawMap().draw_map()
                self.__stdscr.addstr(self.__position_y , self.__position_x , self.__player)

            if c == ord("d") or c == ord("D") or c == curses.KEY_RIGHT:
                self.__position_x += 1
                self.__stdscr.refresh()
                if self.__position_x == 19:
                    self.__position_x -= 1
                DrawMap().draw_map()
                self.__stdscr.addstr(self.__position_y , self.__position_x , self.__player)

            if c == ord("q"):
                break
