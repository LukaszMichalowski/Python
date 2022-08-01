IsWeekend=True
print('Is weekend =',IsWeekend)

Temperature = 13
print('Temperature=',Temperature)

ToDoList=''
print('ToDoList=',ToDoList)

IsHappy= IsWeekend and Temperature >=20 and ToDoList==''
print('is Happy=',IsHappy)
message='Document"cv.doc" was printed on printer: XEROX'
print(message.find(':'))
print(message[message.find(':')+2:])
print(message[message.find('"')+1:])
tmp=message[message.find('"')+1:]
print(tmp[:tmp.find('"')])
q='THE EYES'
countries=['FR','US','DE','RU']
print(countries[1])
countries[1]='GB'
print(countries)
countries.append('PL')
print(countries)
countries.insert(2,'ES')
countries.remove('RU')
print(countries)




