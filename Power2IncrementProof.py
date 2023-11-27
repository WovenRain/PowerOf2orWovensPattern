outcomesDictionary = {}

placeholderDictionary = {}
#loop over higher numbers 1-N x
for testNumber in range(35000):
    lastPosition = 0
    placeholderDictionary = {}

    for increment in range(testNumber):
        # position on circle

        # the increment can be any odd number, the first i tried was 1
        # ie 0,1,2,3,4. But any odd number ive tried seems to work
        # ie 0,3,6,9,12 or 0,9,18,27,36

        position = (lastPosition + increment)%testNumber
        lastPosition = position

        # check for repeat of number  
        if position in placeholderDictionary:
            break
        else:
            placeholderDictionary[position] = True
    
    #find size of dictionary == x
    outcomesDictionary[testNumber] = (len(placeholderDictionary) == testNumber)

#get list of successess
outcomesFile = open("output.txt", "w")
for x in range(len(outcomesDictionary)):
    if outcomesDictionary[x] == True:
        outcomesFile.write(str(x) + "\n")
        
