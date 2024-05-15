import re

seeds = []
tempSeeds = []

with open("input.txt") as input:

    mapInc = 0

    for line in input:

        line = line.strip()

        if "seeds" in line:
            tempSeeds = re.findall(r'\d+', line)
            seedStatus = [0] * len(seeds)

            for seed in tempSeeds:
                if(tempSeeds.index(seed) % 2 == 0):
                    for i in range(int(seed), int(seed) + int(tempSeeds[tempSeeds.index(seed) + 1]) + 1):
                        seeds.append(i)
                        
        if "map" in line:
            mapInc += 1
            #print(seeds)
            seedStatus = [0] * len(seeds)

    
lowestNum = min(seeds)

print(seeds)
print(lowestNum)