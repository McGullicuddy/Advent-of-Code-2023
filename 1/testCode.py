array1 = []
array2 = []
total = 0

with open ("testInput.txt") as input:
    for x in input:
        for z in x:
            if(z.isdigit()):
                array1.append(z)
        test = len(array1)
        lineTotal = str(array1[0]) + str(array1[test - 1])
        print(lineTotal)
        array1.clear()
        array2.append(int(lineTotal))
    for x in array2:
        total = total + x

    print(total)