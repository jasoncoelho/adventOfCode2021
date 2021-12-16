from typing import Counter

with open('input.txt') as f:
    lines = f.readlines()

# read the input and get the coordinates and folds
lines = [ i.rstrip() for i in lines ]

template = list(lines[0])
insertionRules = { i[0] : i[1] for i in [rule.split(' -> ') for idx,rule in enumerate(lines) if idx > 1 ] }

print(insertionRules)

memo = {}

maxMemoSize = 20
maxSteps = 40

def findNearestMemo(key,steps):
    k = key+":"+str(steps)
    if k in memo:
        return (memo[k],steps)
    return (None,None)

def findPolymerizationCount(template,steps):

    if steps == 0:
        return Counter(template)

    ret = Counter()
    for i in range(0,len(template)-1):

        k = "".join(template[i:i+2])

        (found,s) = findNearestMemo(k,steps)
     
        if s==steps:
            ret += found
            ret -= Counter([template[i+1]])
        elif k in insertionRules:

            toInsert = insertionRules[k]
            ret += findPolymerizationCount([ template[i] , toInsert ],steps-1) 
           
            if steps > 1:
                ret += findPolymerizationCount([ toInsert, template[i+1] ],steps-1)
                ret -= Counter([toInsert,template[i+1]])
            
        else:
            ret += template[i]

    ret += Counter( template[len(template)-1] )

    return ret

# build a memo that can be used

for helper in [i for i in insertionRules]:
   
    p = list(helper)
    for step in range(1,maxMemoSize+1):
        counter = findPolymerizationCount(p,step)
        memo[helper + ":" + str(step)] = counter

print(memo)

# Solution 2188189693529 test.txt
# Solution 3906445077999 input.txt

print("-------")
counter = findPolymerizationCount(template,maxSteps)

most_common_element = counter.most_common(1)[0][1]
least_common_element = counter.most_common()[:-2:-1][0][1]

print("Solution",most_common_element-least_common_element)