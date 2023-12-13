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

    gameNumber = 1
    points = []

    for set in winningNumbers:
        
        howMany = 0

        for winningNumber in set:

            if winningNumber in numbersYouHave[gameNumber - 1]:

                howMany += 1
        if howMany == 1:
            points.append(1)
        if howMany > 1:
            points.append(pow(2, howMany - 1))
        print(points)

        gameNumber += 1

for x in points:
    totalPoints += x

print(totalPoints)