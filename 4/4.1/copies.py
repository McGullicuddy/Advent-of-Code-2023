#holy moly the prompt on this challenge hurt my brain
# I am going to write it out to try and understand it 

# RULES
# you win copies of the scratchcards below the winning card equal to the number of matches
# 

import re

winningNumbers = []
numbersYouHave = []
totalPoints = 0
with open ("input") as input:

    for line in input:

        line = line.strip()
        line = line.split(":")[1]

        winningNumbers.append(re.findall(r'\d+', line.split("|")[0]))
        numbersYouHave.append(re.findall(r'\d+', line.split("|")[1]))


with open ("input") as input:

    gameNumber = 0
    totalLines = len(input.readlines())
    copies = [1] * totalLines


for set in winningNumbers:
    
    temp = copies[winningNumbers.index(set)]

    howMany = 0
    for winningNumber in set:

        if winningNumber in numbersYouHave[gameNumber]:

            howMany += 1
            copies[gameNumber + howMany] +=  1 * temp

    gameNumber += 1

for x in copies:
    totalPoints += x
print(totalPoints)