#read file and return its lines
def readFile(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    return lines

def viewDist_Left(grid, row, column):
    """Number of trees visible to the LEFT of one tree"""
    treeHeight = grid[row][column]
    dist = 0

    for i in range(column - 1, -1, -1):
        dist += 1
        if grid[row][i] >= treeHeight:
            return dist
    
    return dist


def viewDist_Right(grid, row, column):
    """Number of trees visible to the RIGHT of one tree"""
    treeHeight = grid[row][column]
    dist = 0

    for i in range(column + 1, len(grid[0])):
        dist += 1
        if grid[row][i] >= treeHeight:
            return dist
    
    return dist

def viewDist_Top(grid, row, column):
    """Number of trees visible to the RIGHT of one tree"""
    treeHeight = grid[row][column]
    dist = 0

    for i in range(row - 1, -1, -1):
        dist += 1
        if grid[i][column] >= treeHeight:
            return dist
    
    return dist

def viewDist_Bottom(grid, row, column):
    """Number of trees visible to the BOTTOM of one tree"""
    treeHeight = grid[row][column]
    dist = 0

    for i in range(row + 1, len(grid)):
        dist += 1
        if grid[i][column] >= treeHeight:
            return dist
    
    return dist

def scenicScore(grid, row, column):
    return (
            viewDist_Left(grid, row, column) *
            viewDist_Right(grid, row, column) *
            viewDist_Top(grid, row, column) *
            viewDist_Bottom(grid, row, column)
        )

if __name__ == "__main__":
    lines = readFile('input.txt')

    #1- Form the grid
    grid = []
    for line in lines:
        arr = list(line.strip())
        arr = [int(i) for i in arr] #Turn "chars" in "int"
        grid.append(arr)

    #2- Determine the largest scenic score
    highestScore = 0

    for row in range(len(grid)):
        for column in range(len(grid[0])):
            
            score = scenicScore(grid, row, column)
            if score > highestScore:
                highestScore = score
    
    #3- Print result
    print(f'Largest scenic score: {highestScore}')