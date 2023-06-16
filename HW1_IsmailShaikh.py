"""
Ismail Shaikh
CS 100 Section 015
HW 01, September 13, 2022
"""
#Exercise 5b
days= 365
feet= 2
fingers= 10

#Exercise 5c
speed= 65.5
lenght= 6.5
width= 7.8

#Exercise 5d
darkKnight= 'Batman'
fastestAlive= "Flash"
bestShow= "Blue Bloods"

#Textbook Exercise 1.1
print("Solution exercise 1.1")
print ("hello world, If we add no parentheses then a SyntaxError will come up saying that we are missing parentheses.")
print("hello world, If we only have one parenentheses there will be a loading error, where nothing will be printed and its just loading")


#print("hello world)
print("hello world, If we only have one quotation then there will be a SyntaxError:unterminated string literal. If we forget both then we get a SyntaxError:invalid syntax.")
print("+3, This shows that the number is positive and once entered the output will be 3.")
print("If we enter 2++2 then the output is 4, showing that its recognized as a positive number and being added")
print("09 gets a SyntaxError:leading zeroes in a decimal integer literals are not permitted.011 gets the same SyntaxError:Leading zeroes in a decimal integer literals are not permitted.")
print(" 2 2, Will not work and we get SyntaxError:invalid syntax.")


#Textbook Exercise 1.2
print("Solution exercise 1.2")
minue=42 #minutes
secs=42 #seconds
total=minue*60+secs
print(total)
km=10
mile=1.61
numMiles=km/mile
print(numMiles)
totalMins=minue+secs/60
averageMins=totalMins/numMiles
finalMins=int(totalMins/numMiles)
#print(averageMins,finalMins)
finalSecs=(averageMins-finalMins)*60
print("Pace minutes and seconds per mile is",finalMins,":",finalSecs)

#Textbook Exercise 2.1
print("Solution exercise 2.1")
print("If we type 42=n we get SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?")
print("If we put x=y=1, the next line becomes a 3 dot loading. If we then type print(y) the output will be 1 and if we try print(x) the output is 1.")
print("If we add a ; to a print statement then there will be a gap/space and then the output will be shown. I tested it with print('hello world'); and type(1);.")
print("If we add a . to the end of a statement the statement will not work and we get a SyntacError. I tested with print('hello world').")
print("If we try to put xy together like this, it will not work and we will get a SyntaxError.")
#Textbook Exercise 2.2
print("Solution exercise 2.2")
pi=3.14
r=5
volumeSphere=4/3*pi*r**3
print(volumeSphere)
price=24.95
copies=60
bookprice=price*copies
discount=price*0.40*copies
shipping=3+0.75*(copies-1)
totalWholesale=bookprice-discount+shipping
print(totalWholesale)
easyMile=2
easyTime=8*60+15
easyFinal=easyTime*easyMile
tempoMile=3
tempoTime=7*60+15
tempoFinal=tempoTime*tempoMile
travelTime=round((tempoFinal+easyFinal)/60)
startTime=6*60+52
finalTime=(startTime+travelTime)/60
finalTime_hour=int(finalTime)
finalTime_minue=int(((finalTime-7)*60))
print(finalTime_hour,":",finalTime_minue,'am')

