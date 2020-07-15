#list
a=[1,3,10,15]
#add in list
a.append(16)
#to insert at a position
a.insert(0,11)
print(a)
#to delete at a particular position
del a[0]
print(a)
def printMarks(physicsmarks,chemistrymarks=0):
    print('marks scrored in physics',physicsmarks,'chemistry marks is',chemistrymarks)
printMarks(100)
def printTable(num):
    for i in range(1,11):
        print(i*num)
printTable(2)




