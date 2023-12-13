# find numbers that are adjacent to symbols and add them together 
# adjacent mmeaning (on top of, below, to the right or left of, or diagonal in any direction)

# run through entire text, finding each symbol, and storing its locatino in an array,
# go back through each line, find a number
# compare that numbers location with the numbers coresponging to the symbols.
#    using the length of each of line and the current location of the number we can determine 


import re

inc = 1
symbols = ['*', '/', '@', '$', '+', '#', '&', '%', '=', '-']
symbolLocations = []
numberLocations = []
lineLength = 140
lineInc = 0
validNumbers = []
total = 0

#I need to check to see if the symbol location is adjacent to any of the other location (8 locations)
# above the number (numberLocation - lineLength)
# below the number (numberLocation + lineLength)
# Right            (numberLocation + 1)
# Left             (numberLocation - 1)
# top Right        (numberLocation - lineLength - 1)
# top left         (numberLocation - lineLength + 1)
# bottom right     (numberLocation + lineLength + 1)
# bottom left      (numberLocation + lineLength - 1)
def checkAdjacency(numbers):
    valid = 0
    for number in numbers:
        if ((int(number) - lineLength in symbolLocations) or 
            (int(number) + lineLength in symbolLocations) or 
            (int(number) + 1 in symbolLocations) or 
            (int(number) - 1 in symbolLocations) or 
            (int(number) - lineLength - 1 in symbolLocations) or 
            (int(number) - lineLength + 1 in symbolLocations) or 
            (int(number) + lineLength + 1 in symbolLocations) or 
            (int(number) + lineLength - 1 in symbolLocations)):
            valid = 1
        if valid != 0:
            return valid
    return valid

with open ("input") as input:

    for line in input:

        for character in line:

            if(character in symbols):

                symbolLocations.append(inc)

            if(character.isspace() == 0):
                
                inc = inc + 1

#check each value to see if it is an integer , if so add it to a list 
# know when a number continues by setting a tempVariable to 1 if the last chracter was a number
with open ("input") as input:
    for line in input:

        for data in re.finditer(r'\d+', line):

            number = int(data.group())
            numberSpan = list(data.span())
            numberSpan[0] = numberSpan[0] + 1 + lineInc
            numberSpan[1] = numberSpan[1] + lineInc

            if checkAdjacency(numberSpan) == 1:
                validNumbers.append(number)

        lineInc += lineLength

for x in validNumbers:
    total = total + int(x)

#print(symbolLocations)
#print(numberLocations)
print(validNumbers)
print(total)
