"""
Ismail Shaikh
CS 100 Section 015
HW 08, November 2, 2022
"""

#Problem 1
def twoWords(lenght,character):
    firstWord=str(input("Enter first word that has a lenght of "+ str(lenght)+":"))
    lst=[]
    while True:
        firstWord=str(input("Enter first word that has a lenght of "+ str(lenght)+":"))
        if len(firstWord)== lenght:
            break
    lst.append(firstWord)
    secondWord=str(input("Enter Second Word Beginning with Character:"))
    while True:
        secondWord=str(input("Enter Second Word Beginning with Character:"))
        if secondWord[0]==character:
            break
    lst.append(secondWord)
    return lst
#Problem 2
def twoWordsV2(lenght,character):
    firstWord=str(input("Enter first word that has a lenght of "+ str(lenght)+":"))
    lst=[]
    while len(firstWord)!= lenght:
        firstWord=str(input("Enter first word that has a lenght of "+ str(lenght)+":"))
    lst.append(firstWord)
    secondWord=str(input("Enter Second Word Beginning with Character:"))
    while secondWord[0]!= character:
        secondWord=str(input("Enter Second Word Beginning with Character:"))
    lst.append(secondWord)
    return lst

#Problem 3
def enterNewPassword():
    while True:
        password=input("Enter a password with 8-15 characters:")
        if len(password)<8 or len(password)>15:
            print("Password not in lenght,redo!")
        else:
            if not any(digit.isdigit() for digit in password):
                print("Password should have a digit!")
                password=input("Enter a password with 9-15 character with one being a digit!:")
            else:
                print("Congratulations your password is accepted!")
                break
    return password

#Problem 4
import random
counter=0
a_i=int(random.randint(0,51))
player=int(input("Guess the number 1-50, you have 5 tries!:"))
counter+=1
while counter<=5:
    if player < a_i:
        print("Value is too low!")
        player=int(input("Guess again!"))
        counter+=1
    elif player > a_i:
        print("Value is too high!")
        player=int(input("Guess again!"))
        counter+=1
    elif player == a_i:
        print("You got the right answer!")
        break
    if counter>=5:
        print("You ran out of attempts!")
        break
