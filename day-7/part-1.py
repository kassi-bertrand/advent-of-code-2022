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
        
        return max(temp) + 1

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
    def __init__(self) -> None:
        self.pwd = None
        self.root = None
    
    def findDirs(self, root: Node):
        """
        Uses level order traversal to determine
        the directories with at most 100,000 in size
        """
        dirs = []
        h = root.height()
        for i in range(1, h+1):
            self._currentLevel(root, i, dirs)
        
        return dirs

    def _currentLevel(self, root: Node, level: int, dirs: list):
        if root is None:
            return

        if level == 1:
            if root.type == 'folder':
                if root.nodeSize() < 100000:
                    dirs.append(root)
        
        elif level > 1:
            for child in root.children:
                self._currentLevel(child, level - 1, dirs)


class Interpreter:
    def __init__(self) -> None:
        self.fileSytem = FileSystem()
    
    def parseLine(self, line: str):
        #Line is a command (cd or ls)
        if line.startswith("$"):
            tokens = line.split(" ")
            match tokens[1]:
                case "cd":
                    #Create folder
                    #Add it filesystem
                    #Update pwd to newly created folder
                    return 

                case "ls":
                    return

                case _:
                    print("Unrecognized command")
        
        #Line is output of "ls" command
        else:
            tokens = line.split(" ")
            if tokens[0] == "dir":
                #Create folder named tokens[1]
                #add it as child of pwd
                pass
            else:
                #Create a file named tokens[1] and size tokens[0]
                #add it as child of pwd
                pass

if __name__ == "__main__":
    
    #TESTS - See if the Tree works :)
    root = Folder('/', None)
    file_1 = File('test1.txt', root, 12)
    root.addNode(file_1)
    #-----
    file_2 = File('test2.txt', root, 12)
    root.addNode(file_2)
    #-----
    folder_1 = Folder('folder', root)
    file_3 = File('test3', folder_1, 12)
    folder_1.addNode(file_3)
    #-----
    root.addNode(folder_1)
    #-----
    print(root.nodeSize()) #Expected 36
    print(root.height()) #Expected 2

    #SOLUTION
    lines = readFile('input-test.txt')
    for line in lines:
        pass

    #Determine the number of directories with size 100,000 or less
    #Traverse the tree level by level
    #Their total size