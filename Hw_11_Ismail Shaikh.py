"""
Ismail Shaikh
CS 100 Section 015
HW 11 December 5, 2022
"""
class Dog:
    '''Creates class'''
    species="Canis familiaris" #Problem 5
    def __init__(self,dog_name,dog_breed):#Problem 1
        self.name=dog_name
        self.breed=dog_breed
        self.dog_tricks=[]#Problem 2
    def teach(self, trick):#Problem 3
        self.dog_tricks.append(trick)
        print(self.name + "knows how to:" + trick)
    def knows(self,k_trick):#Problem 4
        if k_trick in self.dog_tricks:
            print("Yes"+self.name+ "knows how to"+ k_trick)
            return True
        else:
            print("No"+self.name+"doesn't know how to"+k_trick)
            return False
    
