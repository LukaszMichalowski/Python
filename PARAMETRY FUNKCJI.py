def GiveWorkingDay(year,month,day):
    #wskazuje najbliższą datę roboczą
    from datetime import date
    from datetime import timedelta

    #day=date.today()
    day=date(year,month,day)

    if day.weekday()==5:
        workingday=day+timedelta(days=2)
    elif day.weekday()==6:
        workingday=day+timedelta(days=1)
    else:
        workingday=day

    print('working day for',day,'is',workingday)


GiveWorkingDay(2021,10,16)

    
