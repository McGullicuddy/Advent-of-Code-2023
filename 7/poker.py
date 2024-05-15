import re

bids = []
hands = []

def determineType(currentHand):
    for card in currentHand:
        if

# find the bid and hand values and put them into their own arrays for future processing 
with open ("testInput") as input:
    
    for line in input:

        line = line.strip()
        
        bids.append(int(re.findall(r'\d+', line)[-1]))

        line = line.split(' ')

        hands.append(list(line[0]))

# hands can only be 5 cards so I dont think there is any reason to use a nested loop
for hand in hands:
    print(hand)

