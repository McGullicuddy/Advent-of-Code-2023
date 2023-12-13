#for this one we have to find the highest value of each cube type in each game
#   this will act as our "fewest number of cubes of each color"

# to do this we can continue to use the same loops as last time in order to break the lines down,
#   but this time we will need to 


import re

gameIncrementor = 1
colorValue = []
power = 0
totalPerGame = []
tempRed = 0
tempBlue = 0
tempGreen = 0
total = 0

with open ("input", 'r') as input:
    for line in input:
        
        for game in line.split(':'):
            
            for set in game.split(';'):

                for color in set.split(','):
                    
                    number = re.findall(r'\d+', color)

                    if("red" in color and int(number[0]) > tempRed):
                        tempRed = int(number[0])

                    elif("blue" in color and int(number[0]) > tempBlue):
                        tempBlue = int(number[0])

                    elif("green" in color and int(number[0]) > tempGreen):
                        tempGreen = int(number[0])
        power = (tempGreen * tempBlue * tempRed)
        totalPerGame.append(power)
        tempRed = 0
        tempBlue = 0
        tempGreen = 0

for x in totalPerGame:
    total = total + x

print(total)