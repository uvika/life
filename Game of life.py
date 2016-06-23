from collections import Counter

def __init__(g, alive):
   print(alive)

def game_life(cells, generations):
    alive = set((x, y)
                for y, row in enumerate(cells)
                for x, cell in enumerate(row)
                if cell)
    for g in range(generations):
        __init__(g, alive)
        neighbours = Counter((x + i, y + j)
                            for x, y in alive
                            for i in range(-1, 2)
                            for j in range(-1, 2))
        alive = set(xy for xy, cnt in neighbours.items()
                    if cnt == 3 or cnt == 4 and xy in alive)

game_life([[0, 1], [1, 1], [1, 2]], 5)
