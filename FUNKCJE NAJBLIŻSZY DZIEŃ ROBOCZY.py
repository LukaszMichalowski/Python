def GiveWorkingDay():
    #wskazuje najbliższą datę roboczą
    from datetime import date
    from datetime import timedelta

    day=date.today()

    if day.weekday()==5:
        workingday=day+timedelta(days=2)
    elif day.weekday()==6:
        workingday=day+timedelta(days=1)
    else:
        workingday=day

    print('working day for',day,'is',workingday)


GiveWorkingDay()

    
