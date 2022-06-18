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

            print('index cell at: ({}, {})'.format(cell.get_row(), cell.get_column()))
            if north is not None:
                neighbors.append(north)

            print('east is : ', east)
            if east in cell.links():
                print('East is a neighbor')
            
            if east is not None:
                neighbors.append(east)
                print(f'east: ({east.get_rows()},{east.get_columns()})')
            if len(neighbors) >= 1:
                neighbor = choice(neighbors)
                if neighbor is not None:
                    cell.link(neighbor)
            cell_count += 1
            print(grid)
            print(f"Cell Count: {cell_count}")
            time.sleep(1)
            os.system("clear")
        return grid
