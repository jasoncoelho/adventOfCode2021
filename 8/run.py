from collections import Counter

with open('input.txt') as f:
    lines = f.readlines()

def isUniqueCharSignal(u):
    return len(Counter(u)) == len(u)

def getOneFourSevenEight(signals):

    # 1 = 2 uniq chars, 4 = 4 unique chars, 7 = 3 unique chars, 8 = 7 unique chars
    k = { 2 : 1, 3 : 7 , 4 : 4 , 7 : 8 }

    return { k[len(i)]:i for i in getOneFourSevenEightNoUnique(signals) } 

def getOneFourSevenEightNoUnique(signals):
    return [ i for i in signals if len(i) in [2,3,4,7] ]

def getTwoThreeFive(signals):
    return [ set(i) for i in signals if len(i) == 5 ]

def getWiring(unique):

    u = getOneFourSevenEight(unique)

    # get chars exclusive to one , seven , four and eight
    oneChars = set(u[1])
    sevenChars = set(u[7]).difference(oneChars) 
    fourChars = set(u[4]).difference(oneChars) 
    eightChars = set(u[8]).difference(fourChars).difference(sevenChars).difference(oneChars)

    # build our intial set of wiring assumptions
    wiring = {  'a':0 ,'b':0 ,'c':0 ,'d':0 , 'e':0, 'f':0, 'g':0 } 
    wiring['b'] = wiring['c'] = oneChars
    wiring['a'] = list(sevenChars)[0]
    wiring['f'] = wiring['g'] = fourChars
    wiring['d'] = wiring['e'] = eightChars

    # get chars to two, three and give
    twoThreeFive = getTwoThreeFive(unique)

    # we can determine the chars in three
    threeChars = [ i for i in twoThreeFive if oneChars.issubset(i) ][0]
    # we can determine the chars NOT in three by removing the chars in three that are also in eight
    notThreeChars = set(u[8]).difference(threeChars)

    # knowing what is not in 3 we can solidify what is in positions 3,4,5 and 6
    wiring['g'] = list(wiring['g'].difference(notThreeChars))[0]
    wiring['f'] = list(wiring['f'].difference(wiring['g']))[0]
    wiring['d'] = list(wiring['d'].difference(notThreeChars))[0]
    wiring['e'] = list(wiring['e'].difference(wiring['d']))[0]

    # we can now definitively pick the chars in two and therefore the positions at 1 and 2
    twoChars = [ i for i in twoThreeFive if not set(wiring['f']).issubset(i) and set(wiring['e']).issubset(i)   ][0]

    wiring['b'] = list(twoChars.intersection(wiring['b']))[0]
    wiring['c'] = list(wiring['c'].difference(set(wiring['b'])))[0]

    # and generate the wiring for each number
    numbers = {}  
    numbers[0] = {wiring['a'],wiring['b'],wiring['c'],wiring['d'],wiring['e'],wiring['f']}
    numbers[1] = {wiring['b'],wiring['c']}
    numbers[2] = {wiring['a'],wiring['b'],wiring['g'],wiring['e'],wiring['d']}
    numbers[3] = {wiring['a'],wiring['b'],wiring['c'],wiring['d'],wiring['g']}
    numbers[4] = {wiring['f'],wiring['g'],wiring['b'],wiring['c']}
    numbers[5] = {wiring['a'],wiring['f'],wiring['g'],wiring['c'],wiring['d']}
    numbers[6] = {wiring['a'],wiring['f'],wiring['e'],wiring['d'],wiring['c'],wiring['g']}
    numbers[7] = {wiring['a'],wiring['b'],wiring['c']}
    numbers[8] = {wiring['a'],wiring['b'],wiring['c'],wiring['d'],wiring['e'],wiring['f'],wiring['g']}
    numbers[9] = {wiring['a'],wiring['b'],wiring['c'],wiring['d'],wiring['f'],wiring['g']}

    return wiring, numbers

def getNumber(displaySignal,numbers):
    return [ i for i in numbers if numbers[i] == displaySignal][0]

countOfOneFourSevenEight = 0
countOfAllNumbers = 0

for line in lines:

    (unique, display) = line.rstrip().split("|")
    
    (unique, display) = ([i for i in unique.split(" ") if i != ''],[j for j in display.split(" ") if j != ''])

    displayCharSignals = getOneFourSevenEightNoUnique(display)

    countOfOneFourSevenEight += len(displayCharSignals) 

    wiring,numbers = getWiring(unique)

    allnumbers = int("".join([  str(getNumber(set(i),numbers)) for i in display ]))
              
    countOfAllNumbers += allnumbers

print("Count of One Four Seven Eight = ",countOfOneFourSevenEight)
print("Count of All Numbers = ",countOfAllNumbers)

# Count of One Four Seven Eight =  349
# Count of All Numbers =  1070957