"""
9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014


"""

exam_start_date = input('Enter date (dd,mm,yyyy) : ').split(',')
day = exam_start_date[0]
month = exam_start_date[1]
year = exam_start_date[2]
print(f"Date : {day}/ {month}/{year}")