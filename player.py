class Player:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def draw(self, canv, cellSize):
        canv.create_rectangle(self.x * cellSize,
                              self.y * cellSize,
                              (self.x+1) * cellSize,
                              (self.y+1) * cellSize, fill = 'red')

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
