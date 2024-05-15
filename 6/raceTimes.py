# loop through the time, multiply buttonTime by m/s 

import re

times = []
distances = []
numOfTimes = []
total = 1

with open ("input") as input:

    firstLine = input.readline()
    secondLine = input.readline()

    times = re.findall(r'\d+', firstLine)
    distances = re.findall(r'\d+', secondLine)
    
    for race in range(0, len(times)):
        
        metersPerSecond = 0
        numOfWins = 0

        for buttomTime in range(0, int(times[race])):
            
            if ((int(times[race]) - buttomTime) * metersPerSecond > int(distances[race])):
                numOfWins += 1
            
            metersPerSecond += 1
        
        numOfTimes.append(numOfWins)


for x in numOfTimes:
    total *=  x

print(numOfTimes)
print(total)


