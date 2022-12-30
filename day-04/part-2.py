#read file and return the lines in it
def readFile(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    return lines

#Returns "1" if rangeA and rangeB overlap, "0" otherwise
def overlap(rangeA, rangeB):
    if rangeA[0] <= rangeB[1] and rangeB[0] <= rangeA[1]:
        return True
    else:
        return False

#Parses lines of the form: a-b,c-d and returns [(a,b), (c,d)]
def parseLine(line):
    list = []
    pairs = line.split(",") #["a-b", "c-d"]
    for pair in pairs:
        nums = pair.split("-")
        list.append(
            (int(nums[0]), int(nums[1]))
        )

    return list

def pairsOverlapping(lines):
    total = 0
    #- For each pair (i.e. line)
    for line in lines:
        tuples = parseLine(line)
        if overlap(tuples[0], tuples[1]):
            total += 1
    
    return total

if __name__ == "__main__":
    lines = readFile('input.txt')
    print(pairsOverlapping(lines))