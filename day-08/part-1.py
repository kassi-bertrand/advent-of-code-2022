#read file and return its lines
def readFile(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    return lines


def isVisibile_Left(grid, row, column):
    """Is tree visible from left side?"""
    treeHeight = grid[row][column]

    for i in range(column - 1, -1, -1):
        if grid[row][i] >= treeHeight:
            return False

    return True

def isVisible_Right(grid, row, column):
    """Is tree visible from right side?"""
    treeHeight = grid[row][column]

    for i in range(column + 1, len(grid[0])):
        if grid[row][i] >= treeHeight:
            return False

    return True

def isVisible_Top(grid, row, column):
    """Is tree visible from top side?"""
    treeHeight = grid[row][column]

    for i in range(row - 1, -1, -1):
        if grid[i][column] >= treeHeight:
            return False

    return True

def isVisible_Bottom(grid, row, column):
    """Is tree visible from bottom side?"""
    treeHeight = grid[row][column]

    for i in range(row + 1, len(grid)):
        if grid[i][column] >= treeHeight:
            return False

    return True

def isVisible(grid, row, column):
    """Is tree is visible from any side in the grid?"""
    if isVisibile_Left(grid, row, column) or isVisible_Right(grid, row, column) or isVisible_Bottom(grid, row, column) or isVisible_Top(grid, row, column):
        return True
    else:
        return False

if __name__ == "__main__":
    lines = readFile('input.txt')
    
    #1- Form the grid
    grid = []
    for line in lines:
        arr = list(line.strip())
        arr = [int(i) for i in arr] #Turn "chars" in "int"
        grid.append(arr)

    #2- Count the number of trees visibles from any side
    visibleTrees = 0

    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if isVisible(grid, row, column):
                visibleTrees += 1
    
    #3- Print result
    print(f'Trees visibles from outside grid: {visibleTrees}')