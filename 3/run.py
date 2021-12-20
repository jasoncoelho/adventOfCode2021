with open('input.txt') as f:
    lines = f.readlines()

lines = [ line.rstrip() for line in lines ]

def getPositionsOfAboveAverageOneBits(binaryLines, lineLen):

    counter = [ 0 for i in range(lineLen) ]

    for num in binaryLines:
        pos = 0
        while num != 0:        
            counter[pos] += num & 1
            num >>= 1
            pos += 1

    print(counter)
    return [ True if i >= len(binaryLines)/2 else False for i in counter ]

def getO2CO2Numbers(candidates, lineLen ,o2Toggle=True):

    position = lineLen - 1 # start with the left most bit

    # keep filtering the candidates until we have only one number
    while len(candidates) != 1:

        oneBitToggle = getPositionsOfAboveAverageOneBits(candidates,lineLen)[position]

        test = 1
        test <<= position 

        # print(bin(test), oneBitToggle, [ bin(i) for i in candidates ])

        # filter candidates while testing for 
        #  - either one or zero in the relevant position
        #  - either o2 or co2 based on the toggle
        candidates = [ c for c in candidates if ((c & test == test) ^ (not oneBitToggle)) ^ (not o2Toggle)  ] 
        
        position -= 1 # move right to the next bit
    
    print([ bin(i) for i in candidates ])
        
    return candidates[0]

def getGammaAndEpsilonFromOneBitCounter(positionsOfAboveAverageOneBits):

    gamma = 0
    epsilon = 0

    for i,aboveAverageOneBits in enumerate(reversed(positionsOfAboveAverageOneBits)):
        if aboveAverageOneBits: # common 1 bit
            gamma |= 1    
        else:
            epsilon |= 1

        # don't want to shift if this is the last one
        if i < len(positionsOfAboveAverageOneBits)-1:
            epsilon <<= 1
            gamma <<= 1

    return gamma,epsilon

binaryLines = [ int(l,2) for l in lines ]

positionsOfAboveAverageOneBits = getPositionsOfAboveAverageOneBits(binaryLines,len(lines[0]))
print("Counter",positionsOfAboveAverageOneBits)

gamma,epsilon = getGammaAndEpsilonFromOneBitCounter(positionsOfAboveAverageOneBits)
print("Gamma",gamma,"Epsilon",epsilon,"Solution", gamma * epsilon,"\n")

o2rating = getO2CO2Numbers(binaryLines,len(lines[0]))
co2rating = getO2CO2Numbers(binaryLines,len(lines[0]),False)
print("O2 Rating",o2rating,"C02 Rating",co2rating,"Solution", o2rating * co2rating)