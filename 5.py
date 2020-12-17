file = open('Inputs/input5.txt')
input5 = file.readlines()

totRow = 128 #from 0 to 127
totCols = 8 #from 0 to 7

IDs = []
# start = 0
# finish = 128

for line in input5:
    dicc = {}

    start = 0
    finish = 127
    row = 0

    startc = 0
    finishc = 7
    column = 0

    for letter in line:
        largest = round(abs((finish-start)/2),0) #CLOSER TO 128
        smallest = largest-1 #Closer to 0

        largestc = round(abs((finishc-startc)/2),0)
        smallestc = largestc-1 #Closer to 0

        if abs((finish-start))==1:
            if letter == 'F':
                row = start
            elif letter == 'B':
                row = finish
        
        if abs((finishc-startc))==1:
            if letter == 'L':
                column = startc
            elif letter == 'R':
                column = finishc

        else:
            if letter == 'F':
                finish = start+smallest
            elif letter == 'B':
                start = (finish+1)-largest
            elif letter == 'L':
                finishc = startc + smallestc
            elif letter == 'R':
                startc = (finishc+1)-largestc

        #print(letter,'Column: ',startc,finishc,'\n','Row: ',start,finish)
    # print(row,column)
    dicc[row] = [column,int(row*8+column)]
    IDs.append(dicc)
    
# print('ROWS AND COLUMNS')
# for i in IDs:
#     print(i)

#CHECK THE HIGHEST ID
highest = 0
idList = []
for rc in IDs:
    for key in rc:
        iD = rc[key][1]
        idList.append(iD)
        if iD>=highest:
            highest = iD

print(highest)

#Part 2
idList.sort()
for index in range(len(idList)-1):
    if idList[index]+1 != idList[index+1]:
        print(idList[index]+1)