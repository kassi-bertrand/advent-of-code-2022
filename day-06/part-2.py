#read file and return the lines in it
def readFile(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    return lines

"""
Tells if a given list contains distinct elements
    list    -> list of elements
"""
def isFinite(list):
    return len(set(list)) == len(list)

"""
Takes in a string and returns the number of character
before the first start-of-message marker is detected.
It implements a simple 4-characters sliding-window

    str     -> the datastream to process
"""
def charsBeforeStartOfMsg(string):
    start       = 0
    end         = 14
    processed   = 14 # of processed chars

    while end < len(string):
        #Grab first four characters
        tmp = string[start:end]
        if isFinite(tmp):
            return processed
        
        #move the sliding window 1 step forward
        start       += 1
        end         += 1
        processed   += 1
    
    return 0

if __name__ == "__main__":
    lines = readFile('input.txt')
    print(charsBeforeStartOfMsg(lines[0])) #Expected: 