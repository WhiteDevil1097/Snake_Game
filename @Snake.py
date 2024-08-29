import curses
from random import randint
import requests
import os
import sys
import time
def animated(text):
     for x in text:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.01)

logo = '''
                                                  
 @@@@@@   @@@  @@@   @@@@@@   @@@  @@@  @@@@@@@@  
@@@@@@@   @@@@ @@@  @@@@@@@@  @@@  @@@  @@@@@@@@  
!@@       @@!@!@@@  @@!  @@@  @@!  !@@  @@!       
!@!       !@!!@!@!  !@!  @!@  !@!  @!!  !@!       
!!@@!!    @!@ !!@!  @!@!@!@!  @!@@!@!   @!!!:!    
 !!@!!!   !@!  !!!  !!!@!!!!  !!@!!!    !!!!!:    
     !:!  !!:  !!!  !!:  !!!  !!: :!!   !!:       
    !:!   :!:  !:!  :!:  !:!  :!:  !:!  :!:       
:::: ::    ::   ::  ::   :::   ::  :::   :: ::::  
:: : :    ::    :    :   : :   :   :::  : :: ::   
'''
animated(logo)
print('       »»»Devoloper By White_Devil«««')
print('      _________________________________')
# Initialize screen
stdscr = curses.initscr()
curses.curs_set(0)
sh, sw = stdscr.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

# Initialize snake and food
key = curses.KEY_RIGHT
snake = [
    [sh // 2, sw // 4],
    [sh // 2, sw // 4 - 1],
    [sh // 2, sw // 4 - 2]
]
food = [sh // 2, sw // 2]
w.addch(int(food[0]), int(food[1]), curses.ACS_PI)

score = 0

while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    # Calculate new head of the snake
    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

    # Check if snake has collided with food
    if snake[0] == food:
        score += 1
        food = None
        while food is None:
            nf = [
                randint(1, sh - 1),
                randint(1, sw - 1)
            ]
            food = nf if nf not in snake else None
        w.addch(int(food[0]), int(food[1]), curses.ACS_PI)
    else:
        tail = snake.pop()
        w.addch(int(tail[0]), int(tail[1]), ' ')

    if (snake[0][0] in [0, sh] or
        snake[0][1] in [0, sw] or
        snake[0] in snake[10:]):
        curses.endwin()
        quit()

    w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)


