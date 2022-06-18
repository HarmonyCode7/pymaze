class Cell:
    def __init__(self, row, col):
        self._row = row
        self._column = col

        self._north = None
        self._south = None
        self._east = None
        self._west = None

        self._links = {}

    def get_row(self):
        return self._row

    def get_column(self):
        return self._column
    
    def get_east(self):
        return self._east

    def set_east(self, cell):
        self._east = cell
    
    def get_north(self):
        return self._north

    def set_north(self, cell):
        self._north = cell

    def get_south(self):
        return self._south

    def set_south(self, cell):
        self._south = cell

    def get_west(self):
        return self._west

    def set_west(self, cell):
        self._west = cell

    def link(self,cell, bidi=True):
        self._links.update({cell:bidi})
        if bidi:
            cell.link(self, False)
        return self
    
    def unlink(self, cell, bidi=True):
        del self._links[cell]
        if bidi:
            cell.unlink(self, False)
        return self
    
    def links(self):
        return self._links.keys()

    def linked(self,cell):
        if cell in self._links:
            return True 
        return False
    
    def neinghbors(self):
        list = []
        if self._north is not None:
            list.append(self._north)
        if self._south is not None:
            list.append(self._south)
        if self._east is not None:
            list.append(self._east)
        if self._west is not None:
            list.append(self._west)

        return list


