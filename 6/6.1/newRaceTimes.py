# loop through the time, multiply buttonTime by m/s 

import re
from time import perf_counter

t1_start = perf_counter() 

times = []
distances = []
time = ''
distance = ''
numOfTimes = []
total = 1


with open ("input") as input:

    firstLine = input.readline()
    secondLine = input.readline()

    times = re.findall(r'\d+', firstLine)
    distances = re.findall(r'\d+', secondLine)

    for i in range(0, len(times)):
        time += times[i]
        distance += distances[i]

        
    metersPerSecond = 0
    numOfWins = 0

    for buttomTime in range(0, int(time)):
        
        if ((int(time) - buttomTime) * metersPerSecond > int(distance)):
            numOfWins += 1
        
        metersPerSecond += 1

t1_stop = perf_counter()
print("Elapsed time during the whole program in seconds:", t1_stop-t1_start)

print(numOfWins)







