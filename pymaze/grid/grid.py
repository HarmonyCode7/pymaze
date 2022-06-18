from ..cell.cell import Cell 
from random import randint 
from random import choice
import numpy
import cv2

def make_image(width, height, color):
    image_height = width
    image_width = height
    number_of_color_channels = 3
    color = color
    pixel_array = numpy.full((image_height, image_width, number_of_color_channels), color, dtype=numpy.uint8)
    return pixel_array

class Grid:
    def __init__(self, rows, columns):
        self._rows = rows 
        self._columns = columns 

        self._grid = self.prepare_grid()
        self.configure_cells()


    def get_rows(self):
        return self._rows 
    
    def get_columns(self):
        return self._columns 

    def prepare_grid(self):
        rows = self.get_rows()
        cols = self.get_columns()
        return [[Cell(row,col) for col in range(0,cols) ] for row in range(0,rows) ]
    
    def configure_cells(self):
        for cell in self.each_cell():
            row = cell.get_row()
            col = cell.get_column()

            north = self.get_cell(row - 1, col)
            south = self.get_cell(row + 1, col)
            west  = self.get_cell(row, col - 1)
            east  = self.get_cell(row, col + 1)

            cell.set_north(north)
            cell.set_south(south)
            cell.set_west(west)
            cell.set_east(east)

    def get_cell(self,row, column):
        if row not in range(0, self.get_rows()):
            return 
        if column not in range(0, len(self._grid[row])):
            return
        return self._grid[row][column]

    def random_cell(self):
        return choice(self._grid)
    
    def size(self):
        return (self.get_rows() * self.get_columns())
    
    def each_row(self):
        for row in self._grid:
            yield row 
    
    def each_cell(self):
        for row in self.each_row():
            for cell in row:
                if cell is not None:
                    yield cell 
                
    def __str__(self) -> str:
        columns = self.get_columns()
        output = "+" + "---+" * columns + "\n"
        for row in self.each_row():
            top = "|" 
            bottom = "+"
            for cell in row:
                if cell is None:
                    cell = Cell.new(-1, -1)
                body = "   " # <-- that's THREE (3) spaces! 
                east_boundary = " " if cell.linked(cell.get_east()) else  "|"
                top += body + east_boundary

                # three spaces below, too >>-------------->> >...<
                south_boundary = "   " if cell.linked(cell.get_south()) else "---"
                corner = "+"
                bottom += south_boundary + corner
            output += top + "\n"
            output += bottom + "\n" 
        return output

    def to_png(self, cell_size=10):
        img_width = cell_size * self.get_columns()
        img_height = cell_size * self.get_rows();

        background = (0,0,0)
        wall = (0,255,0)

        img = make_image(img_width + 1, img_height + 1, background)
        #img = Image.new('RGB', (img_width + 1, img_height + 1), color=background)

        for cell in self.each_cell():
            x1 = cell.get_column() * cell_size
            y1 = cell.get_row() * cell_size

            x2 = (cell.get_column() + 1) * cell_size
            y2 = (cell.get_row() + 1) * cell_size

            if cell.get_north() is None:
                cv2.line(img,(x1, y1), (x2, y1), wall, 1)
            if cell.get_west() is None:
                cv2.line(img,(x1, y1), (x1, y2), wall, 1)

            if not cell.linked(cell.get_east()):
                cv2.line(img,(x2, y1), (x2, y2), wall, 1)
            if not cell.linked(cell.get_south()):
                cv2.line(img,(x1, y2), (x2, y2), wall, 1)
        return img