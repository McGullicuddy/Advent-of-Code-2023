# find numbers that are adjacent to symbols and add them together 
# adjacent mmeaning (on top of, below, to the right or left of, or diagonal in any direction)

# run through entire text, finding each symbol, and storing its locatino in an array,
# go back through each line, find a number
# compare that numbers location with the numbers coresponging to the symbols.
#    using the length of each of line and the current location of the number we can determine 


import re

inc = 1
symbolLocations = []
lineLength = 140
numberLocations = []
validNumbers = []
total = 0

# I need to compare the location I get with the digits of adjacent loactions
# I can use the math from part 1 
#if an adjacent location is a digit I want to save that location and return it 
# the problem is that if I get multipul locations for a single number how will i process that 
# add the set number to an array 
#   if the set number is already in that set then we likely know that number has already been used 



def surroundingNumbers(locations):
    tempFactors = []

    for location in locations:
        temp = []

        for set in numberLocations:

            if (location + lineLength) in numberLocations[numberLocations.index(set)][0]:
                if (set in temp) == False:
                    temp.append(set)

            if (location - lineLength) in numberLocations[numberLocations.index(set)][0]:
                if (set in temp) == False:
                    temp.append(set)

            if (location + 1) in numberLocations[numberLocations.index(set)][0]:
                if (set in temp) == False:
                    temp.append(set)

            if (location - 1) in numberLocations[numberLocations.index(set)][0]:
                if (set in temp) == False:
                    temp.append(set)

            if (location - lineLength - 1) in numberLocations[numberLocations.index(set)][0]:
                if (set in temp) == False:
                    temp.append(set)
            
            if (location - lineLength + 1) in numberLocations[numberLocations.index(set)][0]:
                if (set in temp) == False:
                    temp.append(set)

            if (location + lineLength + 1) in numberLocations[numberLocations.index(set)][0]:
                if (set in temp) == False:
                    temp.append(set)
            
            if (location + lineLength - 1) in numberLocations[numberLocations.index(set)][0]:
                if (set in temp) == False:
                    temp.append(set)
            
            #print(temp)

            if len(temp) == 2:
                product = temp[0][1] * temp[1][1]
                tempFactors.append(product)
                temp = []

        
    print(tempFactors)

    return tempFactors


with open ("input") as input:

    lineInc = 0

    for line in input:

        line = line.strip()
        
        for character in line:

            if(character == '*'):
                symbolLocations.append(inc)

            inc = inc + 1


with open ("input") as input:

    lineInc = 0
    
    for line in input:

        line = line.strip()

        for data in re.finditer(r'\d+', line):

            number = int(data.group())
            numberSpan = list(data.span())
            numberSpan[0] = numberSpan[0] + 1 + lineInc
            numberSpan[1] = numberSpan[1] + lineInc
            if(numberSpan[1] - numberSpan[0] > 1):
                numberSpan.insert(1, numberSpan[1] - (numberSpan[1] - numberSpan[0] - 1))
            numberLocations.append([numberSpan,number])

        lineInc += lineLength
    
factors = surroundingNumbers(symbolLocations)

for x in factors:
    total += x

print(total)
#print(symbolLocations)
#print(numberLocations)