#Based on opponent choice, return the score for one round
#if the user chooses the option that ends the round as expected
def determineRoundScore(opponentChoice, expectedOutcome):
    
    #My draft-2 shows how I derived this matrix
    matrix = [
        [2, 3, 1],
        [3, 1, 2],
        [1, 2, 3]
    ]

    opponentChoices = {
        'A': 0,
        'B': 1,
        'C': 2
    }

    i = opponentChoices[opponentChoice]
    #Case1: End the round with a loss
    if expectedOutcome == 'X':
        return 0 + matrix[i][1]
    #Case2: End the round with a draw
    elif expectedOutcome == 'Y':
        return 3 + matrix[i][2]
    #Case3: End the round with a win
    elif expectedOutcome == 'Z':
        return 6 + matrix[i][0]


    
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
    #print(RPS('input-test.txt')) #Expected: 12
    print(RPS('input.txt')) #Expected: 12767