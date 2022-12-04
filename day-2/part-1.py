#Compare the two inputs for one round and returns the score
def determineRoundScore(opponentChoice, playerChoice):

    possibleChoices = {
        'X': 1,
        'Y': 2,
        'Z': 3,
        'A': -1,
        'B': -2,
        'C': -3
    }

    sum = possibleChoices[opponentChoice] + possibleChoices[playerChoice]
    #Case 1: Draw
    if sum == 0:
        return 3 + possibleChoices[playerChoice]

    #Case 2: Player choice is stronger than opponent
    elif sum == 1 or sum == -2:
        return 6 + possibleChoices[playerChoice]

    #Case 3: Player choice is weaker than opponent
    elif sum == -1 or sum == 2:
        return 0 + possibleChoices[playerChoice]

    

#This function simulates rounds
#of Rock Paper Scissors and returns
#the player's total score
def RPS(filename):
    finalScore = 0
    
    #Read the file
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()

    #for each line
    for line in lines:
        curr = line.splitlines() #line contains '\n' I don't want that
        choices = curr[0].split(" ")
        opponentChoice = choices[0]
        playerChoice = choices[1]
        #determine score for current round, then update score
        finalScore += determineRoundScore(opponentChoice, playerChoice)
    
    return finalScore

if __name__ == "__main__":
    #print(RPS('input-test.txt')) #Expected: 15
    print(RPS('input.txt')) #Expected: 11666