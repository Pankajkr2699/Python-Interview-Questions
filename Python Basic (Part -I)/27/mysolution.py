"""
27. Write a Python program that concatenates all elements in a list into a string and returns it.


"""

lst = [1,2,3,4,5,6]
catenatedList = ''
for i in lst:
    catenatedList = catenatedList + str(i) 

print(catenatedList)
