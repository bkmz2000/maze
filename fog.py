from lab import Maze
from tkinter import Tk, Canvas

class Fog:
    def __init__(self, maze):
        self.size = maze.size
        self.maze = maze.arr
        self.arr = [[1 for x in range(maze.size)] 
                       for y in range(maze.size)]

    def update(self, x, y):
        '''xp = x+1 < self.size
        xm = x-1 >= 0

        yp = y+1 < self.size
        ym = y-1 >= 0

        if yp:
            self.arr[y+1][x] = 0
            
        if xp:
            self.arr[y][x+1] = 0
            
        if xp and yp:
            self.arr[y+1][x+1] = 0
            
        if ym and xp:
            self.arr[y-1][x+1] = 0
            
        if yp and xm:
            self.arr[y+1][x-1] = 0
            
        if xm:
            self.arr[y][x-1] = 0
            
        if xm and ym:
            self.arr[y-1][x-1] = 0
            
        if ym:
            self.arr[y-1][x] = 0'''


        xBuff = x
        
        while not self.maze[y][xBuff] == 0:
            self.arr[y][xBuff]   = 0
            
            if xBuff+1 < self.size: 
                xBuff += 1

            else:
                break

        xBuff = x
        
        while not self.maze[y][xBuff] == 0:
            self.arr[y][xBuff]   = 0

            if xBuff-1 >= 0:
                xBuff -= 1

            else:
                break

        yBuff = y

        while not self.maze[yBuff][x] == 0:
            self.arr[yBuff][x]   = 0
            
            if yBuff + 1 < self.size:
                yBuff += 1

            else:
                break

        yBuff = y

        while not self.maze[yBuff][x] == 0:
            self.arr[yBuff][x]   = 0

            if yBuff-1 >= 0:
                yBuff -= 1
            
            else:
                break


    def draw(self, canv, size):
        for x in range(self.size):
            for y in range(self.size):
                if self.arr[y][x] == 1:
                    canv.create_rectangle(x*size, y*size,
                                         (x+1)*size, (y+1)*size,
                                         fill = 'gray')

        canv.update()
