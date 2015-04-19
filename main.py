from lab import Maze
from path import Path
from tkinter import Tk, Canvas
from time import sleep, time
from random import choice
from player import Player
from fog import Fog


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
        self.draw()

        self.root.bind('w', lambda a: self.movePlayer('w'))
        self.root.bind('s', lambda a: self.movePlayer('s'))
        self.root.bind('d', lambda a: self.movePlayer('d'))
        self.root.bind('a', lambda a: self.movePlayer('a'))
        self.root.bind('<Button-1>', self.movePlayerTo)
        self.root.bind('g', lambda a: self.goDown())
        self.root.mainloop()

    def movePlayerTo(self, event):
        x = int(event.x/20)
        y = int(event.y/20)

        path = str(Path(self.maze, (self.player.x, self.player.y),
                                   (x, y)))

        for i in path:
            self.movePlayer(i)
            sleep(0.1)


    def goDown(self):
        if self.player.x == self.maze.out[0]:
            if self.player.y == self.maze.out[1]:
                self.setMaze()
                self.draw()

    def setMaze(self):
        self.maze = Maze(20)
        self.fog  = Fog(self.maze) 
        pcoord = choice(self.maze.vis)
        self.player.x = pcoord[0]
        self.player.y = pcoord[1]
        self.fog.update(self.player.x,
                        self.player.y)

    def movePlayer(self, d):
        if d == 's':
            self.player.moveUp(self.maze)

        if d == 'w':
            self.player.moveDown(self.maze)

        if d == 'd':
            self.player.moveRight(self.maze)

        if d == 'a':
            self.player.moveLeft(self.maze)

        self.fog.update(self.player.x,
                        self.player.y)

        self.draw()

    def draw(self):
        n = time()
        self.canv.delete('all')
        self.maze.draw(self.canv, 20) # 0.011569738388061523

        self.fog.draw(self.canv, 20) # 0.01540231704711914

        self.player.draw(self.canv, 20) #0.0006022453308105469
        print(time()-n)

player = Player()
game   = Game(player)
game.draw()




