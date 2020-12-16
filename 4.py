import string

file = open('Inputs/input4.txt')
input4 = file.readlines()

lines = []
for i in input4:
    lines.append(i.strip('\n'))

documents = []
newLine = ''
for line in lines:
    if line!='':
        newLine+=' '+line
    else:
        documents.append(newLine[1:].split(' '))
        newLine=''

documents2 = []
for document in documents:
    valores = {}
    for value in document:
        v = value.split(':')
        key = v[0]
        value = v[1]
        valores[key]=value
    documents2.append(valores)

#Check if the values exist in the documents

# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)

fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']

passports = 0
for document in documents2:
    if ('byr' in document and 'iyr' in document and 'eyr' in document and 'hgt' in document and 'hcl' in document and 'ecl' in document and 'pid' in document):
        passports+=1

print(passports)



#Part 2

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

passports2 = 0
for document in documents2:
    if ('byr' in document and 'iyr' in document and 'eyr' in document and 'hgt' in document and 'hcl' in document and 'ecl' in document and 'pid' in document):
        if int(document['byr'])>=1920 and int(document['byr'])<=2002:
            if int(document['iyr'])>=2010 and int(document['iyr'])<=2020:
                if int(document['eyr'])>=2020 and int(document['eyr'])<=2030:
                    height = document['hgt']
                    measure = height[-2:]
                    number = height[0:-2]
                    if number!='' and ((measure=='cm' and int(number)>=150 and int(number)<=193) or (measure=='in' and int(number)>=59 and int(number)<=76)):
                        colorHexa = document['hcl']
                        hexa = colorHexa[0]
                        color = colorHexa[1:]
                        if(hexa=='#' and all(letra in string.hexdigits for letra in color)):
                            eyeColor = document['ecl']
                            if(eyeColor in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
                                number = document['pid']
                                if len(number)==9:
                                    passports2+= 1
                                                 

print(passports2)