# if the seed is not mapped then it carries its value 
# loop throuh the list of seeds 
# find out if prevSource fits in this line 
    # if the prevSource fits then newDestination = (destination + (prevSource - source))
    # if the prevSource is not on this line then continue on 
    # if the prevSource is not in this mapping set then leave it alone
        # for the last two conditions I can likely just leave the number alone in general

# For some reason this code is not working properly, although I have solved the problem with it.
    # Using the testInput this code does each seed converstion properly except the last conversion
    # of the third seed. It is not converting 82 to 86 in "humidity-to-location"

import re

seeds = []

with open("testInput.txt") as input:

    mapInc = 0

    for line in input:

        line = line.strip()

        if "seeds" in line:
            seeds = re.findall(r'\d+', line)

            seedStatus = [0] * len(seeds)

        if "map" in line:
            mapInc += 1
            #print(seeds)
            seedStatus = [0] * len(seeds)
        

        if (("map" in line) == False and ("seeds" in line) == False and line != ""):

            lineNumbers = re.findall(r'\d+', line)
            print(seeds)
            print(lineNumbers)
            for seed in seeds:
                index = seeds.index(seed)
                if(seedStatus[index] == 0):
                    if  (int(lineNumbers[1]) <= int(seed) <= (int(lineNumbers[1]) + int(lineNumbers[2]))):
                        seeds[index] = (int(lineNumbers[0]) + (int(seed) - int(lineNumbers[1])))
                        seedStatus[index] = 1
    
lowestNum = min(seeds)

print(seeds)
print(lowestNum)