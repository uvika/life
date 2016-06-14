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
            if (neighbours == 2 or ( neighbours == 3 and cell)): 
                alive.add(cell)
            else:
                alive.remove(cell)

    def field(self):
            alive = set()
            init1 = Cell(0, 0)
            init2 = Cell(1, 1)
            init3 = Cell(1, 2)
            alive.update((0, 0), (0, 1), (0, 2), (1, 2))
