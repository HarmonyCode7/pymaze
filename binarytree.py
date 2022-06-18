from random import randint
from random import choice
import os 
import time 

class BinaryTree:
    @staticmethod
    def on(grid):
        cell_count = 0
        for cell in grid.each_cell():
            neighbors = []
            north = cell.get_north()
            east = cell.get_east()

            if north is not None:
                neighbors.append(north)

            if east is not None:
                neighbors.append(east)

            if len(neighbors) >= 1:
                neighbor = choice(neighbors)
                if neighbor is not None:
                    cell.link(neighbor)
            cell_count += 1
            print(grid)
            time.sleep(1)
            os.system("clear")
        return grid
