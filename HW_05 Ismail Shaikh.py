"""
Ismail Shaikh
CS 100 Section 15
Hw 05,October 12, 2022
"""
#Exercise 1
print("Exercise 1")
months=["January","February","March","April","May","June","July","August","September","October","November","December"]
for month in months:
    if month[0]=="J":
        print(month)
#Exercise 2
print("Exercise 2")
for i in range(0,100,2):
    print(i)
for i in range(0,100,5):
    print(i)
#Exercise 3
print("Exercise 3")
horton="A person's a person, no matter how small."
vowels="aeiouAEIOU"
for i in horton:
    if i in vowels:
        print(i)
    
