#Read input file
# loop to read each line 
    #
        #From left to right, grab the first value 
        #From right to left grad the first value 
        #Add these values togehter 

array1 = []
array2 = []
total = 0

with open ("input.txt") as input:
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
