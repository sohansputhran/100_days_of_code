def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        return True
    
    else:
        return False
    
year = int(input("Enter a year: "))
if is_leap_year(year):
    print("Leap year")
else:
    print("Not a leap year")