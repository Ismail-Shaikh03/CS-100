"""
Ismail Shaikh
CS 100 Section 015
HW 02, September 23, 2022
"""
#Question 1
print("Solution to Question 1")
grades=['C','D','A','A','B','F','C','C','A','B']
print(grades)

frequency1=grades.count("A")
frequency2=grades.count("B")
frequency3=grades.count("C")
frequency4=grades.count("D")
frequency5=grades.count("F")
totalFrequency=[frequency1,frequency2,frequency3,frequency4,frequency5]
print(totalFrequency)

#Question2
print("Solution to Question 2")
dog_breeds=['collie','sheepdog','Chow','Chihuahua']
herding_dogs=dog_breeds[0:2]
print(herding_dogs)
tiny_dogs=dog_breeds[3:]
print(tiny_dogs)
print('Persian' in dog_breeds)
