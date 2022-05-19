

def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False

def day_in_month(month, leap):
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    if month == 2:
        if leap:
            return 29
        return 28
    return 31
    
start_year = 1900
end_year = 2000
newarr = []
arr = []
counting_sundays = 0
count = 0

for year in range(start_year, end_year + 1):
    for month in range(1, 12 + 1):
        for day in range(1, day_in_month(month, is_leap_year(year)) + 1):
            count += 1
            arr.append(day)
            if count % 7 == 0:
                newarr.append(arr)
                arr = []

for n in range(len(newarr)):
    if newarr[n][6] == 1 and n > 365//7:
        counting_sundays += 1

print(counting_sundays)     