#read file and return the lines in it
def readFile(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    return lines

#Determines priority of a single character
def priority(char):
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 38

#Determines common item in a group(3-item) list
def intersect(strList):
    if len(strList) != 3:
        print("List size should be 3")
        return

    setA = set(strList[0])
    setB = set(strList[1])
    setC = set(strList[2])
    
    intersection = setA & setB & setC # '&' means intersection
    if len(intersection) == 0:
        return None
    else:
        return next(iter(intersection)) #1st element


def sumOfPriorities(rucksacks):
    sumOfPriorities = 0
    list = []
    #- For Every 3 line (rucksacks)
    for i in range(len(rucksacks)):
        if i != 0 and (i + 1) % 3 == 0:
            list.append(rucksacks[i]) #add every 3rd element
            #Determine common item (i.e. badge) in the 3-item list
            badge = intersect(list)
            print(badge)
            sumOfPriorities += priority(badge)
            #Clear the list to get ready for the next group
            list.clear()
        else:
            list.append(rucksacks[i])
    
    return sumOfPriorities

if __name__ == "__main__":
    rucksacks = readFile('input-test.txt')
    print(sumOfPriorities(rucksacks)) #Expected result: 70