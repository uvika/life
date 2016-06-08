class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        initialpopulation = set([(0,0), (1,1),(1,2)])

    def getNeighbours(self, cell):
        self.x, self.y = cell
        neighbors = [(x + i, y + j)
                     for i in xrange(-1, 2)
                     for j in xrange(-1, 2)
                     if not i == j == 0]
        return neighbors
    
    def aliveCell(cell): 
            alive = set()
            if (neighbours == 2 or ( neighbours == 3 and cell): 
                alive.add(cell)
            else
                alive.

    def deadCell (cell):
            if (neighbours > 3 or ( neighbours < 1 and cell ):
                alive.remove(cell)


