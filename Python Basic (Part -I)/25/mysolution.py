"""
25. Write a Python program that checks whether a specified value is contained within a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False



"""

def specialValue(n):
    value = [1, 5, 8, 3]
    if n in value:
        return(True)
    else:
        return(False)
    
value = int(input('Enter values : '))
print(specialValue(value))