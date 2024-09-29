"""
22. Write a Python program to count the number 4 in a given list.


"""

lst = [1,4,5,4,7,4,2,3,4]
number = 0

for i in lst:
    if i==4:
        number +=1 
else:
    pass

print(f'Number of 4 in list : {number}')