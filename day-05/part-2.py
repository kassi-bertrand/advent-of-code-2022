import re

#read file and return the lines in it
def readFile(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    return lines

"""
Uses "lines" and return all procedure as a list of lists (of integer)
Where each list represents a SINGLE move
Each list is of the form [x, y, z] where:
    x   -> # of crates to be moved
    y   -> src stack
    z   -> dst stack
"""
def procedureList(lines):
    procedure = []
    regex = "([0-9]+)"
    
    for line in lines:
        list = re.findall(regex, line) #Match all numbers in "line" using regex
        for i, element in enumerate(list):
            list[i] =  int(element)
        #add list of integers to procedure
        procedure.append(list)
    
    return procedure

"""
Move a group of crates from one stack to another
"""
def moveCrates(stacks, crateNumber, srcStack, dstStack):
    #Cannot move more crates than there already is.
    if len(stacks[srcStack]) < crateNumber:
        return

    #Move crate(s) all at ONCE... while PRESERVING order
    tmpList = []
    #1-     Store relevant crate in tmpList in order
    for i in range(crateNumber, 0, -1):
        tmpList.append(stacks[srcStack][i * -1])
    
    #2-     Remove crate from srcStack
    for _ in range(crateNumber):
        stacks[srcStack].pop()
    
    #3-     Extend dstStack
    stacks[dstStack].extend(tmpList)

if __name__ == "__main__":

    #Initial stack of crates from the "input.txt"
    stacks = [
        [],
        ['V', 'C', 'D', 'R', 'Z', 'G', 'B', 'W'],
        ['G', 'W', 'F', 'C', 'B', 'S', 'T', 'V'],
        ['C', 'B', 'S', 'N', 'W'],
        ['Q', 'G', 'M', 'N', 'J', 'V', 'C', 'P'],
        ['T', 'S', 'L', 'F', 'D', 'H', 'B'],
        ['J', 'V', 'T', 'W', 'M', 'N'],
        ['P', 'F', 'L', 'C', 'S', 'T', 'G'],
        ['B', 'D', 'Z'],
        ['M', 'N', 'Z', 'W']
    ]

    #Read in the list of individual moves
    lines = readFile('procedure.txt')
    procedures = procedureList(lines)

    #Move the crates around
    for procedure in procedures:
        moveCrates(stacks, procedure[0], procedure[1], procedure[2])

    #Gather elements on top of each stack and print them
    for index in range(1, len(stacks)):
        currList = stacks[index]
        print(currList[len(currList) - 1], end="") #Expected VLCWHTDSZ