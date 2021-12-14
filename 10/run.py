import math

with open('input.txt') as f:
    lines = f.readlines()

closingChunkChars = { '>' : '<' , '}' : '{' , ']' : '[' , ')' : '(' }
closingChunkCharsInverse = { '<' : '>' , '{' : '}' , '[' : ']' , '(' : ')' }

closingChunkCharPoints = { '>' : 25137, '}' : 1197, ']' : 57, ')' : 3 }
incompleteLinePoints = { '>' : 4, '}' : 3, ']' : 2, ')' : 1 }

syntaxErrorScore = 0
totalScores = []

for line in lines:
    
    line = line.rstrip()

    stack = []

    syntaxErrorLine = False

    for closingChunkChar in list(line):

        if closingChunkChar in closingChunkChars:
            stackTop = stack.pop()
            expectedStartingChunkChar = closingChunkChars[closingChunkChar]
            if stackTop != expectedStartingChunkChar:
                # print("Found ",closingChunkChar, "Expected closing char for ",stackTop)
                syntaxErrorScore += closingChunkCharPoints[closingChunkChar]
                syntaxErrorLine = True
                break
        else:
            stack.append(closingChunkChar)

    if len(stack) > 0 and not syntaxErrorLine :
        totalScore = 0
        while len(stack) > 0:
            stackTop = stack.pop()
            closingChunkChar = closingChunkCharsInverse[stackTop]
            totalScore = (totalScore * 5) + incompleteLinePoints[closingChunkChar]    
        totalScores.append(totalScore)

print("Syntax Error Score ",syntaxErrorScore)

list.sort(totalScores)

print("Middle Score ",totalScores[math.floor(len(totalScores)/2)])

# 26397 for test.txt
# 1605968119
