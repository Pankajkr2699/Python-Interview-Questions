"""
4. Write a Python program that calculates the area of a circle based on the radius entered by the user.
Sample Output :
r = 1.1
Area = 3.8013271108436504


"""

PI = 3.14 
radius = float(input('Enter radius : '))
area = (2*PI*radius)
print(f"Area of Circle : {format(area,'.2f')}")