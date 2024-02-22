#power function
def pow(x,y):
    pow=(x**y)
    return pow
x=2
y=2
print(pow(x, y))

#minimum and maximum
def minmax(mylist):
    minmax = min(mylist), max(mylist)
    return minmax
mylist=[10,123,42,212,53]
print(minmax(mylist))

#check leap year
def leapyear(year):
    if year%400==0:
        return True
    elif year%100==0:
        return False
    elif year%4==0:
        return True
    else:
        return False
year=300
print(leapyear(year))

#bmi calulator
def bmi(h,w):
    bmi=(w/h)
    return(bmi)
h=1.8
w=85
print(bmi(h,w))

#rotating digits
n=31415
def rotatedigits(n):
    lastdigit=n%10
    otherdigits=n//10

    length=0
    while n>0:
        n //=10
        length+=1

    rotated_n = lastdigit*(10**(length-1)) + otherdigits
    return rotated_n    
print(rotatedigits(n))

#minmaxwithloops
def minforloop(list):
    minval=list[0]
    for i in list:
        if i<minval:
            minval=i
    return minval
list=[1,234,2,123,43,21,-30,0]
print(minforloop(list))

def maxforloop(list):
    maxval=list[0]
    for i in list:
        if i>maxval:
            maxval=i
    return maxval
list=[1,234,2,123,43,21,-30,0]
print(maxforloop(list))

def minwhileloop(list):
    minval=list[0]
    i=0
    while i <len(list):
        if list[i]<minval:
            minval=list[i]
        i+=1
    return minval
list=[1,234,2,123,43,21,-30,0]
print(minwhileloop(list))

def maxwhileloop(list):
    maxval=list[0]
    i=0
    while i <len(list):
        if list[i]>maxval:
            maxval=list[i]
        i+=1
    return maxval
list=[1,234,2,123,43,21,-30,0]
print(maxwhileloop(list))

#vowels
def vowels(word):
    vowel="aeiouAEIOU"
    vowelcount=0
    for i in word:
        if i in vowel:
            vowelcount+=1
    return vowelcount
word="UC Berkeley"
print(vowels(word))

#digitalroot
def digitalroot(m):
    dr=0
    while m>0:
        i=m%10
        dr+=i
        m //=10
    return dr
m=12345
print(digitalroot(m))