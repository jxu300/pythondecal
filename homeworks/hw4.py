#2.1
list_0to50 = (list(range(51)))

#2.2
lis = [2,3,4]
def square(lis):
    return [i**2 for i in lis]
#syntax error, put i**2 after "for i in lis"

#2.3
listA = [1,2,3,4,5,6,7,8,9,10]
listB = [11,12,13,14,15,16,17,18,19,20]
listC = listA + listB
listD = [i for i in listC if i % 2 ==0]
# invalid syntax, forgot an "i" in line 15

#2.4
twodlist=[]
n=1
for i in range(5):
    row = []
    for j in range (5):
        row.append(n)
        n += 1
    twodlist.append(row)

#2.5
twodlist=[]
n=1
for i in range(5):
    row = []
    for j in range (5):
        if n % 3 ==0:
            row.append("?")
        else:
            row.append(n)
        n += 1
    twodlist.append(row)

#2.6
lis = [1,1,2,3,4,4]
def removeDuplicates(lis):
    newlist = []
    for i in lis:
        if i not in newlist:
            newlist.append(i)
    return newlist
print(removeDuplicates(lis))
    
    




