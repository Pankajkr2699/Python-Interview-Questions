"""
5. Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.


"""

firstName = input('Enter your First Name  : ')
lastName = input('Enter your Last Name : ')
fullName = firstName + " " + lastName
print(fullName[::-1])