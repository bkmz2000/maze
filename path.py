from lab import Maze
from random import choice
from tkinter import Tk, Canvas

class Path:
    def __init__(self, maze, f, t):
        self.maze = maze
        self.f   = f
        self.t   = t
        self.path = ''
        self.vis = []
        self.findFrom(f[0], f[1])

    def __str__(self):
        return self.path

    def findFrom(self, x, y, path = ''):
        self.vis.append((x, y))
        

        if x == self.t[0] and y == self.t[1]:
            self.path = path
            return

        if x+1 < self.maze.size:
            if not self.maze.arr[y][x+1] == 0:
                if not (x+1, y) in self.vis:
                    self.findFrom(x+1, y, path+'d')

        if x-1 >= 0:
            if not self.maze.arr[y][x-1] == 0:
                if not (x-1, y) in self.vis:
                    self.findFrom(x-1, y, path+'a')

        if y+1 < self.maze.size:
            if not self.maze.arr[y+1][x] == 0:
                if not (x, y+1) in self.vis:
                    self.findFrom(x, y+1, path+'s')

        if y-1 >= 0:
            if not self.maze.arr[y-1][x] == 0:
                if not (x, y-1) in self.vis:
                    self.findFrom(x, y-1, path+'w')
