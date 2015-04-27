from random import choice 
from tkinter import Tk, Canvas
from time import time

class Maze:
    def __init__(self, size):
        self.size = size
        self.vis = []
        self.arr = [[0 for i in range(size)] for i in range(size)]
        self.out = ()
        self.gen()
 
    def suits(self, x, y):
        arr = self.arr
 
        if (x, y) in self.vis:
            return False
 
        if y+1 < self.size:
            if arr[y+1][x] == 1:
                return False
 
        if y-1 >= 0:
            if arr[y-1][x] == 1:
                return False
     
        if x+1 < self.size:
            if arr[y][x+1] == 1:
                return False
 
        if x-1 >= 0:
            if arr[y][x-1] == 1:
                return False
 
        return True
 
 
    def genFrom(self, x, y):
        self.vis.append((x, y))
        self.arr[y][x] = 2
        av           = []
 
        if x+1 < self.size:
            if self.suits(x+1, y):
                av.append((x+1, y))
 
        if x-1 > 0:
            if self.suits(x-1, y):
                av.append((x-1, y))
 
        if y + 1 < self.size:
            if self.suits(x, y+1):
                av.append((x, y+1))
 
     
        if y-1 > 0:
            if self.suits(x, y-1):
                av.append((x, y-1))
 
        self.arr[y][x] = 1
 
        if len(av) == 0:
            return
 
        to = choice(av)
     
        X = to[0]
        Y = to[1]
 
        self.arr[y][x] = 1
 
        self.genFrom(X, Y)
         
    def gen(self):
        self.genFrom(0, 0)
 
        for i in range(self.size**2):
            cell = choice(self.vis)
            x = cell[0]
            y = cell[1]
            self.genFrom(x, y)
 
        out = choice(self.vis)
        x = out[0]
        y = out[1]
        self.arr[y][x] = 2
        self.out = out
