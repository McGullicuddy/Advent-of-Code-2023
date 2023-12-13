#The only way I have though about doing this so far is to read from left to ringht and append each
# valid value to an array, one we have that array we take the first and last value

# if(isdigit)
    # Add to array and move to next character
# elif (is char == 'o')
    # (dose that charcter and the next 4 have the word one in it)
    # if so then add that word to the array and move on
# elif (is char == 't')
    # (does that charcter and the next 4 have the word two in it)
        # if so then add that word to the array and move on
    # (does that charcter and the next 4 have the word three in it)
        # if so then add that word to the array and move on
# elif (is char == 'f')
    # (does that charcter and the next 4 have the word four in it)
        # if so then add that word to the array and move on
    # (does that charcter and the next 4 have the word five in it)
        # if so then add that word to the array and move on
# elif (is char == 's')
    # (does that charcter and the next 4 have the word six in it)
        # if so then add that word to the array and move on
    # (does that charcter and the next 4 have the word seven in it)
        # if so then add that word to the array and move on
# elif (is char == 'e')
    # (does that charcter and the next 4 have the word eight in it)
# elif (is char == 'n')
    # (does that charcter and the next 4 have the word nine in it)


one = "one"
two = "two"
three = "three"
four = "four"
five = "five"
six = "six"
seven = "seven"
eight = "eight"
nine = "nine"

array1 = []
array2 = []
total = 0
characterIterator = 0

with open ("testInput") as input:
    for word in input:
        for character in word:
            if(character.isdigit()):
                array1.append(character)
            elif(character == 't'):
                if ((characterIterator+2 < len(word)) and (two in (word[characterIterator:characterIterator+3]))):
                    array1.append('2')
                if ((characterIterator+3 < len(word)) and (three in (word[characterIterator:characterIterator+4]))):
                    array1.append('3')
        arrayLength = len(array1)
        if(arrayLength > 0):
            lineTotal = str(array1[0]) + str(array1[arrayLength - 1])
            print(array1)
            array2.append(int(lineTotal))
            print(lineTotal)
            array1.clear()
    for x in array2:
        total = total + x

    print(total)
