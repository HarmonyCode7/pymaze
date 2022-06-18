from pymaze import Grid 
from binarytree import BinaryTree
import cv2

if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 3:
        rows = int(sys.argv[1])
        cols = int(sys.argv[2])
        grid = Grid(rows, cols)
        g = BinaryTree.on(grid)
        print(g)
        img = g.to_png()
        cv2.imwrite('simple-maze.png', img)