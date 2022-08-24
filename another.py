print("A program that calculates the distance between 2 points of a coordinate")
x2 = int(input('value for x2:  '))
x1 = int(input('value for x1:  '))
y2 = int(input('value for y2:  '))
y1 = int(input('value for y1:  '))

a = x2-x1
b = y2-y1

c = a**2 +b**2
d = c**0.5

print (d)