/*
 *
 *
 *
 
# コンパイルオプションまとめ

## 基本のコンパイル
    gcc life_game.c -o life_game -lncurses

## 最適化オプション
    gcc life_game.c -o life_game -lncurses -O2
    (-O2: バランスの良い最適化, -O3: 高速化, -Os: サイズ削減, -Ofast: 速度重視)

## デバッグ用
    gcc life_game.c -o life_game -lncurses -g
    (gdb でデバッグ可能)

## 警告を強化
    gcc life_game.c -o life_game -lncurses -Wall -Wextra -Werror
    (-Wall: よくある警告, -Wextra: 追加警告, -Werror: 警告をエラー扱い)

## マルチスレッド対応
    gcc life_game.c -o life_game -lncurses -pthread
    (pthread を使用する場合)

## 静的リンク
    gcc life_game.c -o life_game -lncurses -static
    (動的ライブラリがない環境でも動作可能)

## 実行ファイルのサイズ削減
    gcc life_game.c -o life_game -lncurses -s
    (不要なシンボル情報を削除)

## Raspberry Pi 向け最適化
    gcc life_game.c -o life_game -lncurses -O2 -march=armv6 -mtune=arm1176jzf-s -mfpu=vfp -mfloat-abi=hard


sudo apt update
sudo apt install libncurses5-dev libncursesw5-dev



*/


#include <ncurses.h>
#include <stdlib.h>
#include <unistd.h>

#define WIDTH  80
#define HEIGHT 24

void init_grid(int grid[HEIGHT][WIDTH]) {
    for (int i = 0; i < HEIGHT; i++) {
        for (int j = 0; j < WIDTH; j++) {
            grid[i][j] = rand() % 2;  // 0 or 1
        }
    }
}

int count_neighbors(int grid[HEIGHT][WIDTH], int x, int y) {
    int neighbors = 0;
    int dx[] = {-1, -1, -1, 0, 0, 1, 1, 1};
    int dy[] = {-1, 0, 1, -1, 1, -1, 0, 1};

    for (int i = 0; i < 8; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];

        if (nx >= 0 && nx < HEIGHT && ny >= 0 && ny < WIDTH) {
            neighbors += grid[nx][ny];
        }
    }
    return neighbors;
}

void update_grid(int grid[HEIGHT][WIDTH]) {
    int new_grid[HEIGHT][WIDTH] = {0};

    for (int i = 0; i < HEIGHT; i++) {
        for (int j = 0; j < WIDTH; j++) {
            int neighbors = count_neighbors(grid, i, j);
            if (grid[i][j] == 1 && (neighbors == 2 || neighbors == 3)) {
                new_grid[i][j] = 1;
            } else if (grid[i][j] == 0 && neighbors == 3) {
                new_grid[i][j] = 1;
            }
        }
    }

    for (int i = 0; i < HEIGHT; i++) {
        for (int j = 0; j < WIDTH; j++) {
            grid[i][j] = new_grid[i][j];
        }
    }
}

void draw_grid(int grid[HEIGHT][WIDTH]) {
    clear();
    for (int i = 0; i < HEIGHT; i++) {
        for (int j = 0; j < WIDTH; j++) {
            mvaddch(i, j, grid[i][j] ? '#' : ' ');
        }
    }
    refresh();
}

int main() {
    int grid[HEIGHT][WIDTH];
    initscr();
    curs_set(0);
    nodelay(stdscr, TRUE);
    timeout(100);
    init_grid(grid);

    while (1) {
        draw_grid(grid);
        update_grid(grid);
        usleep(100000);  // 100ms delay
        if (getch() == 'q') break;
    }

    endwin();
    return 0;
}

