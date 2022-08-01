#playing with time

import time

print("Current time is....", time.time())
print("\n")
print("Current time is...", time.localtime(time.time()))
print("\n")
print("Current time is...", time.asctime(time.localtime(time.time())))
print("\n")

#playing with calendar

import calendar

print(calendar.month(2021,10,w=5,l=2))
print(calendar.month(2021,10))
print('week day is',calendar.weekday(2021,10,10))
calendar.setfirstweekday(3)
print('is 2021 a leap year',calendar.isleap(2021))
print('leap days 2000-2021',calendar.leapdays(2000,2022))
print(calendar.calendar(2021))
