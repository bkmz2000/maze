from tkinter import Tk, Canvas, PhotoImage
from random import randint

class Creature:
    def __init__(self, x=0,y=0):
        self.x = x
        self.y = y
        self.number = randint(1,4)

    def draw(self, canv, size):
        print('res/player'+str(self.number)+'.png')

        x=self.x
        y=self.y
        
        root = Tk()
        img = PhotoImage(root, file = 'res/player1.png')
        img.pack()
        root.mainloop()
        canv.create_image(x*size, y*size, image = img)

        canv.update()

    def moveUp(self, maze):
        if maze.arr[self.y+1][self.x] == 0:
            return


        self.y+=1


    def moveDown(self, maze):
        if maze.arr[self.y-1][self.x] == 0:
            return

        self.y-=1


    def moveRight(self, maze):
        if maze.arr[self.y][self.x+1] == 0:
            return

        self.x+=1


    def moveLeft(self, maze):
        if maze.arr[self.y][self.x-1] == 0:
            return

        self.x-=1
