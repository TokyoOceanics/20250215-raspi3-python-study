#!/usr/bin/env python3

#20250215 chat gptによる

import curses
import random
import time

def init_grid(height, width):
    return [[random.choice([0, 1]) for _ in range(width)] for _ in range(height)]

def count_neighbors(grid, x, y, height, width):
    neighbors = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),         (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    count = 0
    for dx, dy in neighbors:
        nx, ny = x + dx, y + dy
        if 0 <= nx < height and 0 <= ny < width:
            count += grid[nx][ny]
    return count

def update_grid(grid, height, width):
    new_grid = [[0] * width for _ in range(height)]
    for x in range(height):
        for y in range(width):
            neighbors = count_neighbors(grid, x, y, height, width)
            if grid[x][y] == 1:
                if neighbors in [2, 3]:
                    new_grid[x][y] = 1
            else:
                if neighbors == 3:
                    new_grid[x][y] = 1
    return new_grid

def draw_grid(stdscr, grid, height, width):
    stdscr.clear()
    for x in range(height):
        for y in range(width):
            stdscr.addch(x, y, '#' if grid[x][y] else ' ')
    stdscr.refresh()

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)
    height, width = curses.LINES - 1, curses.COLS - 1
    grid = init_grid(height, width)
    
    while True:
        draw_grid(stdscr, grid, height, width)
        grid = update_grid(grid, height, width)
        time.sleep(0.1)
        key = stdscr.getch()
        if key == ord('q'):
            break

if __name__ == "__main__":
    curses.wrapper(main)

