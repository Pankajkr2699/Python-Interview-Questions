"""
7. Write a Python program that accepts a filename from the user and prints the extension of the file.
Sample filename : abc.java
Output : java


"""

fileName = input('Enter file name : ').split('.')
print(f"Extension is : {fileName[1]}")
