def is_leap(year):
    leap = True
    
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return leap
            return not leap
        return leap
    return not leap

year = int(input())
print(is_leap(year))