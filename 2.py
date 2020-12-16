import collections

file = open('input2.txt','r')
input = file.readlines()

timesx = []
letters = []
password = []
for line in input:
    timesLetter = line.split(' ')
    # print(timesLetter)
    timesx.append(timesLetter[0].split('-'))
    letters.append(timesLetter[1][0])
    password.append(timesLetter[2])

correctPassword = 0

for index in range(len(timesx)):
    letra = letters[index]
    passw = password[index]
    listTimes = timesx[index]
    least = int(listTimes[0])
    most = int(listTimes[1])

    frequencies = collections.Counter(passw)
    repeated = {}
    for key, value in frequencies.items():
        if value>0:
            repeated[key] = value

    repeticiones = 0
    if letra in repeated:
        repeticiones = repeated[letra]
        if repeticiones>=least and repeticiones<=most:
            correctPassword+=1

print(correctPassword)

#Part 2
correctPassword2 = 0

for index in range(len(timesx)):
    letra = letters[index]
    passw = password[index]
    listTimes = timesx[index]
    ind1 = int(listTimes[0])-1
    ind2 = int(listTimes[1])-1

    letra1 = passw[ind1]
    letra2 = passw[ind2]

    if letra1==letra and letra2!=letra:
        correctPassword2+=1
    elif letra2==letra and letra1!=letra:
        correctPassword2+=1

print(correctPassword2)