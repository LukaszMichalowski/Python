from decimal import DivisionByZero


coutries_and_capitals={'Poland':'Warsaw','Germant':'Berlin'}

try:
    print(2/0)
    print(coutries_and_capitals['Poland'])
except ZeroDivisionError:
    print("Wystąpił błąd")


print("--------------------")
try:
    print(2/0)
    print(coutries_and_capitals['Poland'])
except ZeroDivisionError:
    print("Wystąpił błąd")
finally:
    print("To wykona się zawsze")
