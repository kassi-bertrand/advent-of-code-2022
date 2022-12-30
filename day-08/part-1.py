#read file and return its lines
def readFile(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    return lines


def isVisbile_Left(x, y):
    """Is tree visible from left side?"""
    pass

def isVisible_Right(x, y):
    """Is tree visible from right side?"""
    pass

def isVisible_Top(x, y):
    """Is tree visible from top side?"""
    pass

def isVisible_Bottom(x, y):
    """Is tree visible from bottom side?"""
    pass

def isVisible(x, y):
    """Is tree is visible from any side in the grid?"""
    if isVisbile_Left(x,y) or isVisible_Right(x,y) or isVisible_Bottom(x,y) or isVisible_Top(x,y):
        return True
    else:
        return False

if __name__ == "__main__":
    lines = readFile('input-test.txt')

    grid = None
    visibleTrees = 0