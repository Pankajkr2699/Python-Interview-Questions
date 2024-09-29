"""
21. Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.


"""

def iseven(n):
    if n%2==0:
        return("Is Even")
    else:
        return("Is Odd")
    

num = int(input("Enter number : "))
print(iseven(num))