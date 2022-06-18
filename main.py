from pymaze import Grid 
from binarytree import BinaryTree


if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 3:
        rows = int(sys.argv[1])
        cols = int(sys.argv[2])
        grid = Grid(rows, cols)
        g = BinaryTree.on(grid)
        print(g)