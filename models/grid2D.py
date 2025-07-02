class Grid2D():
    """Create a 2D grid, that functions as a map, that can
    handle the geographic attributes.
    """
    def __init__(self, width, height):
        self.width = width
        self.height= height
        self.cells = [[Cell((x,y) for y in range(height))] for x in range(width)]


    
    def get_cell(self, pos):
        x, y = pos
        if 0<=x<self.width and 0<=y<self.height:
            return self.cells[x][y]
        return None

    def get_neighbours(self, pos):
        x, y = pos
        neighbour_offsents = [(-1, 0), (1,0), (0, -1), (0,1)]
        neighbours = []
        
        for dx, dy in neighbour_offsets:
            neighbour = self.get_cell((x+dx, y+dy))
            if neighbour:
                neighbours.append(neighbour.pos)        
        
        return neighbours
        
    def distance_to(self, cell):
        pass


