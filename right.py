import curses
import time
import signal
import sys

N_CNT = 0 
M_CNT = 0

MIN_NUM = 1
MAX_NUM = 80 

def handler(signal, frame):
        print('Done');
        sys.exit(0)
signal.signal(signal.SIGINT, handler)
 
stdscr = curses.initscr()

def main(stdscr):

    n = N_CNT
    m = M_CNT
    first = 0

    while(True):

        if first == 0:
            n = 0        
            first = 1        
        elif first == 1:
            n = n + 1
            if n == 23:
                break

        for i in range(MIN_NUM, MAX_NUM):

            m =  m + 1

            stdscr.clear()
            stdscr.addstr(n, m, 'X')
            stdscr.refresh()

            time.sleep(0.1)

        #stdscr.getkey()
 
        for i in range(MIN_NUM, MAX_NUM):

            m =  m - 1

            stdscr.clear()
            stdscr.addstr(n, m, 'X')
            stdscr.refresh()

            time.sleep(0.1)

    pass

    n = n + 1

if __name__ == '__main__':
    curses.wrapper(main)
