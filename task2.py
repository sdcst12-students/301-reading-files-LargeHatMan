"""
Read the data from one of the task02 text files.
The data from this file contains 3 numbers on each line.  Determine how many lines of this file contains Pythagorean triples.
Pythagorean triples are numbers where all of the sides are integers, and the 3 sides form a right triangle.
The triples contained are : { 2a : 6, 2b: 4, 2c: 11}
"""
filename= 'task02a.txt'
filename2= 'task02c.txt'
filename3= 'task02b.txt'


file = open(filename,'r')
file2 = open(filename2,'r')
file3 = open(filename3,'r')

data = file.read()
data2 = file2.read()
data3 = file3.read()

list = data.split("\n")
list2 = data2.split("\n")
list3 = data3.split("\n")

greg=[]
geoff = []

for i in enumerate(list):
    greg.append(i[1])
    if i[1] == "":
        a=int(greg[0])
        b=int(greg[1])
        c=int(greg[2])
        if c**2+a**2==b**2:
            print('borgir')
            geoff.append(b**2)
        if a**2+b**2==c**2:
            print('borgir')
            geoff.append(c**2)
        if c**2+b**2==a**2:
            print('borgir')
            geoff.append(a**2)
        greg.clear()
    else:
        print(greg)
    if greg==['65', '48', '45']:
        print(geoff)
        aRights = geoff.index((geoff[-1]))+1
        break
geoff.clear()

for i in enumerate(list2):
    greg.append(i[1])
    if i[1] == "":
        a=int(greg[0])
        b=int(greg[1])
        c=int(greg[2])
        if c**2+a**2==b**2:
            print('borgir')
            geoff.append(b**2)
        if a**2+b**2==c**2:
            print('borgir')
            geoff.append(c**2)
        if c**2+b**2==a**2:
            print('borgir')
            geoff.append(a**2)
        greg.clear()
    else:
        print(greg)
    if greg==['65', '48', '45']:
        print(geoff)
        aRights = geoff.index((geoff[-1]))+1
        break
geoff.clear()

for i in enumerate(list3):
    greg.append(i[1])
    if i[1] == "":
        a=int(greg[0])
        b=int(greg[1])
        c=int(greg[2])
        if c**2+a**2==b**2:
            print('borgir')
            geoff.append(b**2)
        if a**2+b**2==c**2:
            print('borgir')
            geoff.append(c**2)
        if c**2+b**2==a**2:
            print('borgir')
            geoff.append(a**2)
        greg.clear()
    else:
        print(greg)
    if greg==['65', '48', '45']:
        print(geoff)
        aRights = geoff.index((geoff[-1]))+1
        break
geoff.clear()
    