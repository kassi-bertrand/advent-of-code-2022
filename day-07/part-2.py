from abc import abstractmethod

#read file and return its lines
def readFile(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    return lines

#Generic tree node
#Inspired myself from: https://stackoverflow.com/questions/2358045/how-can-i-implement-a-tree-in-python
class Node:
    def __init__(self, name, parent, size=0):
        self.name = name
        self.size = size
        self.parent = parent
        self.type = None
        self.children = []

    @abstractmethod
    def addNode(self, node):
        pass

class Folder(Node):
    def __init__(self, name, parent, size=0):
        super().__init__(name, parent, size)
        self.type = 'folder'
        self.children = []

    def addNode(self, node):
        assert isinstance(node, Node)
        self.children.append(node)
    
    def nodeSize(self):
        size = 0    
        for child in self.children:
            size += child.nodeSize()
        return size

    def height(self):
        temp = []
        for child in self.children:
            temp.append(child.height())
        
        #The folder is empty
        if len(temp) == 0:
            return 0 + 1

        return max(temp) + 1
    
    def folderExists(self, folderName: str):
        for child in self.children:
            if child.name == folderName:
                return child
        
        return None

class File(Node):
    def __init__(self, name, parent, size=0):
        super().__init__(name, parent, size)
        self.type = 'file'
    
    def addNode(self, node):
        return

    def nodeSize(self):
        return self.size

    def height(self):
        return 0 + 1

class FileSystem:
    def __init__(self):
        self.pwd = None
        self.root = None
    
    def findDirs(self, root: Node, freeSpace: int):
        """
        Uses level order traversal to determine
        the directories big enough, that if deleted,
        would result in 30_000_000 or more in free
        space.
        """
        dirs = []
        h = root.height()
        for i in range(1, h+1):
            self._currentLevel(root, i, freeSpace, dirs)
        
        return dirs

    def _currentLevel(self, root: Node, level: int, freeSpace: int, dirs: list):
        if root is None:
            return

        if level == 1:
            if root.type == 'folder' and (root.nodeSize() + freeSpace) >= 30000000:
                    dirs.append(root)
        
        elif level > 1:
            for child in root.children:
                self._currentLevel(child, level - 1, freeSpace, dirs)

def parseLine(line: str, fileSystem: FileSystem):
    #Line is a command (cd or ls)
    if line.startswith("$"):
        tokens = line.strip().split(" ")
        match tokens[1]:
            case "cd":
                if tokens[2] == "..":
                    fileSystem.pwd = fileSystem.pwd.parent
                else:
                    if fileSystem.root is None:
                        #set the root and the pwd to '/'
                        folder = Folder('/', None)
                        fileSystem.root = folder
                        fileSystem.pwd = folder
                    
                    elif fileSystem.pwd.folderExists(tokens[2]) is not None:
                        fileSystem.pwd = fileSystem.pwd.folderExists(tokens[2])
                    
                    else:
                        #Create folder, Add it filesystem, and Update pwd
                        folder = Folder(tokens[2], fileSystem.pwd)
                        fileSystem.pwd.addNode(folder)
                        fileSystem.pwd = folder
                return 

            case "ls":
                return
    
    #Line is output of "ls" command
    else:
        tokens = line.strip().split(" ")
        if tokens[0] == "dir":
            #Create folder and add it as child of pwd
            folder = Folder(tokens[1], fileSystem.pwd)
            fileSystem.pwd.addNode(folder)
        else:
            #Create a file named tokens[1] and size tokens[0], as child of pwd
            file = File(tokens[1], fileSystem.pwd, int(tokens[0]))
            fileSystem.pwd.addNode(file)

if __name__ == "__main__":
    #1- Read the input file
    lines = readFile('input.txt')

    #2- Create and populate filesystem as I parse the input
    fileSystem = FileSystem()
    for line in lines:
        parseLine(line, fileSystem)

    #- 
    totalDiskSpace = 70000000
    totalUsedSpace = fileSystem.root.nodeSize()
    totalfreeSpace = totalDiskSpace - totalUsedSpace

    #4- Go through fileSystem and find dirs
    # to delete to free up enough space 
    dirs = fileSystem.findDirs(fileSystem.root, totalfreeSpace)

    #5- Print out the size of the smallest folder
    smallestFolder = dirs[0].nodeSize()
    for dir in dirs:
        if dir.nodeSize() < smallestFolder:
            smallestFolder = dir.nodeSize()

    print(f'The size: {smallestFolder}')