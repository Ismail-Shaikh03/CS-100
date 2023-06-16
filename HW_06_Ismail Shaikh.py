"""
Ismail Shaikh
CS 100 Section 15
Hw 06, October 14, 2022
"""
#Exercise 1
def hasFinalLetter(strList,letters):
    endStrList=[]
    for string in strList:
        if string[-1] in letters:
            if string not in endStrList:
                endStrList.append(string)
    return endStrList

print("Test 1")
strList=["Money", "banana", "PoweR", "Penny"]
letters="yR"
print(hasFinalLetter(strList,letters))

print("Test 2")
strList=["Pie","Honey","SundaY","Light"]
letters="apio"
print(hasFinalLetter(strList,letters))

print("Test 3")
strList=["Mine","PinE","Pizza","Hurry"]
letters="deapleAOPD"
print(hasFinalLetter(strList,letters))
 
#Exercise 2
def isDivisible(maxInt,twoInts):
    endDivisible=[]
    for i in range(1,maxInt):
        if i%twoInts[0]==0 and i%twoInts[1]==0:
            endDivisible.append(i)
    return endDivisible

print("Test 1")
maxInt=(100)
twoInts=(2,5)
print(isDivisible(maxInt,twoInts))

print("Test 2")
maxInt=(5)
twoInts=(4,7)
print(isDivisible(maxInt,twoInts))

print("Test 3")
maxInt=(50)
twoInts=(5,10)
print(isDivisible(maxInt,twoInts))

