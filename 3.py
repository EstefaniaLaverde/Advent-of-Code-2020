file = open('Inputs/input3.txt', 'r')
input3 = file.readlines() 

mapa = []
for index in range(len(input3)-1):
    newLine = input3[index][:-1]*(len(input3)*2)
    mapa.append(newLine)
mapa.append(input3[-1]*(len(input3)*2))

x = 0 #x axis
y = 0 #y axis

trees = 0
while y<len(input3):
    if mapa[y][x]=='#':
        trees+=1
    x+=3
    y+=1

print(trees)



#Part 2
x = 0 #x axis
y = 0 #y axis
trees1 = 0
while y<len(input3):
    if mapa[y][x]=='#':
        trees1+=1
    x+=1
    y+=1
print(trees1)
#________________________
x = 0 #x axis
y = 0 #y axis
trees3 = 0
while y<len(input3):
    if mapa[y][x]=='#':
        trees3+=1
    x+=5
    y+=1

print(trees3)
#_________________________
x = 0 #x axis
y = 0 #y axis
trees4 = 0
while y<len(input3):
    if mapa[y][x]=='#':
        trees4+=1
    x+=7
    y+=1

print(trees4)
# _________________________
x = 0 #x axis
y = 0 #y axis
trees5 = 0
while y<len(input3):
    if mapa[y][x]=='#':
        trees5+=1
    x+=1
    y+=2

print(trees5)

print('Solution: ', trees*trees1*trees3*trees4*trees5)
