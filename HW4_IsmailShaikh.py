"""
Ismail Shaikh
CS 100 Section 015
HW 4 October 4, 2022
"""

#Exercise 1
print("Exercise 1")
a=3
b=4
c=5
if a<b:
    print("Ok")
if c<b:
    print("Ok")
if a+b==c:
    print("Ok")
if a**2+b**2==c**2:
    print("Ok")
#Exercise 2
print("Exercise 2")
a=3
b=4
c=5
if a<b:
    print("Ok")
else:
    print("Not Ok")
if c<b:
    print("Ok")
else:
    print("Not Ok")
if a+b==c:
    print("Ok")
else:
    print("Not Ok")
if a**2+b**2==c**2:
    print("Ok")
else:
    print("Not Ok")

#Exercise 3
print("Exercise 3")
color=input("What color?:")
line_width=input("What line width?:")
line_lenght=int(input("What line lenght?:"))
shape=input("Which shape:line, triangle, or square?:")
import turtle
aScreen=turtle.Screen()
pointer=turtle.Turtle()
pointer.color(color)
pointer.width(line_width)
pointer.forward(line_lenght)
pointer.left(120)
pointer.forward(line_lenght)
pointer.left(120)
pointer.forward(line_lenght)
