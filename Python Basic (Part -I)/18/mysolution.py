"""
18. Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.


"""

x = int(input('Number : '))
y = int(input('Number : '))
z = int(input('Number : '))

if x==y==z: 
    print((x+y+z)*3)
else:
    print(x+y+z)