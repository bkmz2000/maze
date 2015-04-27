from lab import Maze
from tkinter import Tk, Canvas, PhotoImage
from random import randint
class GameScene:
    def __init__(self, maze):
        self.size = maze.size
        self.maze = maze.arr
        self.player = None
        self.arr = [[0 for x in range(maze.size)] 
                       for y in range(maze.size)]

        self.wall = PhotoImage(file = 'res/wall.png')
        self.floor = PhotoImage(file = 'res/floor.png')
        self.floorN = PhotoImage(file = 'res/floor1.png')
        self.none = PhotoImage(file = 'res/none.png')
        self.portal = PhotoImage(file = 'res/portal.png')
        self.playerImg = PhotoImage(file = 'res/player'+str(randint(1,4))+'.png')

        self.vis = [] 

    def update(self, player):
        self.player = player
        self.vis.append((player.x, player.y))
        xBuff = player.x
        
        while not self.maze[player.y][xBuff] == 0:
            self.arr[player.y][xBuff]   = 1
            
            if xBuff+1 < self.size: 
                xBuff += 1

            else:
                break

        xBuff = player.x
        
        while not self.maze[player.y][xBuff] == 0:
            self.arr[player.y][xBuff]   = 1

            if xBuff-1 >= 0:
                xBuff -= 1

            else:
                break

        yBuff = player.y

        while not self.maze[yBuff][player.x] == 0:
            self.arr[yBuff][player.x]   = 1
            
            if yBuff + 1 < self.size:
                yBuff += 1

            else:
                break

        yBuff = player.y

        while not self.maze[yBuff][player.x] == 0:
            self.arr[yBuff][player.x]   = 1

            if yBuff-1 >= 0:
                yBuff -= 1
            
            else:
                break


    def draw(self, canv, size):
        for x in range(0, self.size):
            for y in range(0, self.size):
                if self.arr[y][x] == 0:
                    image = self.none
                    
                if self.arr[y][x] == 1:
                    image = self.floorN

                if (x, y) in self.vis:
                    image = self.floor

                if self.arr[y][x] == 1 and self.maze[y][x] == 2:
                    image = self.portal

                canv.create_image(x*size, y*size, image= image)

        canv.create_image(self.player.x * size, 
                          self.player.y * size, image = self.playerImg)

        canv.update()
