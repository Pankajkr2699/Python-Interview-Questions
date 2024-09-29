"""
19. Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is".


"""

string = input('Enter an string : ')
isExist = (string[0:2]).lower()
if isExist == 'is':
    print(string)
else:
    print(f'is{string}')