import datetime

def age(lst):
    dd=int(lst[0])
    mm=int(lst[1])
    yy=int(lst[2])
    today=datetime.datetime.now()
    day=today.day
    month=today.month
    year=today.year
    if dd>today.day:
        day=today.day+30
        month=today.month-1
    if mm>today.month:
        month=today.month+12
        year=today.year-1
    days=day-dd
    months=month-mm
    years=year-yy
    return days,months,years


if __name__=="__main__":
    bdate = input("enter your date of birth in dd/mm/yy format:: ")
    bdate = bdate.split("/")
    days, months, years = age(bdate)
    print("your age is:: ", years, "year", months, 'month', days, 'day')