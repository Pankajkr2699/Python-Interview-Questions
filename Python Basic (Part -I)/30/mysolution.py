"""
30. Write a Python program that will accept the base and height of a triangle and compute its area.


"""

def areaofTriangle(b,h):
    return(1/2*b*h)

base = int(input('base = '))
height = int(input('height = '))

print(f'area of triangle = {areaofTriangle(base,height)}')
