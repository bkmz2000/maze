from lab import Maze
from tkinter import Tk, Canvas

class GameScene:
    def __init__(self, maze):
        self.size = maze.size
        self.maze = maze.arr
        self.arr = [[0 for x in range(maze.size)] 
                       for y in range(maze.size)]

        self.vis = [] 

    def update(self, x, y):
        self.vis.append((x, y))
        xBuff = x
        
        while not self.maze[y][xBuff] == 0:
            self.arr[y][xBuff]   = 1
            
            if xBuff+1 < self.size: 
                xBuff += 1

            else:
                break

        xBuff = x
        
        while not self.maze[y][xBuff] == 0:
            self.arr[y][xBuff]   = 1

            if xBuff-1 >= 0:
                xBuff -= 1

            else:
                break

        yBuff = y

        while not self.maze[yBuff][x] == 0:
            self.arr[yBuff][x]   = 1
            
            if yBuff + 1 < self.size:
                yBuff += 1

            else:
                break

        yBuff = y

        while not self.maze[yBuff][x] == 0:
            self.arr[yBuff][x]   = 1

            if yBuff-1 >= 0:
                yBuff -= 1
            
            else:
                break


    def draw(self, canv, size):
        for x in range(self.size):
            for y in range(self.size):
                if self.arr[y][x] == 0:
                    color = 'gray'

                if self.arr[y][x] == 1:
                    color = 'lightblue'

                if (x, y) in self.vis:
                    color = 'white'

                if self.arr[y][x] == 1 and self.maze[y][x] == 2:
                    color = 'purple'

                canv.create_rectangle(x*size, y*size,
                                     (x+1)*size, (y+1)*size,
                                     fill = color)

        canv.update()
