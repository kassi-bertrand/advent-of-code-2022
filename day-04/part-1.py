#read file and return the lines in it
def readFile(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    return lines

#If "rangeA" contains "rangeB", return "1"
#If "rangeB" contains "rangeA", return "-1"
#If "rangeA" and "rangeB" are disjoint, return "0"
def isContained(rangeA, rangeB):
    if rangeA[0] <= rangeB[0] and rangeA[1] >= rangeB[1]:
        return 1
    elif rangeA[0] >= rangeB[0] and rangeA[1] <= rangeB[1]:
        return -1
    else:
        return 0

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


def pairsContainingAnother(lines):
    total = 0
    #- For each pair (i.e. line)
    for line in lines:
        tuples = parseLine(line)
        i = isContained(tuples[0], tuples[1])
        if i == 1 or i == -1:
            total += 1

    return total
    
if __name__ == "__main__":
    lines = readFile('input.txt')
    print(pairsContainingAnother(lines)) #Expected 433