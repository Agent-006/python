year = 2024

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    is_leap_year = True
else:
    is_leap_year = False

if is_leap_year:
    print(year, "is a leap year") 
else:
    print(year, "is not a leap year")