from lab import *
from tkinter import Tk, Canvas
from time import sleep
from random import choice

class Game:
    def __init__(self, player, cellSize = 20):
        self.root = Tk()
        self.size = 20
        self.player = player
        self.canv = Canvas(self.root, width  = 20 * cellSize, 
                                      height = 20 * cellSize,
                                      bg = 'black')

        self.canv.pack()

        self.setMaze()

        self.root.bind('w', lambda a: self.movePlayer('w'))
        self.root.bind('s', lambda a: self.movePlayer('s'))
        self.root.bind('d', lambda a: self.movePlayer('d'))
        self.root.bind('a', lambda a: self.movePlayer('a'))
        self.root.bind('g', lambda a: self.goDown())


    def goDown(self):
        print(self.player.x, self.player.y, self.maze.out)
        if self.player.x == self.maze.out[0]:
            if self.player.y == self.maze.out[1]:
                self.setMaze()
                self.draw()

    def setMaze(self):
        self.maze = Maze(20)
        pcoord = choice(self.maze.vis)
        self.player.x = pcoord[0]
        self.player.y = pcoord[1]

    def movePlayer(self, d):
        if d == 's':
            self.player.moveUp(self.maze)

        if d == 'w':
            self.player.moveDown(self.maze)

        if d == 'd':
            self.player.moveRight(self.maze)

        if d == 'a':
            self.player.moveLeft(self.maze)

        self.draw()

    def draw(self):
        self.canv.delete('all')
        self.maze.draw(self.canv, 20)
        self.player.draw(self.canv, 20)
        sleep(0.3)
        self.root.mainloop()


class Player:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def draw(self, canv, cellSize):
        print('Drawing player')
        canv.create_rectangle(self.x * cellSize,
                              self.y * cellSize,
                              (self.x+1) * cellSize,
                              (self.y+1) * cellSize, fill = 'red')

        canv.update()

    def moveUp(self, maze):
        if maze.arr[self.y+1][self.x] == 0:
            return

        print('going up')

        self.y+=1


    def moveDown(self, maze):
        if maze.arr[self.y-1][self.x] == 0:
            return

        print('going down')

        self.y-=1


    def moveRight(self, maze):
        if maze.arr[self.y][self.x+1] == 0:
            return

        print('going right')

        self.x+=1


    def moveLeft(self, maze):
        if maze.arr[self.y][self.x-1] == 0:
            return

        print('going left')

        self.x-=1


player = Player()
game   = Game(player)
game.draw()




