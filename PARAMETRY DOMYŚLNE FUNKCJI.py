from datetime import date
from datetime import timedelta

def GiveWorkingDay(year=date.today().year,\
                   month=date.today().month,\
                   day=date.today().day):
    #wskazuje najbliższą datę roboczą
    #day=date.today()
    day=date(year,month,day)

    if day.weekday()==5:
        workingday=day+timedelta(days=2)
    elif day.weekday()==6:
        workingday=day+timedelta(days=1)
    else:
        workingday=day

    print('working day for',day,'is',workingday)


GiveWorkingDay()

    
