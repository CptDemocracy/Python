from datetime import date

def checkio(date1, date2):
    if date1 > date2:
        raise ValueError("date1 cannot be at a later date than date2")
    DAYS_IN_WEEK = 7
    SATURDAY = 5
    SUNDAY   = 6
    weekend  = [SATURDAY, SUNDAY]
    days_total = (date2 - date1).days
    weekday = date1.weekday()
    count = 0
    for day in range(days_total + 1):
        if weekday in weekend:
            count += 1
        weekday = (weekday + 1) % DAYS_IN_WEEK
    return count
