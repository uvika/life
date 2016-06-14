class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getNeighbours(self, cell):
        self.x, self.y = cell
        neighbors = [(x + i, y + j)
                     for i in xrange(-1, 2)
                     for j in xrange(-1, 2)
                     if not i == j == 0]
        return neighbors
    
    def aliveCell(cell): 
            if (neighbours == 2 or ( neighbours == 3 and cell)): 
                alive.add(cell)
            else:
                alive.remove(cell)

    def field(self):
            alive = set()
            init1 = сell(0, 0)
            init2 = сell(1, 1)
            init3 = сell(1, 2)
            alive.update(init1, init2, init3)
