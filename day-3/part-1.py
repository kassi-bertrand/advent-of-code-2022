from collections import Counter

#read file and return the lines in it
def readFile(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    return lines

#Determines and returns the priority of a single character
#See my notes on how I derived formula
def priority(char):
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 38

#Determine and return the sum of priorities
def sumOfPriorities(rucksacks):
    sumOfPriorities = 0
    #1- For each rucksack
    for rucksack in rucksacks:
        #2- Split it in two
        n = len(rucksack) // 2
        partA = rucksack[:n]
        partB = rucksack[n: len(rucksack)]

        #3- Form two hasmaps, representing the compartments
        compA = Counter(partA)
        compB = Counter(partB)
        
        #- For each item, determine if in other compartment
        for key in compA:
            #Yes? Compute priority
            if key in compB:
                sumOfPriorities += priority(key)
            #No? Next item
        
        

    return sumOfPriorities

if __name__ == "__main__":
    #rucksacks = readFile('input-test.txt') #Expected: 157
    rucksacks = readFile('input.txt') #Expected: 157
    print(sumOfPriorities(rucksacks)) #Expected: 7817