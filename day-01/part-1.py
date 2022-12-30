#This function reads in a list of
#number representing calories
#and returns the max number of
#calories

def maxColories(filename):
    maxColories = 0
    
    #read lines in the file
    file = open(filename, 'r')
    lines = file.readlines()

    #Compute the total number
    #of calories per elf, and compare
    #to 'maxColories'
    temp = 0
    for line in lines:
        if line == '\n':
            if temp > maxColories:
                maxColories = temp
            temp = 0
        else:
            temp += int(line)

    return maxColories

if __name__ == '__main__':
    #print(maxColories('input-test.txt')) #Expected Result is: 24000
    print(maxColories('input.txt'))