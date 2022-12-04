#This function reads in a list of
#number representing calories
#and returns the total calories
#carries by the three elves
#with the most calories

def maxColories(filename):
    caloriesPerElf = []
    
    #read lines in the file
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()

    #Compute the total number
    #of calories per elf, add it to "caloriesPerElf"
    temp = 0
    for i in range(len(lines)):
        if i == len(lines) - 1:
            caloriesPerElf.append(int(lines[i]))
        elif lines[i] == '\n':
            caloriesPerElf.append(temp)
            temp = 0
        else:
            temp += int(lines[i])
        

    #sort callories from great to least
    caloriesPerElf.sort(reverse=True)

    #add the first 3 and returns the final result
    totalCalories = 0
    for i in range(3):
        totalCalories += caloriesPerElf[i]
    
    return totalCalories

if __name__ == '__main__':
    #print(maxColories('input-test.txt')) #Expected Result is: 45000
    print(maxColories('input.txt'))