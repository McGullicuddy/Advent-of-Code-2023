#rules
    # secret number of cubes in bag
    # Goal is to find info about the cubes (using what I assume will be probabilty or process of emlinimation)
    # 3 times per game he revals a random set of cubes
    # Using the data, the elf wants to know which games would have been impossible if
        # the bag only contained 12 r, 13 g, and 14 b
    # sum the ids of the games that were possible

    # I think I was wrong about this being about probability, i think it is v straight forward

# read line
# go through each word 
# keep track of total count by adding onlytthe game numbers of the valid games to an array 
    # Add the array up and output
# Now I have to figure out how to sort through each of the lines and make sure each of the values are 
#   under the corresponding vlaues (12, 13 ,14)
# I might be able to do this using the game sperators in the text (: ; ,)

# okay I got 90% of the way there and now I need to figure out how to write my if statments in order
#   to add the 

# its working now

import re

redCubes = 12
greenCubes = 13
blueCubes = 14
gameIncrementor = 1
validGames = []
isValid = 0
total = 0

with open ("input", 'r') as input:
    for line in input:
        
        for game in line.split(':'):
            
            for set in game.split(';'):

                for color in set.split(','):
                    
                    number = re.findall(r'\d+', color)

                    if(("red" in color and int(number[0]) > redCubes) or ("green" in color and int(number[0]) > greenCubes) or ("blue" in color and int(number[0]) > blueCubes)):
                        isValid = 1

        if(isValid == 0):
            validGames.append(gameIncrementor)
        isValid = 0
        gameIncrementor = gameIncrementor + 1

for num in validGames:
    total = total + int(num)

print(total)
